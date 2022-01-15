#!/usr/bin/python

import json
import operator
import pprint
import sys
import getopt
import re
import optparse
import os
import time


def main():
  desc = """
  Process the stdin line by line. apply the following operators on each line.
  """
  parser = optparse.OptionParser(description = desc)
  parser.add_option("", "--version",
                    action="store_true",
                    help="print version number",
                    dest="version",
                    default=False)
  parser.add_option("", "--Prefix",
                    type=str,
                    help="prefix each line with the given string",
                    dest="prefix",
                    default="")
  parser.add_option("", "--Postfix",
                    type=str,
                    help="postfix each line with the given string",
                    dest="postfix",
                    default="")
  parser.add_option("", "--Grep",
                    type=str,
                    help="output lines containing the given RE",
                    dest="grep",
                    default=None)
  parser.add_option("", "--Splice",
                    type=str,
                    help="Output the given RE",
                    dest="splice",
                    default=None)
  parser.add_option("", "--Replace",
                    action="append",
                    help="Replace --Replace RE with --With",
                    dest="Replace",
                    default=[])
  parser.add_option("", "--With",
                    action="append",
                    help="Replace --Replace RE with --With",
                    dest="With",
                    default=[])
  (options, filenames) = parser.parse_args()

  if len(options.Replace) != len(options.With):
      print "ERROR: 'replace' and 'with' num doesn't match"
      sys.exit(10)

  if options.version:
    print("0.1")
    sys.exit(0)

  if not len(filenames):
      filenames = ['-']

  for filename in filenames:
    if filename == "-":
      input_file = sys.stdin
    else:
      input_file = open(filename, "r")

    for line in input_file:
        line = line.rstrip('\n')

        if options.splice:
          r = re.search(options.splice, line)
          if r and r.group():
            line = r.group()
          else:
            continue

        if options.grep and not re.search(options.grep, line):
          continue

        for i in range(len(options.Replace)):
          pat = options.Replace[i]
          rep = options.With[i]
          line = re.sub(pat, rep, line)

        o = options.prefix
        o += line
        o += options.postfix

        # output the line
        print o

if __name__ == "__main__":
  main()


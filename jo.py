#!/usr/bin/python

import json
from posixpath import split
import sys
import optparse

def recursive_set(options, root, k, v):
  comps = k.split(options.sep)
  comp = comps[0]
  if len(comps) == 1:
    root[comp] = v
  else:
    d = root.get(comp, {})
    recursive_set(options, d, ".".join(comps[1:]), v)
    root[comp] = d

# TODO:: add a way to specify the type of a value (int/bool)
# TODO:: add a way to add a timestamp in s and ms

def main():
  desc = """
  Construct and output a nested JSON object from k=v pairs
  """
  parser = optparse.OptionParser(description = desc)
  parser.add_option("", "--version",
                    action="store_true",
                    help="print version number",
                    dest="version",
                    default=False)
  parser.add_option("", "--sep",
                    help="key separator to use",
                    dest="sep",
                    default=".")
  (options, vars) = parser.parse_args()

  if options.version:
    print("0.2")
    sys.exit(0)

  # root object to be built:
  root = {}

  # parse the (k=v)'s and recursively:
  for kv in vars:
    k = kv.split("=")[0]
    v = kv.split("=")[1]
    recursive_set(options, root, k, v)

  # print the output
  print(json.dumps(root, sort_keys=True))
if __name__ == "__main__":
  main()

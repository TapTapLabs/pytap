# pytap
Python command line tools

## line.py

Splice and extract data from each line

Examples:

```
cat lines.txt
A
B
C

# Prefix / Postfix the line with strings:
cat lines.txt | ./line.py --Prefix "prefix: " --Postfix ": postfix"
prefix: A: postfix
prefix: B: postfix
prefix: C: postfix

# extract data with an RE:
cat lines.txt | ./line.py --splice "A|B"
A
B

# extract an RE:
echo "x,y=100,x=100" | python line.py --splice "y=\d+"
y=100

# extact an RE group:
echo "x=10,y=11" | python line.py --splice "y=(\d+)"
11

# prefix and postfix:
echo "x=10,y=11" | python line.py --grep "y=(\d+)" --prefix "{" --postfix "}"
{x=10,y=11}

# replace / with:
echo "x=10,y=11" | python line.py --replace "x=(\d+)" --with "x=666"
x=666,y=11

```

## jo.py

Create a nested JSON object from the command line

Examples:

```
# build a nested JSON object from the command line:
python jo.py x=1 y=2  z.a=1 z.b=2 z.x=x | jq '.'
{
  "x": "1",
  "y": "2",
  "z": {
    "a": "1",
    "b": "2",
    "x": "x"
  }
}

```


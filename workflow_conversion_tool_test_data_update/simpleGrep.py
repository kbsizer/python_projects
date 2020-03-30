#!/usr/bin/env python
import re
import sys

# process command-line args
# if 2 args were not passed on the command-line, print usage and exit
if len(sys.argv) < 3:
    raise SystemExit(f"Usage: {sys.argv[0]} <regex> <fileToScan>")
regex = sys.argv[1]
fileToScan = sys.argv[2]

# build regex
regexPattern = re.compile(regex)

# process file line-by-line
f = open(fileToScan)
try:
    for line in f:
        if regexPattern.search(line):
        	print(line)
finally:
    f.close()
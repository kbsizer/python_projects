#!/usr/bin/env python

# Process the given file line-by-line, replacing every occurrance of 
#    (Otherwise)
# with
#    (Otherwise #<lineNumber> TEMP)

import sys
import re

# if a filename was not passed on the command-line, print usage and exit
if len(sys.argv) <= 2:
    raise SystemExit(f"Usage: {sys.argv[0]} <SASWorkflowFileName.xml> <targetWorkflowFileName.xml>")

# get first arg  (argv[0] is the script's name)
srcWorkflowFile = sys.argv[1]
destWorkflowFile = sys.argv[2]

# build regex
regexPattern = re.compile(r'\(Complete\)')  # must escape parens because they are capture group identifiers

# open file and process it line-by-line
inFile = open(srcWorkflowFile, "r")
outFile = open(destWorkflowFile, "w")
try:
    for line in inFile:
        match = regexPattern.search(line)
        if match:
            print(line)
        
finally:
    inFile.close()
    outFile.close()

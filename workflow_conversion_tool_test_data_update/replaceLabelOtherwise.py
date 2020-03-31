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
regexPattern = re.compile(r'\(Otherwise\)')  # must escape parens because they are capture group identifiers

# open file and process it line-by-line
inFile = open(srcWorkflowFile, "r")
outFile = open(destWorkflowFile, "w")
matchCount = 1
lineNo = 0
try:
    for line in inFile:
        lineNo += 1
        replacementText = f"(Otherwise #{lineNo} TEMP)"
        opt = re.sub(regexPattern, replacementText, line)
        # print(f"{lineNo}: {opt.rstrip()}")  # rstrip() removes trailing space and newline
        outFile.write(opt)        
finally:
    inFile.close()
    outFile.close()

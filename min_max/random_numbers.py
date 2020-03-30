"""
Generates one or more columns of random numbers.

Syntax:
    $ python random_numbers.py [rows [columns]]

if columns is omitted, 1 is assumed.
if rows is omitted, 10 is assumed.
"""

import random as rand
import sys

# read command=line args
columnsToGenerate = 1
rowsToGenerate = 10
parmCount = len(sys.argv) - 1
print (f'Passed {parmCount} args')
if parmCount > 0:
    rowsToGenerate = int(sys.argv[1])
    if parmCount > 1:
        columnsToGenerate = int(sys.argv[2])

for r in range(rowsToGenerate):
    for c in range(columnsToGenerate):
        prefix = '' if c==0 else ','
        sys.stdout.write(f'{prefix}{rand.random():.5f}')
#        print(rand.random())
    sys.stdout.write('\n')



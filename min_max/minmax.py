"""
Python script to return the min, max and average of a 
list of values.

Illustrates working with command-line parameters 
and CSV files in Python.

See: https://realpython.com/python-csv
"""

import csv

# Parse command-line args


# Open and process file
with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    line_count = 0
    for row in csv_reader:
        for col in row:
            printf(col)
        print('--------')

    print(f'Processed {line_count} lines.')

import sys
import os
import csv
from tabulate import tabulate

def format_pizza_table(x):
    if not x.endswith('.csv'):
        sys.exit("not a .CSV file")

    if not os.path.exists(x):
        sys.exit("file does not exist")

    with open(x, 'r', newline='') as csvfile:
        n = csv.reader(csvfile)
        h = next(n)
        td = [h]

        for row in n:
            td.append(row)

        table = tabulate(td, headers='firstrow', tablefmt='grid')

        return table

if len(sys.argv) != 2:
    sys.exit("Usage: python pizza.py <filename.csv>")

x = sys.argv[1]

try:
    formatted_table = format_pizza_table(x)
    print(formatted_table)
except KeyboardInterrupt:
    sys.exit("canceled by user.")

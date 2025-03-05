from pathlib import Path
import csv

from matplotlib import pyplot as plt




path =Path('daywork.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines) 
header_row = next(reader)
print(header_row)


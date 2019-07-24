import csv
from os import listdir
from os.path import isfile
from graphing_interface import interface


files = [f for f in listdir('.') if isfile(f)]
full_data = []

filenames = []
for filename in files:
    if filename.endswith(".CSV"):
        filenames.append(filename)
label_row = [filenames,[]]
full_data.append(label_row)
for filename in files:
    if filename.endswith(".CSV"):
        with open(filename) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            x = []
            y = []
            for row in readCSV:
                x_val = float(row[0])
                y_val = float(row[1])
                x.append(x_val)
                y.append(y_val)
            set_val = []
            set_val.append(x)
            set_val.append(y)
            full_data.append(set_val)

interface(full_data)





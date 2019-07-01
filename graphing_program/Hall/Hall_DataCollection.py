import csv
from os import listdir
from os.path import isfile
import os
import url
from tkinter import filedialog


files = [f for f in listdir('.') if isfile(f)]
full_data = []

for filename in files:
    if filename.endswith(".txt"):
        with open(filename) as csvfile:
            data = []
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                data.append(row)
            if files.index(filename) ==0:
                data6 = data[6][0].split()
                full_data.append(data6)
            data7 = data[7][0].split()
            full_data.append(data7)
print(full_data)
filename = filedialog.asksaveasfilename(initialdir= os.getcwd(), title="Select file", filetypes=(
        ('CSV files', '*.csv'),('All files','*.*'))) + '.csv'
if filename != '.csv':
    url.dataset_to_csv(full_data, filename)
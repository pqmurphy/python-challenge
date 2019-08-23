# Perform Imports
import csv
import os, sys

# Set Variables
months = 0
totalin = 0
totals = []
diffs = []
montharr = []

# Set file path
dirpath = os.path.dirname(sys.argv[0])
csvpath = os.path.abspath(dirpath)+"/budget_data.csv"

# Open file

with open(csvpath, newline = '') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)

    for row in csvreader:
        totals.append(int(row[1]))
        diffs.append(totals[months] - totals[months-1])
        montharr.append(row[0])
        months = months + 1
        totalin = totalin + int(row[1])

GrInc = max(diffs)
GrDec = min(diffs)
GrIncInd = diffs.index(GrInc) 
GrDecInd = diffs.index(GrDec)

# Print Results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {months}")
print(f"Total: ${totalin}")
print(f"Greatest Increase in Profits: {montharr[GrIncInd]} (${GrInc})")
print(f"Greatest Decrease in Profits: {montharr[GrDecInd]} (${GrDec})")

printfile = open("analysis.txt", "w+")
printfile.write(f"Financial Analysis\n------------------\nTotal Months: {months}\nTotal: ${totalin}\nGreatest Increase in Profits: {montharr[GrIncInd]} (${GrInc})\nGreatest Decrease in Profits: {montharr[GrDecInd]} (${GrDec})")
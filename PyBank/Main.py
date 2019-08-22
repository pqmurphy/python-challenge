import csv

# Set Variables
months = 0
totalin = 0
totals = []
diffs = []
montharr = []

# Set file path
csvpath = "/Users/patrickmurphy/Documents/Northwestern/Python/PyBank/budget_data.csv"

# Open file

with open(csvpath, newline = '') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)

    #print(f"CSV Header: {csvheader}")

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
printfile.write(f"Financial Analysis\n ------------------\nTotal Months: {months}\nTotal: ${totalin}\nGreatest Increase in Profits: {montharr[GrIncInd]} (${GrInc})\nGreatest Decrease in Profits: {montharr[GrDecInd]} (${GrDec})")

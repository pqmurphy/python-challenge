# Perform Imports
import csv
import decimal

# Set Variables
votes = 0
khan = 0
correy = 0
li = 0
otooley = 0
percentages = []
bad = 0

# Get File
csvpath = "/Users/patrickmurphy/Documents/Northwestern/Python/PyPoll/election_data.csv"

# Get Votes
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:

        if (row[2] == "Khan"):
            khan = khan +1
        elif (row[2] == "Correy"):
            correy = correy + 1
        elif (row[2] == "Li"):
            li = li +1
        elif (row[2] == "O'Tooley"):
            otooley = otooley + 1
        else:
            bad = bad + 1

        votes = votes + 1

# Get Percentages
kp = round((khan/votes)*100,3)
cp = round((correy/votes)*100,3)
lp = round((li/votes)*100,3)
op = round((otooley/votes)*100,3)
bp = round((bad/votes)*100, 3)

# Get Winner
percentages = [kp, cp, lp, op, bp]
candidates = ["Khan", "Correy", "Li", "O'Tooley", "Bad Ballots"]
winner = candidates[percentages.index(max(percentages))]

# Print Results
print("Election Results")
print("-------------------")
print(f"Total Votes: {votes}")
print("-------------------")
print(f"Khan: {kp}% ({khan})")
print(f"Correy: {cp}% ({correy})")
print(f"Li: {lp}% ({li})")
print(f"O'Tooley: {op}% ({otooley})")
print(f"Bad Ballots: {bp}% ({bad})")
print("-------------------")
print(f"Winner: {winner}")
print("-------------------")

# Create File
printfile = open("analysis.txt", "w+")
printfile.write(f"Election Results\n------------------\nTotal Votes: {votes}\nKhan: {kp}% ({khan})\nCorrey: {cp}% ({correy})\nLi: {lp}% ({li})\nO'Tooley: {op}% ({otooley})\nBad Ballots: {bp}% ({bad})\n------------------\nWinner: {winner}\n------------------")
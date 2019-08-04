import os
import csv

poll_csv=os.path.join("Resources", "election_data.csv")

votes=0
candi_votes=""
candi=""
percent={}
winning_votes=0
winner=""

with open(poll_csv, newline="") as csvfile:
    csvreader = csv.reader(poll_csv, delimiter=",")
    next(csvreader)
    for row in csvreader:
        votes=votes+1
        candi=row[2]
        if candi in candi_votes:
            candi_votes[candi]=candi_votes[candi]+1
        else:
            candi_votes[candi]=1
for person, votes in candi_votes.items():
    percent[person]='{0:.0%}'.format(total_votes/votes)
    if total_votes>winning_votes:
        winning_votes=total_votes
        winner=person

print("Election Results")
print("-------------------------")
print("Total Votes: {votes}")
print("-------------------------")
for person, total_votes in candi_votes.items():
    print(f"{person}:{candi_votes[person]} ({total_votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

import sys
import csv

#  Initialize all variables used below. Not needed for Python
#  but is a good practice

MONTH_COLUMN = 0
PL_COLUMN = 1

cand_vote_count = {}
total_votes = 0

with open("election_data.csv", 'r', encoding="utf8") as infile, \
     open("election_results.txt", 'w', newline=None) as outfile:
       f_handle = [outfile, sys.stdout]
       reader = csv.reader(infile, delimiter=",")

       # Read the header row first (skip this step if there is no header)
       csv_header = next(reader)

       for row in reader:
         # Do not process empty line in CSV file
         if row:
           total_votes += 1
           name = row[2]
           #if cand_vote_count.get(name) == None:
           if not name in cand_vote_count:
             cand_vote_count[name] = 1
           else:
             cand_vote_count[name] += 1
         # else:
           # print("Empty line")

       winner_cnt = 0
       for curr_file in f_handle:
         print("Election Results", file=curr_file)
         print("---------------------", file=curr_file)
         print(f"Total Votes: {total_votes}", file = curr_file)
         print("---------------------", file=curr_file)
         for name, vote_cnt in cand_vote_count.items():
           if total_votes > 0: # Catch div by zero
             percent = vote_cnt / total_votes
             percent = round(percent, 3)
             percent *= 100
           else:
             percent = 0
           if winner_cnt < vote_cnt:
             winner_cnt = vote_cnt
             winner = name
           print(f"{name}: %2.3f%% ({vote_cnt})" % percent, file = curr_file)
         print("---------------------", file=curr_file)
         print(f"Winner: {winner}", file=curr_file)
         print("---------------------", file=curr_file)


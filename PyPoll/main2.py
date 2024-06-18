import os
import csv

# folder path for input file
csvpath = os.path.join('Resources', 'election_data.csv')

# Lists to store data and set all variables
ballot = []
county = []
candidate = []

votes = {}

# open input file 
with open(csvpath, encoding='UTF-8') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)
    #print(f"Header: {csv_header}")

    #storing data individually to lists and getting total number of votes
    for row in csvreader:
        ballot.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
total_votes = int(len(ballot))

#storing candidate name and vote count in dictionary
for cand in candidate:
    if cand in votes:
        votes[cand] +=1
    else:
         votes[cand] = 1       

#printing all data
print(f'Total Votes: {total_votes}') 

for cand, vt in votes.items():         
    print(str(cand)+": "+str(round((vt/total_votes*100), 3))+"% "+"("+str(vt)+")")
    
#getting the winner from who got max vote count
winner = max(zip(votes.values(), votes.keys()))[1]
print(winner)   

# setting output file locaaion and open output file
output_path = os.path.join("analysis", "analysis2_vote.txt")
with open(output_path, 'w', newline='') as file:
    writer = csv.writer(file)
#writing the report  
    writer.writerow(["Election Results"])
    writer.writerow(["----------------------------"])
    writer.writerow(["Total Votes: " + str(total_votes)])
    writer.writerow(["----------------------------"])
    for cand, vt in votes.items():         
        writer.writerow([str(cand) + ": " + str(round((vt/total_votes*100), 3)) + "% (" + str(vt) + ")"])
    writer.writerow(["----------------------------"])
    writer.writerow(["Winner: " + str(winner)])
    writer.writerow(["----------------------------"])
   
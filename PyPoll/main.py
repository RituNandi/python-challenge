import os
import csv

# folder path for input file
csvpath = os.path.join('Resources', 'election_data.csv')

# Lists to store data and set all variables
ballot = []
county = []
candidate = []
total_charles = 0
percent_charles = 0
total_diana = 0
percent_diana = 0
total_raymon = 0
percent_raymon = 0
cand_names = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]


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


#calculating total number of votes for each candidate
for i in candidate:
    if str(i) == cand_names[0]:
       total_charles = total_charles + 1
    elif str(i) == cand_names[1]:
       total_diana = total_diana + 1
    else:
       str(i) == cand_names[2]
       total_raymon = total_raymon + 1       

#calculating percentage of votes for each candidate
percent_charles = round((total_charles / total_votes * 100), 3) 
percent_diana = round((total_diana / total_votes * 100), 3) 
percent_raymon = round((total_raymon / total_votes * 100), 3) 

#Getting the winner
if percent_charles > percent_diana and percent_raymon:
    winner = cand_names[0]

if percent_diana > percent_charles and percent_raymon:
    winner = cand_names[1]

if percent_raymon > percent_charles and percent_diana:
    winner = cand_names[2]

#printing all data to terminal
print(f'Total Votes: {total_votes}')    
print(f'{str(cand_names[0])}: {percent_charles}% ({total_charles})')
print(f'{str(cand_names[1])}: {percent_diana}% ({total_diana})')
print(f'{str(cand_names[2])}: {percent_raymon}% ({total_raymon})')
print(f'Winner: {str(winner)}')                 

# setting output file locaaion and open output file
output_path = os.path.join("analysis", "analysis_vote.txt")
with open(output_path, 'w', newline='') as file:
    writer = csv.writer(file)
#writing the report  
    writer.writerow(["Election Results"])
    writer.writerow(["----------------------------"])
    writer.writerow(["Total Votes: " + str(total_votes)])
    writer.writerow(["----------------------------"])
    writer.writerow([str(cand_names[0]) + ": " + str(percent_charles) + "% (" + str(total_charles) + ")"])
    writer.writerow([str(cand_names[1]) + ": " + str(percent_diana) + "% (" + str(total_diana) + ")"])
    writer.writerow([str(cand_names[2]) + ": " + str(percent_raymon) + "% (" + str(total_raymon) + ")"])
    writer.writerow(["----------------------------"])
    writer.writerow(["Winner: " + str(winner)])
    writer.writerow(["----------------------------"])
   
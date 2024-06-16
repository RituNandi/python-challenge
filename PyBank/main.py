import os
import csv

# folder path for input file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Lists to store data and set all variables
month = []
amount = []
changes = []
changes_2 = []
total_amount = 0
greatest_changes = 0
greatest_increase = 0
greatest_decrease = 0
average_change = 0
change_profit = 0

# open input file 
with open(csvpath, encoding='UTF-8') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)
    #print(f"Header: {csv_header}")

    #storing month and amount to list and getting total number of months
    for row in csvreader:
        month.append(row[0])
        amount.append(row[1])
    total_months = int(len(month))
    
for i in amount:

    # summing up all amount to get the total
    total_amount += int(i)
    #calculating the change in profit/loss amount starting from first row, first row has no change
    change_profit = int(i) - greatest_changes
    # storing current row amount value for the difference calculation for the next row for amount 
    greatest_changes = int(i)
    # storing the calculated amount changes 
    changes.append(change_profit)
                 
#here discarding the first row from the change in amount as beginning value should not contribute in change calculation
for j in changes[1:]:
    changes_2.append(j)  

#getting greatest increase in profits
greatest_increase = max(changes_2)

#getting greatest decrease in profits
greatest_decrease = min(changes_2) 

#calculating average of change in amount to 2 decimal placess
average_change =  round((sum(changes_2) / len(changes_2)), 2)  

#getting the date associated with greatest increase and decrease from the first change list,
#same can be achieved using 2nd change list but then need to substract 1 to match the data index
increase_text = month[changes.index(greatest_increase)]
decrease_text = month[changes.index(greatest_decrease)]

#printing all data to terminal
print(f'Total Months: {total_months}')    
print(f'Total: ${total_amount}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {increase_text} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {decrease_text} (${greatest_decrease})')


# open output file
output_path = os.path.join("analysis", "analysis_result.txt")
with open(output_path, 'w', newline='') as file:
    writer = csv.writer(file)
#writing the report  
    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------------------"])
    writer.writerow(["Total Months: " + str(total_months)])
    writer.writerow(["Total: " + "$" + str(total_amount)])
    writer.writerow(["Average Change: " + "$" + str(average_change)])
    writer.writerow(["Greatest Increase in Profits: " + str(increase_text) + " ($" + str(greatest_increase) + ")"])
    writer.writerow(["Greatest Decrease in Profits: " + str(decrease_text) + " ($" + str(greatest_decrease) + ")"])
   
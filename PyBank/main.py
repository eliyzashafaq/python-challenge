# Import dependencies
import os
import csv

# create variables
total_months = 0
net_profit_loss = 0
profit_loss_val = 0
changes = 0
great_inc_val = 0
great_dec_val = 0
great_inc_date = []
great_dec_date = []
differences = []


# Open and read the budget data file
csv_path = "Resources/budget_data.csv"
budget_data = os.path.join('..', 'Resources', 'budget_data.csv')
with open(csv_path, "r", encoding="utf") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

  # Read/loop through each row of data after the header
    for row in csvreader:
        total_months = total_months + 1
        net_profit_loss = net_profit_loss + int(row[1])
        date = row[0]
        
        prev_profit_loss_val = profit_loss_val
        profit_loss_val = int(row[1])
        diff = profit_loss_val - prev_profit_loss_val
        changes = changes + diff
        differences.append(diff)
    
        if diff > great_inc_val:
            great_inc_val = diff
            great_inc_date = date
        elif diff < great_dec_val:
            great_dec_val = diff
            great_dec_date = date
        else: continue
    
# reverse the first change        
differences.pop(0) 
profit_loss_avg = round(sum(differences)/len(differences),2)

# Print out the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {net_profit_loss}")
print(f"Average Change: ${profit_loss_avg}")
print(f"Greatest Increase in Profits: {great_inc_date} (${great_inc_val})")
print(f"Greatest Decrease in Profits: {great_dec_date} (${great_dec_val})")

# Export a text file with the results
output_file = os.path.join('..', 'analysis', 'analysis.txt')
file1 = open("analysis/alysis.txt","w")
L = ["Financial Analysis \n",
     "------------------------\n",
     f"Total Months: {total_months}\n",
     f"Total: ${net_profit_loss} \n",
     f"Average Change: ${profit_loss_avg} \n",
     f"Greatest Increase in Profits: {great_inc_date} (${great_inc_val}) \n",
     f"Greatest Decrease in Profits: {great_dec_date} (${great_dec_val}) \n"]
file1.writelines(L)
file1.close()
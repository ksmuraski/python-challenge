import os
import csv

profit_csv = os.path.join("Resources", "budget_data.csv")


#Variables
total_months=0
months=[]
total_profit=0
current_months_profit=0
prior_month_profit=0
profit_changes=0
profit_changes=[]


with open(profit_csv, newline="") as csvfile:
    csvreader = csv.reader(profit_csv, delimiter=",")
    next(csvreader)
    for row in csvreader:
        total_months=total_months+1
        months.append(row[0])
        current_months_profit=int(row[0])
        total_profit=total_profit+current_months_profit
        if total_months >1:
            profit_changes=current_months_profit-prior_month_profit
            profit_changes.append(profit_changes)
        prior_month_profit=current_months_profit

#profit changes
max_changes=max(profit_changes)
min_changes=min(profit_changes)
max_months_indx=profit_changes.index(max_changes)
min_months_indx=profit_changes.index(min_changes)
min_month=months[min_months_indx]
max_month=months[max_months_indx]
revenue_changes=sum(profit_changes)
avg_changes=revenue_changes/(total_months-1)

#printing it all out
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average  Change: ${avg_changes}")
print(f"Greatest Increase in Profits: {max_month} ${max_changes}")
print(f"Greatest Decrease in Profits: {min_month} ${min_changes}")


#hopefully text file
text_file=profit_csv.strip(".csv")+"_final.txt"
profit_csv=os.path.join(".",text_file)
with open(profit_csv, 'w')as text:
    text.write(f"Financial Analysis")
    text.write(f"----------------------------")
    text.write(f"Total Months: {total_months}")
    text.write(f"Total: ${total_profit}")
    text.write(f"Average  Change: ${avg_changes}")
    text.write(f"Greatest Increase in Profits: {max_month} ${max_changes}")
    text.write(f"Greatest Decrease in Profits: {min_month} ${min_changes}")
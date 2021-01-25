import pathlib
import csv
csvpath = pathlib.Path("budget_data.csv")
TotalNumber_months = 0
Total_PL = 0
monthly_changes= []
Previous_profitloss = 0
Max_increase = 0
Max_decrease = 0
max_decrease_month = 0
max_increase_month = 0
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        TotalNumber_months += 1
        profit = int(row[1])
        month = row[0]
        Total_PL +=profit
        change = profit- Previous_profitloss
        monthly_changes.append(change)
        Previous_profitloss = profit
        if change> Max_increase:
           Max_increase = change
           max_increase_month = month
        if change < Max_decrease:
            Max_decrease = change  
            max_decrease_month = month

    average_change = sum(monthly_changes[1:]) / len(monthly_changes[1:])          


    # Print Statements
    print("Financial Analysis")
    print("-------------------------------")
    print("Total Months: ", TotalNumber_months)
    print("Net Total: $", Total_PL)
    print("Average Change: $", average_change)
    print("Greatest Increase in Profits: ", max_increase_month, "($", Max_increase,")")
    print("Greatest Decrease in Profits: ", max_decrease_month, "($", Max_decrease,")")        
           


output_path = pathlib.Path("PyBank_output.txt")
    # Open the file with write mode
with open(file=output_path, mode='w', newline='') as txtfile:
        txtfile.write("Financial Analysis \n")
        txtfile.write("------------------- \n")
        txtfile.write(f"Total Months: {TotalNumber_months} \n")
        txtfile.write(f"Net Total: ${Total_PL} \n")
        txtfile.write(f"Average Change: $ {average_change:.3f}% \n")
        txtfile.write(f"Greatest Increase in Profits: {max_increase_month} ${Max_increase} \n")
        txtfile.write(f"Greatest Decrease in Profits: {max_increase_month} ${Max_decrease} \n")
        txtfile.close()           
import sys
import csv

#  Initialize all variables used below. Not needed for Python
#  but is a good practice

total_months = 0
total_pl = 0
change = 0
total_change = 0
avg_change = 0
prev_month_pl = 0
curr_month_pl = 0
gr_increase = 0
gr_decrease = 0
MONTH_COLUMN = 0
PL_COLUMN = 1

with open("budget_data.csv", 'r', encoding="utf8") as infile, \
     open("budget_analysis.txt", 'w', newline=None) as outfile:
       f_handle = [outfile, sys.stdout]
       reader = csv.reader(infile, delimiter=",")

       # Read the header row first (skip this step if there is no header)
       csv_header = next(reader)

       # Read the first data row to initialize with starting values
       row = next(reader)
       total_months = 1
       total_pl = int(row[PL_COLUMN])
       prev_month_pl = int(row[PL_COLUMN])
       for row in reader:
         # Do not process empty line in CSV file
         if row:
           total_months += 1

           # Debug print(row[0], row[1])
           curr_month_pl = int(row[PL_COLUMN])
           total_pl += curr_month_pl
           change = curr_month_pl - prev_month_pl
           total_change += change
           if (change > gr_increase):
             gr_increase = change
             gr_inc_month = row[MONTH_COLUMN]
           if (change < gr_decrease):
             gr_decrease = change
             gr_dec_month = row[MONTH_COLUMN]
           prev_month_pl = curr_month_pl
         # else:
           # print("Empty line")

       # Verify all these in Excel sheet

       # Avoid division by zero
       if total_months > 1:
         avg_change = total_change/(total_months - 1)

       for curr_file in f_handle:
         print("Financial Analysis", file=curr_file)
         print("---------------------------", file=curr_file)
         print(f"Total months: {total_months}", file=curr_file)
         print(f"Total: ${total_pl}", file=curr_file)
         print("Average Change : $%.2f" % avg_change, file=curr_file)
         print(f"Greatest Increase in Profits: {gr_inc_month} ${gr_increase}", file=curr_file)
         if (gr_decrease < 0):
           print(f"Greatest Decrease in Profits: {gr_dec_month} (${gr_decrease})", file=curr_file)
         else:
           print(f"Greatest Decrease in Profits: {gr_dec_month} ${gr_decrease}", file=curr_file)


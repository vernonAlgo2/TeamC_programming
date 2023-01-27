from pathlib import Path
import csv
# create a file to csv file
fp = Path.cwd()/"project_group"/"csv_reports"/"MAB CSV"/"45-overheads.csv"

# create an empty list to store overhead 
overhead_list = [] 
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    for expense, percentage in reader:
        # append the data directly to the overhead_list as a list
        overhead_list.append([expense, percentage])


# Assign the first category and percentage from the list as the initial highest
# Set as a reference point for the next elements in the list
highest_category = overhead_list[0][0]
highest_percentage = float(overhead_list[0][1])

for expense in overhead_list:
    # Check if the current expense's percentage is greater than the current highest percentage
    if float(expense[1]) > highest_percentage:
        # Update the highest category and highest percentage if the current expense's category and percentage is greater than the previous high
        highest_category = expense[0]
        highest_percentage = float(expense[1])

# create the summary_report text file
fp_cwd = Path.cwd()/"summary_report.txt"
fp_cwd.touch()
# opens the file to write the output
with fp_cwd.open(mode="w", encoding = "UTF-8", newline ="") as file:
    file.write(f"[HIGHEST OVERHEADS]{highest_category.upper()}: {highest_percentage}%\n")



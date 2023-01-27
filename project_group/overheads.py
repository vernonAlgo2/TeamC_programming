# Overheads
from pathlib import Path
import csv
# create a file to csv file
fp = Path.cwd()/"project_group"/"csv_reports"/"MAB CSV"/"45-overheads.csv"

# create an empty dictionary to store overhead 
overhead_list = [] 
# reads the csv file to append overhead the csv
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    for expense, percentage in reader:
        empty_dict = dict()
        empty_dict["Category"] = expense
        empty_dict["Overheads"] = percentage
        # append overhead as a dictionary back into the empty overhead_list dictionary 
        overhead_list.append(empty_dict)

# Assign the first category and percentage from the list as the initial highest
# Set as a reference point for the next elements in the list
highest_category = overhead_list[0]["Category"]
highest_percentage = float(overhead_list[0]["Overheads"])

for expense in overhead_list:
    # Check if the current expense's percentage is greater than the current highest percentage
    if float(expense["Overheads"]) > highest_percentage:
        # Update the highest category and highest percentage if the current expense's category and percentage is greater than the previous high
        highest_category = expense["Category"]
        highest_percentage = float(expense["Overheads"])

# create the summary_report text file
fp_cwd = Path.cwd()/"summary_report.txt"
fp_cwd.touch()
# opens the file to write the output
with fp_cwd.open(mode="w", encoding = "UTF-8", newline ="") as file:
    file.write(f"[HIGHEST OVERHEADS]{highest_category.upper()}: {highest_percentage}%\n")



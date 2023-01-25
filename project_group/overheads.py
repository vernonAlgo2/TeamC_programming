from pathlib import Path
import csv
fp = Path.cwd()/"project_group"/"csv_reports"/"MAB CSV"/"45-overheads.csv"

overhead_list = [] 
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    for expense, percentage in reader:
        empty_dict = dict()
        empty_dict["Category"] = expense
        empty_dict["Overheads"] = percentage
        overhead_list.append(empty_dict)


highest_category = overhead_list[0]["Category"]
highest_percentage = float(overhead_list[0]["Overheads"])
fp_cwd = Path.cwd()/"project_group"/"summary_report.txt"
fp_cwd.touch()
with fp_cwd.open(mode="w", encoding = "UTF-8", newline ="") as file:
    file.write(f"[HIGHEST OVERHEADS]{highest_category.upper()}: {highest_percentage}%\n")

#sort the data into descending and take the percentage at index 0
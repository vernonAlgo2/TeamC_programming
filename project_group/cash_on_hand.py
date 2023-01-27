from pathlib import Path
import csv
# create a file to csv file
fp = Path.cwd()/"project_group"/"csv_reports"/"cash_on_hand.csv"

# create an empty dictionary to store cash on hand by day 
cash_on_hand_list = []

# reads the csv file to append cash on hand from the csv
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    for day, coh in reader:
        empty_dict = dict()
        empty_dict["Day"] = day
        empty_dict["Cash On Hand"] = coh
        # append cash on hand as a dictionary back into the empty cash_on_hand_list dictionary 
        cash_on_hand_list.append(empty_dict)

# keeps track of the previous day's cash on hand
previous_day = cash_on_hand_list[0]["Day"]
previous_coh = float(cash_on_hand_list[0]["Cash On Hand"])

# create the summary_report text file
fp_cwd = Path.cwd()/"summary_report.txt"
fp_cwd.touch()
# opens the file to write the output
with fp_cwd.open(mode="a", encoding = "UTF-8", newline ="") as file:
    for index in range(1, len(cash_on_hand_list)):
        current_day = cash_on_hand_list[index]["Day"]
        current_coh = float(cash_on_hand_list[index]["Cash On Hand"])
        if current_coh < previous_coh:
            difference = previous_coh - current_coh
            file.write(f"[CASH DEFICIT] DAY: {current_day} , AMOUNT: USD{difference}\n")
        previous_day = current_day
        previous_coh = current_coh


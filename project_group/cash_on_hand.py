from pathlib import Path
import csv
fp = Path.cwd()/"project_group"/"csv_reports"/"cash_on_hand.csv"

cash_on_hand_list = []
# reads the csv file containing cash on hand from day 40 to 50
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    for day, coh in reader:
        empty_dict = dict()
        empty_dict["Day"] = day
        empty_dict["Cash On Hand"] = coh
        cash_on_hand_list.append(empty_dict)
# keeps track of the previous day's cash on hand
previous_day = cash_on_hand_list[0]["Day"]
previous_coh = float(cash_on_hand_list[0]["Cash On Hand"])

fp_cwd = Path.cwd()/"summary_report.txt"
fp_cwd.touch()
# writes cash defecits if any onto txt file
with fp_cwd.open(mode="a", encoding = "UTF-8", newline ="") as file:
    for i in range(1, len(cash_on_hand_list)):
        current_day = cash_on_hand_list[i]["Day"]
        current_coh = float(cash_on_hand_list[i]["Cash On Hand"])
        if current_coh < previous_coh:
            difference = previous_coh - current_coh
            file.write(f"[CASH DEFICIT] DAY: {current_day} , AMOUNT: USD{difference}\n")
        previous_day = current_day
        previous_coh = current_coh


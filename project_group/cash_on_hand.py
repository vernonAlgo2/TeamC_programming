from pathlib import Path
import csv
fp = Path.cwd()/"project_group"/"csv_reports"/"cash_on_hand.csv"

cash_on_hand_list = []

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    for day, coh in reader:
        empty_dict = dict()
        empty_dict["Day"] = day
        empty_dict["Cash On Hand"] = coh
        cash_on_hand_list.append(empty_dict)

previous_day = cash_on_hand_list[0]["Day"]
previous_coh = float(cash_on_hand_list[0]["Cash On Hand"])

fp_cwd = Path.cwd()/"project_group"/"test.txt"
fp_cwd.touch()

with fp_cwd.open(mode="w", encoding = "UTF-8", newline ="") as file:
    for i in range(1, len(cash_on_hand_list)):
        current_day = cash_on_hand_list[i]["Day"]
        current_coh = float(cash_on_hand_list[i]["Cash On Hand"])
        if current_coh < previous_coh:
            difference = previous_coh - current_coh
            file.write(f"[CASH DEFICIT] DAY: {current_day} , AMOUNT: USD{difference}\n")
        previous_day = current_day
        previous_coh = current_coh



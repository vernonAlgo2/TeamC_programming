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

fp_cwd = Path.cwd()/"project_group"/"test.csv"
fp_cwd.touch()

with fp_cwd.open(mode="w", encoding = "UTF-8", newline ="") as file:
    writer = csv.writer(file)
    writer.writerow(["Day", "Cash On Hand"])
    for item in cash_on_hand_list:
        writer.writerow([item["Day"], item["Cash On Hand"]])





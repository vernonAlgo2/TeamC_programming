from pathlib import Path
import csv
fp = Path.cwd()/"project_group"/"csv_reports"/"cash_on_hand.csv"

cash_on_hand = {}

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    
    previous_day = []
    previous_coh = []
    for row in reader:
        day = row[0]
        coh = float(row[1])


day_cluster, coh_cluster = [[day[0] for day in previous_day], [coh[1] for coh in previous_coh]]





from pathlib import Path
import csv
fp = Path.cwd()/"project_group"/"csv_reports"/"cash_on_hand.csv"

cash_on_hand = {}

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    
    day_cluster = []
    coh_cluster = []
    
    for row in reader:
        row[0] == "Day"
        day_cluster.append([row[0]])
        row[1] == "Cash On Hand (Accumulated) (USD)"
        coh_cluster.append([row[1]])

day_cluster, coh_cluster = [[day[0] for day in day_cluster], [coh[1] for coh in coh_cluster]]






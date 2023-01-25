from pathlib import Path
import csv
fp = Path.cwd()/"project_group"/"csv_reports"/"MAB CSV"/"profit-and-loss-usd.csv"
pnl_list = []
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    for day,sales,trading_profit, operating_expense, net_profit in reader:
        empty_dict = dict()
        empty_dict["Day"] = day
        empty_dict["Sales"] = sales
        empty_dict["Trading Profit"] = trading_profit
        empty_dict["Operating Expense"] = operating_expense
        empty_dict["Net Profit"] = net_profit
        pnl_list.append(empty_dict)

previous_day = pnl_list[0]["Day"]
previous_profit = float(pnl_list[0]["Net Profit"])

fp_cwd = Path.cwd()/"project_group"/"summary_report.txt"
fp_cwd.touch()
# writes cash defecits if any onto txt file
with fp_cwd.open(mode="a", encoding = "UTF-8", newline ="") as file:
    for i in range(1, len(pnl_list)):
        current_day = pnl_list[i]["Day"]
        current_profit = float(pnl_list[i]["Net Profit"])
        if current_profit < previous_profit:
            difference = previous_profit - current_profit
            file.write(f"[PROFIT DEFICIT] DAY: {current_day} , AMOUNT: USD{difference}\n")
        previous_day = current_day
        previous_profit = current_profit
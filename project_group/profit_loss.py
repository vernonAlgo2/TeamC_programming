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

fp_cwd = Path.cwd()/"summary_report.txt"
# writes cash defecits onto file
with fp_cwd.open(mode="a", encoding = "UTF-8", newline ="") as file:
    # Iterate through all elements in pnl_list starting from the second element
    # loop starts from the second element because the first element is being used as a reference point for comparison
    for index in range(1, len(pnl_list)):
        # Get current day and profit
        current_day = pnl_list[index]["Day"]
        current_profit = float(pnl_list[index]["Net Profit"])
        # Check if current profit is less than the previous profit
        if current_profit < previous_profit:
            # Calculate the difference between the current and previous profit
            defecit = previous_profit - current_profit
            file.write(f"[PROFIT DEFICIT] DAY: {current_day} , AMOUNT: USD{defecit}\n")
        # store current values to "previous_day" and "previous_coh" to be used as new reference point for next iteration
        previous_day = current_day
        previous_profit = current_profit
        
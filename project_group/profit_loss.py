from pathlib import Path
import csv
fp = Path.cwd()/"project_group"/"csv_reports"/"MAB CSV"/"profit-and-loss-usd.csv"

# create an empty list to store profit and loss by day
pnl_list = []
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    for day,sales,trading_profit, operating_expense, net_profit in reader:
        # append the data direct to the pnl_list as a list
        pnl_list.append([day, sales, trading_profit, operating_expense, net_profit])

previous_day = pnl_list[0][0]
previous_profit = float(pnl_list[0][4])

fp_cwd = Path.cwd()/"summary_report.txt"
# writes cash defecits onto file
with fp_cwd.open(mode="a", encoding = "UTF-8", newline ="") as file:
    # Iterate through all elements in pnl_list starting from the second element
    # loop starts from the second element because the first element is being used as a reference point for comparison
    for index in range(1, len(pnl_list)):
        # Get current day and profit
        current_day = pnl_list[index][0]
        current_profit = float(pnl_list[index][4])
        # Check if current profit is less than the previous profit
        if current_profit < previous_profit:
            # Calculate the difference between the current and previous profit
            defecit = previous_profit - current_profit
            file.write(f"[PROFIT DEFICIT] DAY: {current_day} , AMOUNT: USD{defecit}\n")
        # store current values to "previous_day" and "previous_coh" to be used as new reference point for next iteration
        previous_day = current_day
        previous_profit = current_profit
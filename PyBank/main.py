import os
import csv

csv_path = os.path.join("Resources", "budget_data.csv")
output_path = os.path.join("analysis", "analysis.txt")

total_months = 0
total = 0
average_change = 0
profits_inc_date = ""
profits_inc = 0
profits_dec_date = ""
profits_dec = 0

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    average_list = []
    month_list = []
    month = ""
    monthly_change = 0
    previous = 1088983

    for row in csvreader:
        total_months += 1
        total += int(row[1])

        current = int(row[1])
        monthly_change = current - previous
        average_list.append(monthly_change)
        month = row[0]
        month_list.append(month)
        previous = current

    average_dict = {average_list[i]: month_list[i] for i in range(len(month_list))}

    for average in average_list:
        average_change += average

    average_change = round(average_change / (len(average_list) - 1), 2)

    profits_inc = max(average_dict)
    profits_inc_date = average_dict[profits_inc]
    profits_dec = min(average_dict)
    profits_dec_date = average_dict[profits_dec]

with open(output_path, "w") as output:
    txt_title = "Financial Analysis"
    txt_line = "----------------------------"
    txt_total_months = f"Total Months: {total_months}"
    txt_total = f"Total: ${total}"
    txt_average_change = f"Average Change: ${average_change}"
    txt_profits_inc = (
        f"Greatest Increase in Profits: {profits_inc_date} (${profits_inc})"
    )
    txt_profits_dec = (
        f"Greatest Decrease in Profits: {profits_dec_date} (${profits_dec})"
    )

    final_output = (
        txt_title
        + "\n"
        + txt_line
        + "\n"
        + txt_total_months
        + "\n"
        + txt_total
        + "\n"
        + txt_average_change
        + "\n"
        + txt_profits_inc
        + "\n"
        + txt_profits_dec
    )

    print(final_output)
    output.write(final_output)

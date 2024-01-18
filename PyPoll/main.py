import os
import csv

csv_path = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("analysis", "analysis.txt")

total_votes = 0
c1_votes = 0
c1_percent = 0
c2_votes = 0
c2_percent = 0
c3_votes = 0
c3_percent = 0
winner = ""

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        if row[2] == "Charles Casper Stockham":
            c1_votes += 1
        elif row[2] == "Diana DeGette":
            c2_votes += 1
        else:
            c3_votes += 1

    c1_percent = round((c1_votes / total_votes) * 100, 3)
    c2_percent = round((c2_votes / total_votes) * 100, 3)
    c3_percent = round((c3_votes / total_votes) * 100, 3)

    if max(c1_votes, c2_votes, c3_votes) == c1_votes:
        winner = "Charles Casper Stockham"
    elif max(c1_votes, c2_votes, c3_votes) == c2_votes:
        winner = "Diana DeGette"
    else:
        winner = "Raymon Anthony Doane"

with open(output_path, "w") as output:
    txt_title = "Election Results"
    txt_line = "----------------------------"
    txt_total_votes = f"Total Votes: {total_votes}"
    txt_c1_votes = f"Charles Casper Stockham: {c1_percent}% ({c1_votes})"
    txt_c2_votes = f"Diana DeGette: {c2_percent}% ({c2_votes})"
    txt_c3_votes = f"Raymon Anthony Doane: {c3_percent}% ({c3_votes})"
    txt_winner = f"Winner: {winner}"

    final_output = (
        txt_title
        + "\n"
        + txt_line
        + "\n"
        + txt_total_votes
        + "\n"
        + txt_line
        + "\n"
        + txt_c1_votes
        + "\n"
        + txt_c2_votes
        + "\n"
        + txt_c3_votes
        + "\n"
        + txt_line
        + "\n"
        + txt_winner
        + "\n"
        + txt_line
    )

    print(final_output)
    output.write(final_output)

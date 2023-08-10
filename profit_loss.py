import csv

def find_profit_changes(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        previous_day = None
        previous_net_profit = None
        highest_increment_day = None
        highest_increment_amount = 0

        for row in reader:
            day = int(row['Day'])
            net_profit = float(row['Net Profit'])

            if previous_day is not None:
                if net_profit < previous_net_profit:
                    # Compute the difference in net profit
                    difference = previous_net_profit - net_profit
                    print(f"Day {day}: Decrease in Net Profit by {difference:.2f}")
                elif net_profit > previous_net_profit:
                    # Check for the highest increment in net profit
                    increment = net_profit - previous_net_profit
                    if increment > highest_increment_amount:
                        highest_increment_day = day
                        highest_increment_amount = increment

            # Update previous_day and previous_net_profit
            previous_day = day
            previous_net_profit = net_profit

        if highest_increment_day is not None:
            print(f"Highest increment occurred on Day {highest_increment_day} with an amount of {highest_increment_amount:.2f}")
        else:
            print("No increasing trend found in Net Profit.")

# Provide the CSV file path here
csv_filename = 'profit_loss.csv'
find_profit_changes(csv_filename)
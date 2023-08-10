import csv

data_list = []
with open('profit_loss.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        data_list.append(row)

# Process the data
for row in data_list:
    print(row)


highest_diff_day = 0
highest_diff = 0

# Open the CSV file
with open('profit_loss.csv', 'r') as file:
    reader = csv.DictReader(file)

    # declaring variables
    previous_day = 0
    previous_day_coh = 0

    # define over each row in the CSV file
    for row in reader:
        current_day = int(row['Day'])
        coh = int(row['Cash On Hand'])

        if previous_day < current_day:
            increment = coh - previous_day_coh

            # Update the highest increment
            if increment > highest_diff:
                highest_diff = increment
                highest_diff_day = current_day
            
        # Update previous day's data
        previous_day = current_day
        previous_day_coh = coh

if highest_diff_day is not None:
    print(f"Highest increment occurred on Day {highest_diff_day} with an amount of {highest_diff:.2f}")
else:
    print("No increment found")






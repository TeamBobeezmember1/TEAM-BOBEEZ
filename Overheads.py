import csv

# Define a dictionary to store the total value for each overhead
overhead_totals = {}

# Read the CSV file
with open('Overheads.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        overhead = row['Category']
        value = abs(float(row['Overheads']))

        # Find total value for each overhead
        if overhead in overhead_totals:
            overhead_totals[overhead] += value
        else:
            overhead_totals[overhead] = value

# Determine highest overhead
highest_overhead = max(overhead_totals, key=overhead_totals.get)
highest_value = overhead_totals[highest_overhead]

# Print the total value for each overhead
for overhead, total_value in overhead_totals.items():
    print(f"Total value for {overhead}: {total_value}")

# Print the highest value and corresponding overhead
print(f"Highest overhead is {highest_overhead}: {highest_value}")
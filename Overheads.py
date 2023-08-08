import csv

# Define variables to track highest value and corresponding overhead
highest_value = float('-inf')
highest_overhead = None

# Define a dictionary to store the total value for each overhead
overhead_totals = {}

# Read the CSV file
with open('Operating expense.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        overhead = row['Items ']
        value = abs(float(row['Amount ']))

        # Define the overheads
        keywords = ['Expense']

        # Check if the item is an expense
        contains_expense = any(keyword in overhead for keyword in keywords)
        if not contains_expense:
            # Skips items that are not expenses
            continue 

        # Find total value for each overhead

        if overhead in overhead_totals:
            overhead_totals[overhead] += (value)
        else:
            overhead_totals[overhead] = (value)

        # Determine highest overhead
        if float(value) > highest_value:
            highest_value = (value)
            highest_overhead = overhead
    
# Print the total value for each overhead
for overhead, total_value in overhead_totals.items():
    print(f"Total value for {overhead}: {total_value}")

# Print the highest value and corresponding overhead
print(f"Highest overhead is {highest_overhead}: {highest_value}")
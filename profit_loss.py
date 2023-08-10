import csv

# Main function to calculate cash deficits
def cash_on_hand_function():
    cash_data = []  # Fix: Initialize as an empty list
    COH_final = 0 
    
    # Open the CSV file containing cash-on-hand data
    with open('COH_final.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cash_data.append(row)  # Fix: Append rows to cash_data

    # Compute the differences in cash on hand between consecutive days
    cash_differences = compute_cash_difference(cash_data)  # Fix: Use single equal sign
    
    # Filter and collect days with cash deficits (amount > 0)
    cash_deficits = [(day, amount) for day, amount in cash_differences if amount > 0]
    print(cash_deficits)

# Calculate the differences in cash on hand between consecutive days
def compute_cash_difference(data):
    differences = []
    for i in range(1, len(data)):
        current_cash = int(data[i]['Cash On Hand'])
        previous_cash = int(data[i - 1]['Cash On Hand'])
        difference = previous_cash - current_cash
        differences.append((i, difference))  # Store the day index and cash difference
    return differences

# Call the main function
cash_on_hand_function()






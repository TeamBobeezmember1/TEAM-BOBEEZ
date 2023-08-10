import csv

# Main function to calculate profit deficits
def net_profit_function():
    net_profit_data = []  # Fix: Initialize as an empty list
    profit_loss_final = 0 
    
    # Open the CSV file containing profit and loss data
    with open('profit_loss.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            net_profit_data.append(row)  # Fix: Append rows to net_profit_data

    # Compute the differences in net profit between consecutive days
    net_profit_differences = compute_net_profit_difference(net_profit_data)  # Fix: Use single equal sign
    
    # Filter and collect days with profit deficits (amount > 0)
    profit_deficits = [(day, amount) for day, amount in net_profit_differences if amount > 0]
    print(profit_deficits)

# Calculate the differences in net profit between consecutive days
def compute_net_profit_difference(data):
    differences = []
    for i in range(1, len(data)):
        current_net_profit = int(data[i]['Net Profit'])
        previous_net_profit = int(data[i - 1]['Net Profit'])
        difference = previous_net_profit - current_net_profit
        differences.append((i, difference))  # Store the day index and net profit difference
    return differences

# Call the main function
net_profit_function()






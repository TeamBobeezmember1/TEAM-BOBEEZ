import csv

# Define variables to track the highest increment
max_increment_day = 0
max_increment_amount = 0

# Open the CSV file
with open('COH.final.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    # Initialize variables for previous day's data
    prev_day = 0
    prev_coh = 0

# define over each row in the CSV file
    for row in reader:
        current_day = int(row['Day'])
        coh = int(row['Cash On Hand'])
        
        # Calculate the increment if the current day is lower than the previous day
        if prev_day is not None and current_day < prev_day:
            increment = prev_coh - coh
            
            # Update the highest increment
            if increment > max_increment_amount:
                max_increment_amount = increment
                max_increment_day = current_day
        
        # Update previous day's data
        prev_day = current_day
        prev_coh = coh

if max_increment_day is not None:
    print(f"Highest increment occurred on Day {max_increment_day} with an amount of {max_increment_amount:.2f}")
else:
    print("No increment found")























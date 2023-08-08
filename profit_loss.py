"[NET PROGIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY"

import csv

data_list = []
with open('profit_loss.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        data_list.append(row)

# Process the data
for row in data_list:
    print(row)







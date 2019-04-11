import os
import csv

filepath = os.path.join('Resources', 'budget_data.csv')

with open(filepath, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(reader)

    date = []
    profit = []
    change =[]
    lastrow = 0

    for row in reader:
        date.append(row[0])
        profit.append(row[1])
        
        diff = int(row[1]) - int(lastrow)
        lastrow = row[1]
        change.append(diff)

zip_values = zip(date, change)
zip_list = list(zip_values)
change.remove(change[0])
zip_list.remove(zip_list[0])

total_months = len(date)
total = sum(map(int, profit))
average_change = sum(change) / len(change)
increase = max(change)
decrease = min(change)

max_change = 0
min_change = 0

for row in zip_list:
    if row[1] == increase:
        max_change = row[0]
    if row[1] == decrease:
        min_change = row[0]

print(f'Financial Analysis')
print(f'----------------------------')
print(f'Total Months: {total_months}')
print(f'Net Total Profit: ${total}')
print(f'Average Change in Value: ${average_change:.2f}')
print(f'Greatest Profit Value: {max_change} (${increase})')
print(f'Greatest Loss Value: {min_change} (${decrease})')

with open('Financial_Analysis.txt', 'w') as text_file:
    print(f'Financial Analysis', file=text_file)
    print(f'----------------------------', file=text_file)
    print(f'Total Months: {total_months}', file=text_file)
    print(f'Net Total Profit: ${total}', file=text_file)
    print(f'Average Change in Value: ${average_change:.2f}', file=text_file)
    print(f'Greatest Profit Value: {max_change} (${increase})', file=text_file)
    print(f'Greatest Loss Value: {min_change} (${decrease})', file=text_file)
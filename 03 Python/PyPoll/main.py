import os
import csv

filepath = os.path.join('Resources', 'election_data.csv')

with open(filepath, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    csv_header = next(reader)

    candidates = []

    for row in reader:
        candidates.append(row[2])

    candidate_count = [[x,candidates.count(x)] for x in set(candidates)]
    
    votes = []
    name = []
    
    for row in candidate_count:
        name.append(row[0])
        votes.append(row[1])

    candidates_zip = zip(name, votes)
    candidates_list = list(candidates_zip)

    winner = max(votes)

    for row in candidates_list:
        if row[1] == winner:
            winner_name = row[0]       
            
total_votes = len(candidates)

khan_total = candidates.count('Khan')
khan_percent = khan_total / total_votes

correy_total = candidates.count('Correy')
correy_percent = int(correy_total) / int(total_votes)

li_total = candidates.count('Li')
li_percent = li_total / total_votes

o_tooley_total = candidates.count("O'Tooley")
o_tooley_percent = o_tooley_total / total_votes

print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------')
print(f'Khan: {khan_percent:.3%} ({khan_total})')
print(f'Correy: {correy_percent:.3%} ({correy_total})')
print(f'Li: {li_percent:.3%} ({li_total})')
print(f"O'Tooley: {o_tooley_percent:.3%} ({o_tooley_total})")
print(f'-------------------------')
print(f'Winner: {winner_name}')
print(f'-------------------------')

with open('Election_Results.txt', 'w') as text_file:
    print(f'Election Results', file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Total Votes: {total_votes}', file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Khan: {khan_percent:.3%} ({khan_total})', file=text_file)
    print(f'Correy: {correy_percent:.3%} ({correy_total})', file=text_file)
    print(f'Li: {li_percent:.3%} ({li_total})', file=text_file)
    print(f"O'Tooley: {o_tooley_percent:.3%} ({o_tooley_total})", file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Winner: {winner_name}', file=text_file)
    print(f'-------------------------', file=text_file)
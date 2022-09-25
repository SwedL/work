
import csv

with open('D:/student_counts.csv', 'r', encoding='utf-8') as inp_data:
    data = list(csv.DictReader(inp_data))
    header = [k for k in data[0].keys()]

    for line in data:
        print(line)
    print(header)





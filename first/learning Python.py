
import csv

with open('D:/deniro.csv', 'r', encoding='utf-8') as file:
    data = csv.reader(file)
    column = int(input())-1
    list1 = sorted(data, key=lambda item: int(item[column]) if column else item[column])
    for row in list1:
        print(','.join(row))

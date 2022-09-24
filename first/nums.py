
import csv


def csv_columns(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        category_dict = {}
        data = csv.DictReader(file)
        for line in data:
            for item in line:
                category_dict[item] = category_dict.get(item, []) + [line[item]]
        return category_dict



print(csv_columns('D:/1.csv'))

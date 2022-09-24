
import csv


with open('D:/data.csv', 'r', encoding='utf-8') as inp_data:
    data = csv.DictReader(inp_data)
    domain_dict = {}
    for line in data:
        domain_dict[line['email'][line['email'].find('@')+1:]] = domain_dict.get(line['email'][line['email'].find('@')+1:], 0) + 1
    domain_list = [[domain, count] for domain, count in domain_dict.items()]
    domain_list.sort(key=lambda item: item[1])
    print(domain_list)

    columns = ['domain', 'count']
    with open('D:/domain_usage.csv', 'w', encoding='utf-8') as out_data:
        writer = csv.writer(out_data)
        writer.writerow(columns)
        writer.writerows(domain_list)





import json



with open('D:/food_services.json', 'r', encoding='utf-8') as inp_file:
    data = list(json.load(inp_file))
    print(*data[0:15], sep='\n')





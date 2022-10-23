
from collections import ChainMap, Counter


bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}
menu = ChainMap(bread, meat, sauce, vegetables, toppings)


zakaz = input().split(',')
counter = Counter(zakaz)

indent = max(map(len, zakaz))
indent_minus = indent+3+len(str(max(counter.values())))
print(indent_minus)

total = sum([menu[i]*counter[i] for i in counter])
print(sorted(counter.most_common(), key=lambda x: x[0]))

print(total)


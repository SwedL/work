from collections import OrderedDict

def custom_sort(ordered_dict, by_values=False):
    key_res = []
    key_res = [sorted(ordered_dict, key=lambda ord: ord[0]), sorted(ordered_dict, key=lambda ord: ord[1])][by_values]
    print(key_res)
    for i in key_res:
        ordered_dict.move_to_end(i)

data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
print(data)
custom_sort(data, by_values=True)
print(data)

# data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
# print(data)
# custom_sort(data, by_values=True)
#
# print(*data.items())




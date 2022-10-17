from collections import OrderedDict


def custom_sort(ord_dict, by_values=False):
    key_res = [sorted(ord_dict), sorted(ord_dict, key=lambda values: ord_dict[values])][by_values]
    [ord_dict.move_to_end(i) for i in key_res]


# data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
# print(data)
# custom_sort(data, by_values=True)
# print(data)

data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
print(data)
custom_sort(data, by_values=False)

print(*data.items())




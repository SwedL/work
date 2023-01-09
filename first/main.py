from itertools import permutations


all_num_permutations = all(map(lambda x: (x[0] + x[1]) > x[2], permutations([self.a, self.b, self.c])))
print(list(all_num_permutations))




# res, n = input(), ''
#
# while n != res:
#     n = res
#     res = re.sub(r'\b(\w{2,})\W*\s*\1\b', r'\1', res)
#
#
# print(res)

from itertools import combinations


wallet = [100, 50, 20, 10, 5]
print(wallet*20)
list_res = []

for i in range(1, 21):
    list_res.append(len([k for k in set(combinations(wallet*20, i)) if sum(k) == 100]))
print(sum(list_res))





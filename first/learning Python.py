




def primes(left, right):
    list_res = iter(range((left, left+1)[left == 1], right+1))
    next_simply_number = 2

    for i in list_res:
        yield i




generator = primes(1, 15)
print(*generator)

# for num in list_res:
#     d, count = 2, 0
#     while d < num and count == 0:
#         if num % d == 0:
#             count = 1
#         d += 1
#     if count == 0:
#         next_simply_number.append(num)
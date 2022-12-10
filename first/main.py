






def ranges(numbers):
    list1, list_temp, a = [], [], numbers[0]
    for i in range(len(numbers)):
        if a + 1 == numbers[i] or a == numbers[i]:
            list_temp.append(numbers[i])
        else:
            list1.append(list_temp)
            list_temp = [numbers[i]]
        a = numbers[i]
    list1.append(list_temp)
    return list(map(lambda x: (min(x), max(x)), list1))


numbers = [1, 2, 3, 4, 7, 8, 10]
print(ranges(numbers))

numbers = [1, 3, 5, 7]
print(ranges(numbers))

numbers = [1, 2, 3, 4, 5, 6, 7]
print(ranges(numbers))


def func(lst, operation):
    newLst = []
    for i in lst:
        newLst.append(operation(i))
    return newLst

print(func([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], lambda i: i ** 2))
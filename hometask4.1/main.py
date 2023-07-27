lst = [45, 67, 23, 45, 111, 67, 12, 55]
lst2 = []
for x in lst:
    if x not in lst2:
        lst2.append(x)
        lst = lst2
print(lst)

mylist = []
mylist.extend(range(1, 100))
mylist = ["fizzbuzz" if num % 5 == 0 and num % 3 == 0 else "fizz" if num % 3 == 0 else "buzz" if num % 5 == 0 else num for num in mylist]
for element in mylist:
    if element == "fizz":
        print(element)
    elif element == "buzz":
        print(element)
    elif element == "fizzbuzz":
        print(element)
    else:
        print(element)

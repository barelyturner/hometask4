import random
num = random.randrange(1, 10)
usernum = int(input("I bet you won't guess the number from 1 to 10: "))
while num != usernum:
    if usernum < num:
        print(f'X is > than {usernum}')
        usernum = int(input("Try again: "))
    elif usernum > num:
        print(f'X is < than {usernum}')
        usernum = int(input("Try again: "))
print("woohoo!")

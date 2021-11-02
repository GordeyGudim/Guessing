import random
n = int(input())
i = random.choice(range(1, 101))
while n != i:
    if n > i:
        print('Your number is greater')
    if n < i:
        print('Your number is less')
    n = int(input())
if n == i:
    print('You win!')
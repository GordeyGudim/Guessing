import random
n = int(input())
i = random.choice(range(1, 101))
while n != i:
    if n > i:
        print('Ваше число больше')
    if n < i:
        print('Ваше число меньше')
    n = int(input())
if n == i:
    print('Вы победили')
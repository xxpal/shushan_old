import random

random_num = random.randint(1, 5)
# random_num = 5
ongoing = True
count = 0

while ongoing:
    input_num = int(input('Please input your guessing number:'))
    count += 1
    if input_num == random_num:
        print('Bingo! You got it!')
        ongoing = False
        break
    elif input_num > random_num:
        print('Your input number is greater, please try again!')
        continue
    else:
        print('Your input number is less, please try again!')
        continue

print('You totally tried {} times.'.format(count))

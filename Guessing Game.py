## Problem 2
import random

print('Think of a number between 0 and 100')

min = 0
max = 100
guess = None
count = 1

inGame = True
while inGame:
    number = random.randint(min, max)
    guess = input('Is your number ' + str(number) + ' (H/L/Yes): ')

    if (guess == 'H'):
        max = number - 1
        count = count + 1
    elif (guess == 'L'):
        min = number + 1
        count = count + 1
    else:
        print('Game Over! Your number is {}'.format(number))
        print('No. of Attempts: {}'.format(count))
        inGame = False
        
        again = input('Would you like to play Again? ' + '(Yes/No): ')
        if (again == 'Yes'):
            inGame = True
        else:
            print('Thank You for Playing')
            inGame = False
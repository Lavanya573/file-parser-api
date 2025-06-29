# To generate random number
import random

#random integer
number = random.randint(1,10)

#while Loop
while True:
    num = int(input("Guess a Number between 1-10 : "))


    if num == number:
        print('Correct, you guessed it!')
        break
    elif num < number:
        print('Too low')

    else:
        print('Too high')


import random
run = True
n = 0
rand = random.randint(1,10)

while run:
    print("you have 5 trails only ")
    while n < 5:
        user_input = int(input('Enter Numberin range[1,10]: '))
        if user_input == rand:
            print('You won!')
            break
        elif user_input > rand:
            print('your number is big')
        elif user_input < rand:
            print('your number is small')
        n+=1

    if n == 5:
        print("you loss!")
    c = input("want to continue enter y/n: ")
    rand = random.randint(1,10)
    if c == "n":
        run = False
    n = 0
    


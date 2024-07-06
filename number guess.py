import random

num = input('Type a number : \n')

if num.isdigit():
    num = int(num)
    if num <= 0:
        print('Type a number larger than 0 next time!')
        quit()

    random_number = random.randint(0, num)  # Corrected randint usage

    while True:
        guess = input('Guess a number :\n')
        if guess.isdigit():
            guess = int(guess)
        
            if guess < 0 or guess > num:
                print('Try again ')
                continue

            if guess < random_number:
                print('Guess higher!')
            elif guess > random_number:
                print('Guess lower!')
            else:
                print('Congratulations! You guessed the correct number:', random_number)
                break
        else:
            print('Enter a valid number.')

else:
    print('Try again!')
    quit()

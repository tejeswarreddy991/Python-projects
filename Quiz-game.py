print('Welcome to my computer quiz!')

playing = input('Do you want to play? (yes/no): ')

if playing.lower() != 'yes':
    quit()

print('Okay! Let\'s play.')

score = 0  # Initialize score counter

# Question 1
answer = input('What does CPU stand for? ')
if answer.lower() == 'central processing unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    
# Question 2
answer = input('What does ROM stand for? ')
if answer.lower() == 'read only memory':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

# Question 3
answer = input('What does RAM stand for? ')
if answer.lower() == 'random access memory':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

# Question 4
answer = input('What does GPU stand for? ')
if answer.lower() == 'graphics processing unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print(f'You got {score} out of 4 questions correct.')

# Optionally, you can provide a closing message based on the score
if score == 4:
    print('Congratulations! You are a computer whiz!')
elif score >= 2:
    print('Well done!')
else:
    print('You might want to brush up on your computer knowledge.')

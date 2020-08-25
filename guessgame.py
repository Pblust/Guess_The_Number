import random
guesstaken = 0
print('Hello! What is your name?')
name = input()
number = random.randint(1,20)
print(f'Well, {name.title()}, I am thinking of a number between 1 and 20')
for guess in range(1,20):
    print('Take a guess: ')
    guess= input()
    guess = int(guess)
    
    
    if guess < number:
        print('Your guess is to low. Try again')
    if guess > number:
        print('Your guess is to high. Try again')
    if guess == number:
        break
if guess == number:
    guess = str(guess+1)
    print(f'Good Job {name.title()}!')

if guess != number:
    number =str(number)
    print(f'The number I was thinking of was {number}')

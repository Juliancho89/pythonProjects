import random

options = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissors'
}

user_wins = 0
computer_wins = 0

while user_wins < 2 and computer_wins < 2:
    print('\n' * 3)
    print('*' * 50)
    print('*            ROCK-PAPER-SCISSORS GAME            *')
    print('*' * 50)
    
    print('\nSelect the letter you want to play:')
    for element in options:
        print(f"{element}: {options[element]}")
    user_option = input('Your choise -> ')
    
    if not user_option in options:
        print(f'Select again!\n   There is not "{user_option}" into playable options!')
        continue
    
    computer_option = random.choice(tuple(options.keys()))
    
    if user_option == computer_option:
        print('Draw!')
    elif user_option == 'r':
        if computer_option == 'p':
            print('Computer wins')
            computer_wins += 1
        else:
            print('You win')
            user_wins += 1
    elif user_option == 'p':
        if computer_option == 's':
            print('Computer wins')
            computer_wins += 1
        else:
            print('You win')
            user_wins += 1
    else:
        if computer_option == 'r':
            print('Computer wins')
            computer_wins += 1
        else:
            print('You win')
            user_wins += 1
    
    print(f'\n\t\tYou:\t|Computer:')
    print(f'wins:\t\t   {user_wins}\t|   {computer_wins}')
    print(f'selection:\t   {user_option}\t|   {computer_option}')

print('\n')
print('º' * 50)
if computer_wins == 2:
    print('º         Computer Has Won The Game              º')
    print('º         Better luck for the next time          º')
else:
    print('º     Congratulations! You Have Won The Game     º')
    print('º     Find the awards on Platzi.com              º')
print('º' * 50)
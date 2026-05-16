import random as r

def game_logic():
    num = r.randint(1,100)
    print('<<<<<<<<<<<<<<<<<<<<< Welcome to the Number guessing game! >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('Try to guess the number...\nHint - The  number is between 1 to 100')

    d = {'Easy':20,'Moderate':10,'Hard':5,'Very Hard':3, 'Extreme':2}
    print('Levels')
    for i in d:
        print(f'{i}---{d[i]}')

    level = input('Enter the level: ')
    num1 = int(input('Enter the guessed number: '))
    maxtry = d[level.capitalize()]

    tries = 1

    while num != num1 and tries <= maxtry:
        print('Wrong Choice')
        if num1>num:
            print('Hint - The number is smaller...')
        elif num1<num:
            print('Hint - The number is bigger...')
        print('Try again...')
        choice = input('Do you want to continue?(y/n): ')
        if choice.lower() == 'y':
            num1 = int(input('Enter the guessed number: '))
            tries += 1
        elif choice.lower() == 'n':
            print('Ok... come again!')
            break

    if num == num1:
        print(f'You guessed it right in {tries} times!')
    else:
        print('You are defeated!')

game_logic()

choice = input('Do you want to play the game again?(y/n): ')

if choice.lower() == 'y':
    game_logic()
else:
    print('Thankyou for playing the game')
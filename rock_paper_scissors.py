import random

print('\n      WIN RULE \n 1. Paper beats Rock. \n 2. Rock beats Scissors. \n 3. Scissors beats Paper')

while True:

    user_choice = int(input('\n      User Choice \n 1. Rock \n 2. Paper \n 3. Scissors \n ----->'))
    while user_choice > 3 or user_choice  < 1:
        user_choice = int(input('please enter valid choice:  '))

    if user_choice == 1:
        user_choice_name = 'rock'
    elif user_choice == 2:
        user_choice_name = 'paper'
    else:
        user_choice_name = 'scissors'
    print('\n     User Choice     ')
    print(f'======={user_choice_name}=======')

    print('\n------Now Computer------')
    computr_choice =  random.randint(1,3)
    if computr_choice == 1:
        computr_choice_name = 'rock'
    elif  computr_choice == 2:
        computr_choice_name = 'paper'
    else:
        computr_choice_name = 'scissors'

    print('\n     Comp Choice     ')
    print(f'======={computr_choice_name}=======')


    if user_choice == computr_choice:
        print('\n----------Tie----------')

    if user_choice == 1 and computr_choice == 2:
        print('\n     Paper beats Rock')
        print('         Computer Win')
    elif user_choice == 2 and computr_choice == 1:
        print('\n     Paper beats Rock')
        print('         User Win')
    elif user_choice  == 2 and computr_choice == 3:
        print('\n     Scissors beats Paper')
        print('         computer Win')
    elif user_choice == 3 and computr_choice == 2:
        print('\n     Scissors beats Paper')
        print('         User Win')
    elif user_choice == 3 and computr_choice == 1:
        print('\n     Rock beats Scissors')
        print('         computer win')
    elif user_choice == 1 and computr_choice == 3:
        print('\n     Rock beats Scissors')
        print('         user win')   
    print('Do you want to play again(Y/N)')
    play = input('==>').lower()
    if play == 'n':
        break

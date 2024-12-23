from random import choice
"""
A computer chooses between the rock, paper and scissors and compare it to your input.
rules 
paper beats rock
rock beats scissors
scissors beats paper
"""
options = ('rock','paper','scissors')
def paper_rock(user_input, computer_option):
    if user_input == 'paper' and computer_option == 'rock':
        return f'{user_input} beats {computer_option} so User win'
    elif computer_option == 'paper' and  user_input == 'rock':
        return f'{computer_option} beats {user_input} so Computer win'

    return
def rock_scissors(user_input, computer_option):
    if user_input == 'rock' and computer_option == 'scissors':
        return f'{user_input} beats {computer_option} so User win'
    elif computer_option == 'rock' and  user_input == 'scissors':
        return f'{computer_option} beats {user_input} so Computer win'
    return

def scissors_paper(user_input, computer_option):
    if user_input == 'scissors' and computer_option == 'paper':
        return f'{user_input} beats {computer_option} so User win'
    elif computer_option == 'scissors' and  user_input == 'paper':
        return f'{computer_option} beats {user_input} so Computer win'
    return

if __name__ == '__main__':
    attempt = 0
    while attempt < 3:
        attempt += 1
        user_input = str(input('Choose one ("rock","paper","scissors") >> ')).lower()
        computer_option = choice(options)

        if user_input == computer_option:
            print(f'This is a Tie you both chose {computer_option}')
            attempt = 0
        else:
            result = paper_rock(user_input, computer_option) or rock_scissors(user_input, computer_option) or scissors_paper(user_input, computer_option)
            if not result:
                print('Error Try again ')
            else:
                print(result)

    else:
        print('Ended .')
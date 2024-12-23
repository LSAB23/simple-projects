from random import choice

# This is a random number number genrator where you provide 


break_point :int= int(input('How many tries you want (default = 5)>> ')) or 5
times_guessed :int= 1


range_to_guess :str= input('number range with comma : ')

first_number, *second_number = range_to_guess.replace(',', '')
second_number = ''.join(_ for _ in second_number)

guess :int = int(input('Enter a guess >> '))
random_genrator :int= choice([_ for _ in range(int(first_number) ,int(second_number))])

while times_guessed < int(break_point):
    if guess == random_genrator:
        print('You guessed right')
        break
    else:
        print('Wrong guess')
        times_guessed += 1
        guess :int= int(input('Try again >> '))
else:
    print('You guessed worng')

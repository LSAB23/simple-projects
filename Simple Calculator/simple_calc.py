# Simple calculator +,-,/ and *
# noinspection PyShadowingNames

while True:
    user_input :str = input('What to calculate >> ')
    if '+' in user_input:
        numbers :list= user_input.split('+')
        num1 :int= int(numbers[0])
        num2 :int= int(numbers[1])
        print(num1+num2)
        continue
    if '-' in user_input:
        numbers :list= user_input.split('-')
        num1 :int= int(numbers[0])
        num2 :int= int(numbers[1])
        print(num1 - num2)
        continue

    if '*' in user_input:
        numbers :list= user_input.split('*')
        num1 :int= int(numbers[0])
        num2 :int= int(numbers[1])
        print(num1*num2)
        continue

    if '/' in user_input:
        numbers :list= user_input.split('/')
        num1 :int= int(numbers[0])
        num2 :int= int(numbers[1])
        print(num1/num2)
        continue

    if user_input.lower() == 'quit' or 'q':
        break
    else:
        print('try again or type q or quit to quit its not case sensitive')

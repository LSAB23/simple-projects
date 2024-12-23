"""
A calculator cli that add, subtract,multiply and divide multiple numbers
"""

def add(lst :list) -> int:
    result :int = 0
    for num in lst:
        result += int(num)
    return result

def minus(lst :list) -> int:
    result :int = 0
    for num in lst:
        result -= int(num)
    return result

def multiply(lst :list) -> int:
    result :int= 0
    for num in lst:
        result *= int(num)
    return result


def divide(lst :list) -> int|float:
    result :int|float= 0
    for num in lst:
        result /= int(num)
    return result


while True:

    operation :str= input('operation or type help >> ')
    operation = operation.lower()
    if operation == 'q':
        break
    if operation == 'help':
        print('''
    -- Enter q or Q to quit in the operations input
    -- + or add to add
    -- - or minus to subtract
    -- * or times to multiply
    -- / to divide
    -- help to see this again in the operations input
    ''')
        continue
    lst_numbers :list= str(input('Enter num with , inbetween >> ')).split(',')

    if operation == '+' or 'add':
        answer :int = add(lst_numbers)
        print(f'Answer: {answer}')
        continue

    if operation == '-' or minus:
        answer :int = minus(lst_numbers)
        print(f'Answer: {answer}')
        continue

    if operation == '*' or 'times':
        answer :int = multiply(lst_numbers)
        print(f'Answer: {answer}')
        continue

    if operation == '/' or 'divide':
        _answer :int|float= divide(lst_numbers)
        print(f'Answer: {_answer}')
        continue
    else:
        print('Try again')

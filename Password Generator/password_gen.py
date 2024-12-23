from string import digits, ascii_letters
from secrets import choice

while True:
    user_input :int= int(input('Enter how long you want it to be or Press Enter >> '))
    lenght :int= user_input or 10
    characters :str= ascii_letters + digits

    if lenght >= 8:
        password :str= ''.join(choice(characters) for _ in range(int(lenght))) 
        print(password)
        break
    else:
        print('it have to be more than or equal 8')
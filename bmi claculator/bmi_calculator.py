"""
A body mass calculator  
I just convert all to metric and use one function to find the bmi
"""
def calculate(height, weight):
    height_squared = height * height
    print(
        f'Your BMI is {round(weight / height_squared)}'
    )


if __name__ == '__main__':
    choose_one = int(input(
        '''
        Enter 1 for (kilogram and meters)  
        ,2 for (Pounds and inches) and 3
        if its foot inches add comma in the middle
        >> 
        '''))
    height = input('Enter your height >> ')
    weight = float(input('Enter your weight >> '))
    if choose_one == 1:
        calculate(float(height),weight)

    elif choose_one == 2:
        height = float(height)/39.37
        weight = weight/2.205
        calculate(height, weight)

    else:
        feet,inches = height.split(',')
        feet= float(feet)*12
        inches = float(inches)
        height = float(feet + inches)/39.37
        weight = weight/2.205
        calculate(height, weight)

b = False
while b == False:
    print('1. add')
    print('2. subtract')
    print('3. multiply')
    print('4 exit')
    option = input('enter an option')
    if option in ('1', '2', '3'):
        num1 = int(input('enter first number'))
        num2 = int(input('enter second number'))

    if option == '1':
        total = num1 + num2
        print(f'the addition of {num1} and {num2} is {total}')
    elif option == '2':
        total = num1 - num2
        print(f'the subtraction of {num1} and {num2} is {total}')
    elif option == '3':
        total = num1 * num2
        print(f'the multiplication of {num1} and {num2} is {total}')
    elif option == '4':
        b = True



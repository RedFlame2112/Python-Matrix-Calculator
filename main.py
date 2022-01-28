"""
DRIVER CODE
"""
import options
import time
import sys

print("Welcome to the matrix calculator! Be ready to enter in a matrix you want to operate on. Give it a few seconds.")
sys.stdout.flush()
time.sleep(1)
print('\n')
print("Oh yeah, btw, make sure you scroll up a bit to get your answer as the menu will print right under lol")
sys.stdout.flush()
time.sleep(1)
print('\n')
print("We are loading the menu for you. Sit tight!")
sys.stdout.flush()
time.sleep(1)

# ======================== GLOBAL MENU FOR MATRIX CALCULATOR =================================
# menu dictionary
menu_options = {
    1: 'Generate Copy Matrix',
    2: 'Generate Transpose Matrix',
    3: 'Generate Identity Matrix',
    4: 'Find Determinant',
    5: 'Find Inverse',
    6: 'Add 2 matrices',
    7: 'Subtract 2 matrices',
    8: 'Multiply 2 matrices',
    9: 'Get Just Eigenvalues',
    10: 'Get Eigenvalues and Eigenvectors',
    11: 'Exit'
}


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])
sys.stdout.flush()
time.sleep(0.5)
while True:
    print_menu()
    option = ''
    try:
        option = int(input('Enter the operation you want to take: '))
    except:
        print('Wrong input. Please enter a number...')

    if option == 1:
        options.option1()
    elif option == 2:
        options.option2()
    elif option == 3:
        options.option3()
    elif option == 4:
        options.option4()
    elif option == 5:
        options.option5()
    elif option == 6:
        options.option6()
    elif option == 7:
        options.option7()
    elif option == 8:
        options.option8()
    elif option == 9:
        options.option9()
    elif option == 10:
        options.option10()
    elif option == 11:
        print('Thank you for using this matrix calculator. Have a good one!')
        exit()
    else:
        print('Invalid option. Please enter an integer between 1 and 9 inclusive')

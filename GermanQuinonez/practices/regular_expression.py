import re


def input_user_name():
    while True:
        name = input('Input a user name:')
        if len(re.findall(r'[a-z0-9_]', name)) == len(name):
            print('Very nice')
            break
        else:
            print('Not a valid name,')
            print('You need to be write only with lowercase letter (a-z),')
            print('number (0-9), an underscore')


def input_user_password():
    while True:
        password = input('Input a password')

        if re.match(r'[a-zA-Z0-9]{8,}', password):
            print('Very nice password')
            break
        else:
            print('Not a valid password')
            print('You need to be write with lowercase letter (a-z), number (0-9), letter (A-Z) ')
            print('and the length have to be between 8 and 16 characters')


def input_user_email():
    while True:
        email = input('Input a email: ')
        if re.match(r'[\w\d.-]+@[\w.-]+', email):
            print('Very nice')
            break
        else:
            print('Not a valid email')


input_user_name()
input_user_password()
input_user_email()

from age.calculate import calculate_age_in_minutes, calculate_age_in_hours, calculate_age_in_days
from age.messages import message_by_age

users = {}


def dictionary_users():
    """
    This function ask for the length of the dictionary.
    According the length defined, ask to the user for the name user and for the age.
    """

    print("Enter the number of users ")
    number = int(input())
    for i in range(number):
        print("Enter name")
        name = input()
        print("Enter age")
        age = int(input())
        users[name] = age


def print_users():
    """"
    This function prints the users
    """
    for user in users:
        print(f'User {user}')
        print(f'Age in days :{calculate_age_in_days(users[user])}')
        print(f'Age in hours :{calculate_age_in_hours(users[user])}')
        print(f'Age in minutes :{calculate_age_in_minutes(users[user])}')
        print(message_by_age(users[user]))


dictionary_users()
print_users()

dictionary = {}


def valid_user_id(user_id):
    """
    This function valid a user id
    :param user_id: user id
    :return: boolean
    """
    if (user_id > 0) & (user_id < 101):
        return True
    print('the user ID should be only numbers between 1 to 100.')
    return False


def valid_user_name(user_name):
    """
    This function valid a user name
    :param user_name: user name
    :return: boolean
    """
    if len(user_name) <= 8:
        return True
    print('User name should be only lowercase (nor more than 8 digits)')
    return False


def add_user(user_id, user_name):
    """
    This function adds data to dictionary,
    :param user_id:  the user ID should be only numbers between 1 to 100.
    :param user_name: User name should be only lowercase (nor more than 8 digits)
    :return: boolean
    """
    if valid_user_id(user_id) & valid_user_name(user_name):
        dictionary[user_id] = user_name.lower()
        return True
    return False


def get_user_by_id(id):
    """
    This function returns the amount of users that have their user ID
    starting with the number inserted
    (E.g. if user inserted 1, then could count all users with 1, 10,11,12,13..19 or 100),
     return and array with the user_ID that fulfilled this condition

    :param id: (only 1 number)
    :return: return and array
    """
    list_user_id = []
    for key in dictionary:
        if str(key).find(str(id)) == 0:
            list_user_id.append(key)
    return list_user_id


def get_user_by_name(name):
    """
    This Function that receives for a character (only 1 char)
    and  to return the amount of users that have their  user Name
     starting with the character inserted
     (E.g. if user inserted a, then could count all users that start with a),
     return and array with the list of user Name that fulfilled this condition
    :param name:a character (only 1 char)
    :return:return and array
    """
    list_user_id = []
    for key in dictionary:
        if str(dictionary[key]).find(str(name)) == 0:
            list_user_id.append(dictionary[key])
    return list_user_id


def user_belong_group(user_id):
    if (user_id >= 1) & (user_id <= 25):
        return "User belong Group 1"
    elif (user_id >= 26) & (user_id <= 50):
        return "User belong Group 2"
    elif (user_id >= 51) & (user_id <= 75):
        return "User belong Group 3"
    elif (user_id >= 76) & (user_id <= 100):
        return "User belong Group 4"


def print_array(array):
    """"
    This function prints the array
    """
    for value in array:
        print(value)


for i in range(102):
    print(i)
    print(add_user(i, 'User' + str(i)))

print(dictionary)
print_array(get_user_by_id('3'))
print_array(get_user_by_name('n'))
print_array(get_user_by_name('u'))
print(user_belong_group(10))
print(user_belong_group(30))
print(user_belong_group(60))
print(user_belong_group(90))

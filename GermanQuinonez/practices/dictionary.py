dictionary_data = {}


def dictionary():
    """
    This function ask for the length of the dictionary.
    According the length defined, ask to the user for the key and for the value.
    """

    print("Enter the number of elements in the dictionary")
    number = int(input())
    for i in range(number):
        print("Enter key value of element in the dictionary")
        key = input()
        print("Enter value for the key")
        value = input()
        dictionary_data[key] = value


def print_dictionary_keys():
    """
    This function prints the dictionary keys
    """
    for key in dictionary_data:
        print(key)


def print_dictionary_values():
    """"
    This function prints the dictionary values
    """
    for key in dictionary_data:
        print(dictionary_data[key])


def print_dictionary():
    """"
    This function prints the dictionary values
    """
    for key in dictionary_data:
        print(f'({key}:{dictionary_data[key]})')


def key_exist(key):
    """"
    this function defines if a key inserted by the user, exists on the dictionary.
    """
    list_keys = list(dictionary_data.keys())
    return list_keys.count(key) > 0


def value_exist(key):
    """"
    this function defines if a value inserted by the user, exists on the dictionary.
    """
    list_values = list(dictionary_data.values())
    return list_values.count(key) > 0


print("initializing dictionary")
dictionary()
print(dictionary_data)
print("Printing by keys")
print_dictionary_keys()
print("Printing values")
print_dictionary_values()
print("Printing dictionary")
print_dictionary()
dictionary_data = {'name': 'john', 'code': 6734, 'dept': 'sales'}
print("Printing dictionary")
print_dictionary()
print(key_exist('name'))
print(value_exist('john'))

def message_by_age(age):
    """
    This function prints message by age
    :param age:
    :return: message
    """
    if age <= 12:
        return "You are a child"
    elif (age >= 13) & (age < 17):
        return "You are a teenager"
    elif (age >= 18) & (age < 29):
        return "You are young"
    else:
        return "You are adult"

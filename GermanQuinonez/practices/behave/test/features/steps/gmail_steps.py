import parse
from behave import register_type, given


@given(u'I am on form Gmail new account')
def step_impl(context):
    print('')


@given(u'I fill First name with {name:D}')
def step_impl(context, name):
    print(name)


@given(u'I fill Last name with {last:D}')
def step_impl(context, last):
    print(last)


@given(u'I fill username with {user:w}')
def step_impl(context, user):
    print(user)


@given(u'I fill password with {password}')
def step_impl(context, password):
    print(password)


@given(u'I select Birthday Month on {month:D}')
def step_impl(context, month):
    print(month)


@given(u'I fill Day with {day:d}')
def step_impl(context, day):
    print(day)


@given(u'I fill Year with {year}')
def step_impl(context, year):
    print(year)


@given(u'I select Gender on {gender:D}')
def step_impl(context, gender):
    print(gender)


@given(u'I fill Mobile phone with {phone:d}')
def step_impl(context, phone):
    print(phone)


# -- TYPE CONVERTER: For a email address.
@parse.with_pattern(r'[\w\d.-]+@[\w.-]+')
def parse_email(text):
    return text


# -- REGISTER TYPE-CONVERTER: With behave
register_type(Email=parse_email)


@given(u'I fill Current email address with {email:Email}')
def step_impl(context, email):
    print(email)

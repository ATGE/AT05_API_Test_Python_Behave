@given(u'I fill zipCode with {code:d}')
def step_impl(context, code):
    print(code)


@given(u'I fill Country  with {country:w}')
def step_impl(context, country):
    print(country)


@given(u'I fill Number of Inhabitants with {inhabitants:n}')
def step_impl(context, inhabitants):
    print(inhabitants)

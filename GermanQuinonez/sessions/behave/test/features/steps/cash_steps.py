from compare import expect

@given(u'I have ${balance:g} in my account')
def step_impl(context, balance):
    context.balance = balance


@when(u'I choose to withdraw the fixed amount of ${withdraw:g}')
def step_impl(context, withdraw):
    context.withdraw = withdraw


@then(u'I should receive ${cash:g} cash')
def step_impl(context, cash):
    print("This is your $", cash)


@then(u'the balance of my account should be ${balance:g}')
def step_impl(context, balance):
    expected_result = context.balance - context.withdraw
    expect(expected_result).to_equal(balance)

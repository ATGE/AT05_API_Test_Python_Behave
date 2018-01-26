
from clients  import clients
from compare import expect
from prices import prices


@given(u'I have a list Clients')
def step_impl(context):
    context.clients =clients


@given(u'I have a list Total price')
def step_impl(context):
    context.prices = prices


@when(u'I search  a {client} with {id:d}')
def step_impl(context, client, id):
    context.client = client
    context.id = id


@when(u'A  ${price:g}')
def step_impl(context, price):
    context.price = price


@then(u'I should found  this client int the list')
def step_impl(context):
    expect(context.price).to_equal(context.prices[context.id])
    expect(context.client).to_equal(context.clients[context.id])


@when(u'I search  a {client} in the list')
def step_impl(context, client):
    context.client = client


@then(u'I should found him in the list')
def step_impl(context):
    list_clients = list(context.clients.values())
    index_client = list_clients.index(context.client)
    expect(index_client) >= 0

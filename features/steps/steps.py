from behave import *
from calculator import Calculator

@given('the second number is {y:d}') # :d przesyła do funkcji od razu int zamiast str
def step_impl(context, y):
    context.calculator.set_y(y)

@given('the first number is {x:d}')
def step_impl(context, x):
    context.calculator = Calculator()
    context.calculator.set_x(x)

@given('the second number is {y:d}')
def step_impl(context, y):
    context.calculator.set_y(y)

@when('the two numbers are added')
def step_impl(context):
    context.calculator.add()

@when('the two numbers are subtracted')
def step_impl(context):
    context.calculator.sub()

@when('I calculate delta from {a:d},{b:d},{c:d} as coefficients of the quadratic equation')
def step_impl(context, a:int, b:int, c:int):
    context.calculator = Calculator()
    context.calculator.set_delta(a, b, c)

@when('calculated delta are from {a:d}, {b:d}, {c:d} as coefficients of quadratic equation')
def step_impl(context, a:int, b:int, c:int):
    context.calculator = Calculator()
    context.calculator.set_delta(a, b, c)

@then('the result should be {result:d}')
def step_impl(context, result):
    assert(context.calculator.result == result)

@then('the result should be {result:d}')
def step_impl(context, result):
    assert(context.calculator.result == result)

@then('the equation has {numOfSolutions:d} real number solutions')
def step_impl(context, numOfSolutions):
    assert(context.calculator.number_of_solutions() == numOfSolutions)

@then('the equation has {numberOfSolutions:d} real number solutions')
def step_impl(context, numberOfSolutions:int):
    assert(context.calculator.number_of_solutions() == numberOfSolutions)
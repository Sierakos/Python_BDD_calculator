# W tym pliku definiowane są tagi

from behave import *
from calculator import Calculator

def before_scenario(context, scenario):
    if 'FirstNumber' in scenario.tags:
        context.calculator = Calculator()
        context.calculator.set_x(50)
        
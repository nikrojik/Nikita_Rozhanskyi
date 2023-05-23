from behave import *
from common.helper import TimeShifterTest
global tester


@given('we have driver initialized')
def init_driver(context):
    global tester
    tester = TimeShifterTest()


@when('we login successfully')
def login_page(context):
    tester.login_page()


@when('we go to time shift panel')
def main_page(context):
    tester.main_page()


@when('we add new time shift')
def time_shift_page(context):
    tester.time_shift_page()


@then('we have new time shift appeared')
def check_new_row(context):
    tester.check_new_row()


@then('we remove row')
def remove_row_and_check(context):
    tester.remove_row_and_check()

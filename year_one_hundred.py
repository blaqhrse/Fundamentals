"""This is a simple program that asks a user for their name and age then
prints out the year that they'll turn 100 years old"""


import time
import datetime


user_name = input('What is your name? ')
user_age = int(input('How old you are you: '))
print() # print a blank new line
current_year = datetime.datetime.now().year  # prints out only the year as an integer value
hundred = 100


def golden_year():
    if user_age > hundred:
        time.sleep(1)
        print('You are over 100 years old. Awesome!')
    elif user_age == 100:
        print('You are exactly 100 years old. Nice!')
    else:
        years_to_hundred = 100 - user_age
        final_year = current_year + years_to_hundred
        print(user_name + '. ' + 'You will be 100 years old in the year', str(final_year) + '!')


golden_year()



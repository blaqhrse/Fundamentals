import time
import datetime


user_name = input('What is your name? ')
user_age = int(input('How old you are you: '))
print()
current_year = datetime.datetime.now().year  # prints out only the year as an integer value

hundred = 100
if user_age > hundred:
    time.sleep(1)
    print('You are over 100 years old. Awesome!')
elif user_age == 100:
    print('You are exactly 100 years old. Nice!')
else:
    years_to_hundred = 100 - user_age
    final_year = current_year + years_to_hundred
    print('You will be 100 in the year', final_year)




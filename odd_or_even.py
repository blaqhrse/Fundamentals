"""This is a simple program that evaluates if number is even or odd."""

number = int(input('Enter a number: '))


def even_odd():
    if number % 2 == 0:
        print('Number is even')

    else:
        print('Number is odd')


even_odd()

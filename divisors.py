"""This program prints out all the divisors of the number entered."""


number = int(input('Enter a number: '))

end_of_range = number + 1

list_of_divisors = []


def divisors():
    all_numbers = range(1, end_of_range)
    for item in all_numbers:
        if number % item == 0:
            list_of_divisors.append(item)
    print('The divisors of ' + str(number) + ' are ' + str(list_of_divisors)[1:-1])  # The slicing removes the []


divisors()










"""
1- get an int and turn into str
2- strip the string and append to a list
3- get each str from list and turn into int and power to 2 and sum
4- if number > 10: again
5- if number < 10: check if num == 1
"""


def get_next_number(number):
    number_str = str(number)
    numbers_list = [int(char) for char in number_str]

    next_number = sum(char ** 2 for char in numbers_list)

    return next_number


def is_happy_number(number):
    seen_numbers = set()

    while number != 1 and number not in seen_numbers:
        seen_numbers.add(number)
        number = get_next_number(number)

    return number == 1


# print(is_happy_number(19))
# print(is_happy_number(2))

if __name__ == "__main__":
    num = int(input("Enter number: "))
    print(is_happy_number(num))

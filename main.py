import random
import string


def generate_password():
    num_letters = int(input("How many letters would you like in your password? "))
    num_symbols = int(input("How many symbols? "))
    num_numbers = int(input("How many numbers? "))

    letters = string.ascii_letters
    symbols = "!@#$%^&*()-_=+"
    numbers = string.digits

    password_characters = random.sample(letters, num_letters) + \
                          random.sample(symbols, num_symbols) + \
                          random.sample(numbers, num_numbers)
    random.shuffle(password_characters)

    password = "".join(password_characters)

    return password


generate_password = generate_password()
print("Your password is: ", generate_password)

def factorial(number: int):
    total = number // 5
    number = number // 5
    while (number % 5 == 0):
        number = number / 5
        total += total // 5
    return total

number = input("Number: ")
try:
    number = int(number)
    print(factorial(number))
except Exception as _ex:
    print(f"{_ex}\nWrite a number, not a word!")
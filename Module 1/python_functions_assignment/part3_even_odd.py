def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = 7
result = check_even_odd(num)
print("Number is", result)

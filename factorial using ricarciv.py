def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

result = factorial(6)
print("Factorial:", result)
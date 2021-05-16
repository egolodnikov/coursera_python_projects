"""
# Syntax error example:
print(15/5))
"""

"""
# ZeroDivisionError example: 
print(15 / 0)
"""

"""
# Example custom ValueError:
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Your name is: " + name)
if age < 18:
    raise ValueError("Error: you need to be over 18")
else:
    print("Your age is: " + str(age))
"""

"""
# Example custom Exception:
number = 4
if number < 5:
    raise Exception("Error: value need to be greater than 5")
"""

"""
# Example custom AssertionError
x = 1
y = 0
assert y != 0, "Invalid Operation"
print(x / y)
"""

"""
# Example custom AssertionError:
def print_age(age):
    assert age > 0, "The value for age has to be greater than zero"
    print("Your age is: " + str(age))


print_age(-1)
"""

"""
# Example try except ZeroDivisionError
try:
    num1 = 4
    num2 = 0
    result = num1 / num2
    print(result)
except ZeroDivisionError as e:
    print(e)
"""

"""
# Example try except else TypeError:
try:
    num1 = '4'
    num2 = 2
    result = num1 / num2
    print("End of try block")
except TypeError as e:
    print("TypeError: Value has to be an integer")
else:
    print("No exception raised")
"""

"""
# Example try except finally FileNotFoundError
try:
    f = open("example1.txt")
except FileNotFoundError:
    print("FileNotFoundError: The file is not found")
finally:
    f.close()
"""

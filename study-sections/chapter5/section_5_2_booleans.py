# Section 5.2: Logical Operators
# Experiment with and, or, not

print("=== Logical Operators ===\n")

# 1. AND operator - both must be true

print("True and True:", True and True)
print("True and False:", True and False)
print("False and True:", False and True)
print("False and False", False and False)
print()

# 2. OR Operator - at least one must be true
print("2. OR operator:")
print("True or True:", True or True)
print("True or False:", True or False)
print("False or True:", False or True)
print("False or False:", False or False)

# 3. NOT operator - flips the value
print("3. NOT operator:")
print("not True:", not True)
print("not False:", not False)
print()


# Examples

# Check to see if a number is in a range (between 10 and 20)

x = 15

print("Is X bigger than 10 and smaller than 20?", x > 10 and x < 20)

n = 12

print("Check to see if a number is divisble by 2 or 3", n % 2 == 0 and n % 3 == 0)


n = 5

print("Check to see if a number is not negative:", not n < 0)
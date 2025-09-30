# Section 5.2: Boolean Expressions
# Learning about True/False values and comparison operators

print("=== Section 5.2: Boolean Expressions ===")
print()

# Boolean values - the basics
print("1. Boolean Values:")
print("True:", True)
print("False:", False)
print("Type of True:", type(True))
print("Type of False:", type(False))
print()

# Comparison operators
print("2. Comparison Operators:")
print("Equal to (==):")
print("5 == 5:", 5 == 5)
print("5 == 3:", 5 == 3)
print()

print("Not equal to (!=):")
print("5 != 3:", 5 != 3)
print("5 != 5:", 5 != 5)
print()

print("Greater than (>):")
print("7 > 3:", 7 > 3)
print("3 > 7:", 3 > 7)
print()

print("Less than (<):")
print("3 < 7:", 3 < 7)
print("7 < 3:", 7 < 3)
print()

print("Greater than or equal (>=):")
print("5 >= 5:", 5 >= 5)
print("5 >= 3:", 5 >= 3)
print("3 >= 5:", 3 >= 5)
print()

print("Less than or equal (<=):")
print("3 <= 5:", 3 <= 5)
print("5 <= 5:", 5 <= 5)
print("7 <= 5:", 7 <= 5)
print()

# Comparing different types
print("3. Comparing Strings:")
print("'apple' == 'apple':", 'apple' == 'apple')
print("'apple' == 'banana':", 'apple' == 'banana')
print("'apple' < 'banana':", 'apple' < 'banana')  # Alphabetical order
print("'Zebra' < 'apple':", 'Zebra' < 'apple')    # Capital letters come first
print()

# Variables in comparisons
print("4. Using Variables:")
x = 10
y = 15
print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")
print(f"x < y: {x < y}")
print(f"x + 5 == y: {x + 5 == y}")
print()

# The bool() function
print("5. The bool() function:")
print("bool(1):", bool(1))
print("bool(0):", bool(0))
print("bool('hello'):", bool('hello'))
print("bool(''):", bool(''))
print("bool([1, 2, 3]):", bool([1, 2, 3]))
print("bool([]):", bool([]))
# Section 5.2: Boolean Expressions
# Learning about True/False values and comparison operators

print("=== Basic Boolean Values ===")
print(True)
print(False)
print(type(True))
print(type(False))

print("\n=== Comparison Operators ===")
# Equal to (==)
print("5 == 5:", 5 == 5)
print("5 == 3:", 5 == 3)

# Not equal to (!=)
print("5 != 3:", 5 != 3)
print("5 != 5:", 5 != 5)

# Greater than (>)
print("5 > 3:", 5 > 3)
print("3 > 5:", 3 > 5)

# Less than (<)
print("3 < 5:", 3 < 5)
print("5 < 3:", 5 < 3)

# Greater than or equal to (>=)
print("5 >= 5:", 5 >= 5)
print("5 >= 3:", 5 >= 3)
print("3 >= 5:", 3 >= 5)

# Less than or equal to (<=)
print("3 <= 5:", 3 <= 5)
print("5 <= 5:", 5 <= 5)
print("5 <= 3:", 5 <= 3)

print("\n=== Comparing Strings ===")
print("'apple' == 'apple':", 'apple' == 'apple')
print("'apple' == 'banana':", 'apple' == 'banana')
print("'apple' < 'banana':", 'apple' < 'banana')  # Alphabetical order

print("\n=== Boolean with Variables ===")
x = 10
y = 20
print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")
print(f"x < y: {x < y}")
print(f"x != y: {x != y}")
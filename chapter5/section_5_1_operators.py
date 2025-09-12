print("Floor division and modulus")

# movie runtime
print("\n--- Movie Runtime ---")
minutes = 105
print(f"Movie runtime: {minutes} minutes")

# regular division
print("\n--- Regular division using the divison operator (/) ---")
hours_in_decimal = minutes / 60
print(f"Regular division: {minutes} / 60 = {hours_in_decimal}")

# floor division, will give integer hours
print("\n--- Floor division using the floor division operator (//), it divides the left operand by the right operand and then round the result down")
example = 5 // 2.5
print(f"{example} = 5 // 2.5")
example2 = 5 // 2.6
print(f"{example2} = 5 // 2.6")
hours_in_integer = minutes // 60
print(f"Floor division: {minutes} // 60 = {hours_in_integer}")

# Method 1: calculate reminder using subtraction
print("\n--- Calculate the reminder by subtracting the integer part (in minutes) from the total minutes ---")
remainder_method1 = minutes - (hours_in_integer * 60)
print(f"Remainder method 1, calculate by subtracing the integer part from the total: {minutes} - ({hours_in_integer} * 60) = {remainder_method1}")


# Method 2: calculate reminder using the modulus operator
print("\n--- calculate the reminder using the modulus operator (%) ---")
remainer_method2 = minutes % 60
print(f"Remainder method 2, calculate using the modulus operator: {minutes} % 60 = {remainer_method2}")
print(f"\nSo {minutes} minutes = {hours_in_integer} hours and {remainer_method2} minutes")

# Try out
print("\n--- Try out ---")
test = 100 % 60
print(test)
test2 = 105 % 60
print(test2)


# Modulus practical uses, remaining from here
print("\n==== Modulus practical uses ===")




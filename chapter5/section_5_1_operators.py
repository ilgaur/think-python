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


# 1. Check if a number is even or odd
print("\n==== Detect even/odd in a python list ===")

for num in [23, 21, 3, 5, 6, 10, 12, 13, 7]:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

# 2. Divisibilty check
print("\n==== Check if a number is divisible by another ===")
number = 25
for divisor in [2, 4, 6, 9, 10, 25]:
    if number % divisor == 0:
        print(f"{number} is divisble by {divisor}")
    else:
        print(f"{number} is not divisible by {divisor}")

# 3. Extract digits from right (?)
print("\n==== Extracting digits from right using modulus ===")
number_to_exract_digits_from = 33123124
print(f"Original number: {number_to_exract_digits_from}")
print(f"Last digit: {number_to_exract_digits_from % 10}")
print(f"Last two digits: {number_to_exract_digits_from % 100}")
print(f"Last three digits: {number_to_exract_digits_from % 1000}")


# 4. Cycling through days
print("\n==== Cycling through days ===")
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
start_day = 0 #monday
print("\nShow next 10 days -->")

for i in range(10):
    day_index = (start_day + i) % 7
    print(f"Day {i}: {days[day_index]} --- i is: {i} --- day_index is {day_index} so 0 + {i} % 7 will be {day_index}")
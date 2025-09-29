# Chapter 5, Section 5.1 Review Questions
# Test Your Understanding

print("=== Chapter 5.1 Review Questions ===")

# Question 1: How would you check if a year is divisible by 4 (leap year check)?
print("\n--- Question 1: Leap Year Check ---")
# Your code here
def is_leap_year(year):
    if year % 4 == 0:
        print(f'{year} is divisible by 4 (leap year candidate): True')
    else:
        print(f'{year} is NOT divisible by 4: False')

years = [1901, 2003, 2001, 2004, 2017, 2020]
for year in years:
    is_leap_year(year)
# Question 2: If you have 37 items and want to put them in groups of 5, 
# how many complete groups do you get and how many items are left over?
print("\n--- Question 2: Grouping Items ---")
# Your code here

def complete_groups(total_items, group_size):
    complete = total_items // group_size
    leftover = total_items % group_size
    print(f'Total items: {total_items}, Group size: {group_size} => Complete groups: {complete}, Leftover items: {leftover}')

complete_groups(37, 5)  # Original question
complete_groups(35, 5)  # Your test case

# Question 3: How could you use modulus to create a "wrap-around" effect in a game?
print("\n--- Question 3: Wrap-around Effect ---")


# Your code here
board_size = 8
current_position = 6
steps_to_move = 3

print(f"Board has {board_size} positions: 0 to {board_size - 1}")
print(f"Current position: {current_position}")
print(f"Steps to move: {steps_to_move}")

# The wrong way
wrong_position = current_position + steps_to_move
print(f"Wrong new position (without wrap-around): {wrong_position}")

# The right way using modulus
correct_position = (current_position + steps_to_move) % board_size

print(f"With wrap-around: ({current_position} + {steps_to_move}) % {board_size} = {correct_position}")

print(f"\nStep-by-step movement:")
pos = current_position
for step in range(steps_to_move):
    next_pos = (pos + 1) % board_size
    print(f" Step {step + 1}: Position {pos} → Position {next_pos}")
    pos = next_pos
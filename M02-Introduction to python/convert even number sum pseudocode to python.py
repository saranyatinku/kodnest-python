# Read the limit
limit = int(input())
number = 1
total = 0

# Initialize the loop variable and total
while number <= limit:
    if number % 2 == 0:
        total += number
    number += 1

# Examine every number from 1 to limit

# Display the result
print(f"Even Sum: {total}")
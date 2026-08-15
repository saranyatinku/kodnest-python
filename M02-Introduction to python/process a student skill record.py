skills = []

# Read and store five skills
for i in range(5):
    skill = input()
    skills.append(skill)

# Convert the list into a tuple
skill_record = tuple(skills)

# Create the required slices
first_three = skill_record[0:3]
last_two = skill_record[-2:]
alternate = skill_record[0::2]
reverse_order = skill_record[::-1]

# Display all required results
print("Skill Record:", skill_record)
print("First Three:", first_three)
print("Last Two:", last_two)
print("Alternate Skills:", alternate)
print("Reverse Order:", reverse_order)
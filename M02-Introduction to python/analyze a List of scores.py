n = int(input())
scores = []

# Read and store all scores
for i in range(n):
    score = int(input())
    scores.append(score)

search_score = int(input())

# Display the highest, lowest and total scores
highest = max(scores)
lowest = min(scores)
total = sum(scores)

# Display whether search_score is present
if search_score in scores:
    result = "Found"
else:
    result = "Not Found"

print(f"Highest Score: {highest}")
print(f"Lowest Score: {lowest}")
print(f"Total Score: {total}")
print(f"Search Result: {result}")
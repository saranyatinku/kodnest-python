sentence = input()

# Clean and normalize the sentence
cleaned = sentence.strip()
no_dots = cleaned.replace(".", "")
normalized = no_dots.lower()

# Split the sentence and create the slug
words = normalized.split()

# Produce the uppercase form and search result
slug = '-'.join(words)

# Display all processed values
print(f"Cleaned: {cleaned}")
print(f"Normalized: {normalized}")
print(f"Words: {words}")
print(f"Slug: {slug}")
print(f"Uppercase: {normalized.upper()}")
print(f"Python Position: {normalized.find('python')}")
text = input().strip().lower()

# Words to find (all in lowercase)
words_to_find = ["sand", "water", "fish", "sun"]

# Initialize total count
total_count = 0

# Loop through each word and count occurrences
for word in words_to_find:
    total_count += text.count(word)

# Print the total count
print(total_count)
text = "Python"
count = 0

# Loop through the numeric positions (0, 1, 2, 3, 4, 5)
for i in range(len(text)):
    # Look up the character at that specific position
    if text[i] in "aeiouAEIOU":
        count += 1

print("Vowel count:", count, "in text:", text)

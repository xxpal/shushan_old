vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels:")

# Create an empty dictionary
found = {}

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)     # Insert key with a value of default if key is not in the dictionary.
        found[letter] += 1
for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')

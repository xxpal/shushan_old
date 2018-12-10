vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels:")

# Create an empty dictionary
found = {}
# Initialize the value associated with each of the keys (each vowel) to 0
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

for letter in word:
    if letter in vowels:
        found[letter] += 1
for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')

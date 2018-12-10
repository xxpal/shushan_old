vowels = ['a', 'e', 'i', 'o', 'u']

word = input('请输入一个单词：')
print('您输入的单词是{}，包含的元音字母有：'.format(word), end='')

# for letter in word:
#     if letter in vowels:
#         print(letter, end='\t')

found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for i in found:
    print(i, end='\t')


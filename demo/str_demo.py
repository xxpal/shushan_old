# print str1
str1 = 'Hello'
print(str1)

# concatenate str1 and str2, then print
str2 = 'World'
print(str1 + str2)

# concatenate str1 and str2 with a comma separation, then assign it to str3 and print str3
str3 = str1 + ',' + str2
print(str3)

print(str3[0])          # print the first letter
print(str3[5])          # print the letters in index 5
print(str3[-1])         # print the last letter
print(str3[:])          # print the whole string
print(str3[2:])         # print the slice string from index 2 to the end
print(str3[:5])         # print the slice string from beginning to index 5 (excluded)
print(str3[3:7])        # print the slice string from index 3 to index 7 (excluded)
str3 = str3[2:5]        # Assign the slice string from index 2 to index 5 to str3
print(str3 + 'Good!')   # concatenate str3 to 'Good!' then print

# Use '''..''' or """ ...""" for strings with special characters
html = '''
<html>
    <title>String Demo</title>
    <body>Hello World!</body>
</html>
'''
print(html)

# str3[0] = 'h'
# print(str3)
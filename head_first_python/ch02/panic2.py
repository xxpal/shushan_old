phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# Slice out the word "on" from "plist"
new_phrase = ''.join(plist[1:3])
# Then, picked out each additional letter that we needed: space, "t", "a" and "p".
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]])

print(plist)
print(new_phrase)

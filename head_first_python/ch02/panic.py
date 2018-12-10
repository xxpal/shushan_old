phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# This small loop pops the last four objects from "plist". No more 'nic!'.
for i in range(4):
    plist.pop()
# Get rid of 'D' at the start of the list
plist.pop(0)
# Find, then remove, the apostrophe from the list
plist.remove("'")
# Swap the two objects at the end of the list by first popping each object from the list,
# then, using the popped objects to extend the list.
# The pops occur first, then the extend happens.
plist.extend([plist.pop(), plist.pop()])
# This line of code pops the space from the list, then inserts it back into the list at index location 2.
# The pop occurs first, before the insert happens.
plist.insert(2, plist.pop(3))

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)

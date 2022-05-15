# Write a python program to check if the word “name” is present
# in the string entered by the user (Print : “Yes” or “No”)

str = input("str = ")
if str.find('name') == -1:
    print('No')
else:
    print('Yes')

#defining a reverse function
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

#user input string 
s = 'Python is a case sensitive language'
#finding length of given str
print('(a)')
print(len(s),"\n")

#reversing the given str
print('(b)')
print(reverse(s),'\n')

#using slice fnc to store "a case sensitive"
newstr=s[10:27]
print('(c)')
print(newstr,'\n')

#replace "a case sensitive" with "object oriented"
s.replace('a case sensitive','object oriented')
print('(d)')
print(s.replace('a case sensitive','object oriented'),'\n')

#Find index of substring “a” in the given input string
print('(e)')
print(s.find('a'),'\n')

#Remove the white spaces from the given input string
print('(f)')
print(s.replace(" ",""))
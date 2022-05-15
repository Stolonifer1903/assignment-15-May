from re import X
from tkinter import Y


def triangle(a, b, c):
    if(c > (a+b) or a > (b+c) or b > (c+a)):
        print("No")
    else:
        print("YES")


x = int(input("x="))
y = int(input('y='))
z = int(input('z='))
print('can we form a triangle=')
triangle(x, y, z)

#!/usr/bin/python3
g=1;error=0.00000001
a=float(input("enter a number to find it's squre root:"))
if not a>0:
    print("input error")
else:
    while(abs(g*g-a)>error):
        g=(g+a/g)/2
    print("the squre root is:",round(g,3))
        

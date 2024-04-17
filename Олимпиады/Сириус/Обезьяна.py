def inpint ():
    return int(input())
n= inpint ()
d= inpint ()
a = []
for i in range (n):
    a.append (inpint())
del inpint
print (a)

dist=0
for i,var in enumerate (a):
    a[i]= var + dist
    dist+=d
del dist
print (a)

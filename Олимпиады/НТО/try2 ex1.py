# put your python code here
from itertools import *
x = 3#int(input())
y = 5#int(input())
n=0
print (list(permutations (-2,2)), list (permutations(-1,1)))
for i in permutations (product (-2,2), (-1,1)):     #err
    for k, var in enumerate({x,y}):
        if not 0< var+i[k] <9:
            break
    else:
        n+=1
print (n)

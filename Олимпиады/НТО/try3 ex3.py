from itertools import permutations
a= input().split()
n= int (a[0])
m= int (a[1])
del a

def permutationsx2 (n, m):  #недоделано
    if n==m:
        def res():
            yield (n,m)
        return res
    else:
        return permutations ((n, m))
res = set()
def choko (n,m):    #нужна меморизация
    for b, c in permutationsx2 (n, m):   #if == [+]
        for i in range (1, b):
            res.add (s-i*c)
            choko (i, c)
s = n*m
choko (n, m)
#print (res)
for i in res:
    print (str(i) + " ", end= "")

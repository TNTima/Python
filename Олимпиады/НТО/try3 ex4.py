n = int (input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]   #как-то зациклить
max = 0
for i in range (n):     #здорово бы использовать max
    sum = a[i] + b[i]
    if sum > max:
        max= sum
del sum

c= []
for i in range (n):
    c.append (max-(a[i]+b[i]))

#print (a,b,c)

del a
def generator (c,b):
    for i in range (c):
        yield "."
    for i in range (b):
        yield "*"
    while True:
        yield "#"

spGen = []      #список генераторов
for i in range (n):
    spGen.append (generator (c[i],b[i]))
for strI in range (max):
    for gen in spGen:
        for out in gen:
            print (out, end='')
            break
    print ()

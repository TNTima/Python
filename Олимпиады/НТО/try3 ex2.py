n= int(input())
a= input().split()
for i,var in enumerate (a):
    a[i] = int(var)
#print (i,var,a)

high=0
low=0
a1= a[0]
for i in range (1, n):
    a0= a1
    a1= a[i]
    up = a1-a0
    if up > 0:
        if a1>2000:
            if a0>2000:
                high+=up
            else:
                ilow= 2000-a0
                low+= ilow
                high+= up - ilow
        else:
            low+=up
print (low, high)

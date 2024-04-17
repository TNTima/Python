n = int (input())
a = int (input())
b = int (input())
polov= n//2
if polov > b:
    a = n - b
elif polov + n%2 > a:
    b = n - a
else:
    b = polov
    a = n - b
print (a,b)

a=int(input())
b=int(input())
n=int(input())
port= []
for i in range (n):
    port.append (int(input()))
#print (a,b,n,port)
time=0
for obj in (a,b):
    stop = None
    for p in port:
        start= stop
        stop= p
        if obj < stop:
            if start == None:
                time+= abs (stop-obj)
            else:
                time+= min(abs (start-obj),abs (stop-obj))
            break
    else:
        time+= abs (stop-obj)
time+=1
#print (time)
print (min (time, abs(a-b)))

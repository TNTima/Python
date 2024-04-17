a = [int (i) for i in input().split()]
lenN = a[1]
a = input().split() #стоит ли в set?
#print (a)
sp = set()

def bol (char):
    if char == '1':
        return True
    else:
        return False
for num in a:
    templist = []
    for simv in num:
        templist.append (bol (simv))
    sp.add (tuple(templist.copy()))
del templist, a, bol

#print (lenN, sp)

disk = 0
black_list = set()   #множество len(списков) = lenN

for num in sp:
    diff = lenN - len (num)
    if 0 < diff:
        disk+= 2**(diff)
    else:
        cut = num [:lenN]
        if cut not in black_list:
            black_list.add (cut)
            disk+=1    #одинаковый путь (устранено)
del diff, cut
#print (black_list)
del black_list
print (2**lenN - disk)

def permutations (inp_set):
    #set -> yield list
    if inp_set == set():
        return []
    el = inp_set.pop()
    for res in permutations (inp_set):
        for i in range (len(res) + 1):
            res.insert (i, el)
            yield res

for i, el in enumerate (permutations (set("abc"))):
    print (f"{i}= {el}")
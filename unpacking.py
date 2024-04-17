class A:
    @classmethod
    def __iter__ (cls):
        return range (5)
    
    def __iter__ (self):
        for i in range (6, 10):
            yield (i, i)

a= A()
print (f"A = {A}, type(A) = {type(A)}", f"a = {a}, type(a) = {type(a)}", sep = '\n')

def my_print (*args, **kwargs):
    print (locals())

for i in a:
    print (i)
#print (*a)
my_print (*a, **a)
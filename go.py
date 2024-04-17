"""
#@classmethod
def expand (f):
    from inspect import signature
    sig = signature(f)
    print (sig, sig)
    def warper (super_args, args):
        pass
"""

class Matrix (list):
    #@expand
    def __new__ (cls, len_list, init_v=None):
        if len(len_list) > 1:
            self.len = len_list[0]
            tail = len_list[1:]
            for _ in range (self.len):
                self.append (Matrix(tail))
        elif len(len_list) == 1:
            super().__init__([init_v] * len_list[0])
        else:
            raise ValueError ("empty list", len_list)
    
    @classmethod
    def init (cls, l):

        def dec (f1, f2):
            def warper (*args, **kwargs):
                return f1(f2(*args, **kwargs))
            return warper
    
        from curry import curry as curry
        lst = curry (dec, list)
        @lst
        def len_list (l):
            while True:
                try:
                    yield len(l)
                except TypeError:
                    return
        
        matrix = Matrix (len_list (l))
    
    def insert(self, i, obj) -> None:
        if i :
            super().insert(i, obj)

    def append(self, obj) -> None:
        return super().append(obj)
            


a= Matrix([5]*2)
print (a)

b = Matrix.init ([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print (b)
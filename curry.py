
def curry (f, *args, **kwargs):
    #kwargs = my_dict (kwargs)
    def warper (*local_args, **local_kwargs): 
        nonlocal kwargs
        def __iadd__ (self, other):
            for key, v in other.items():
                if key in self:
                    raise ValueError(f"dicts intersect at [{key}]")
                else:
                    self [key] = v

        __iadd__ (kwargs, local_kwargs)
        #print ("local_kwargs=", local_kwargs)
        return f (*(args + local_args), **kwargs)
    return warper

if __name__ == "__main__":
    class my_dict (dict):
        def __iadd__ (self, other):
            for key, v in other.items():
                if key in self:
                    raise ValueError(f"dicts intersect at [{key}]", key, self[key], other[key])
                else:
                    self [key] = v
        
        def __add__ (self, other):
            import copy
            res = copy (self)
            res += other
            return res

    def test (first, *args, **kwargs):
        print (locals())

    a = curry (test, 1, 2, a=5)
    a (3, b=8)

    b = curry(test, same=9)
    b = curry(b, same=5)
    print ("starting...")
    b()
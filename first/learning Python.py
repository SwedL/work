

def reduce_fraction(fraction):
    def nod(x=min(fraction)):
        if fraction[0] % x == 0 and fraction[1] % x == 0:
            return tuple(list(map(lambda i: int(i / x), fraction)))
        else:
            return nod(x-1)
    return nod()


print(reduce_fraction([80, 120]))

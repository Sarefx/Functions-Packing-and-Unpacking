def calculate_total(*args):
    total = sum(args)
    print(total)

calculate_total(25)

def unpacker():
    return (1,2,3)

var1, var2, var3 = unpacker()

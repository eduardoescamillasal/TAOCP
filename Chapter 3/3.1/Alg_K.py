'''
Algorithm K (pg 5 vol 2)
"Super-random" number generator
'''

def init(x):
    #k1
    y = int(x/10**9) + 1
    #k2random step
    z = int(x/10**8)%10
    # goto K(3+z)
    while y > 0:
        if z == 0:
            x = k3(x)
            x = k4(x)
            x = k5(x)
            x = k6(x)
            x = k7(x)
            x = k8(x)
            x = k9(x)
            x = k10(x)
            x = k11(x)
            x = k12(x)
            
        if z == 1:
            x = k4(x)
            x = k5(x)
            x = k6(x)
            x = k7(x)
            x = k8(x)
            x = k9(x)
            x = k10(x)
            x = k11(x)
            x = k12(x)
        if z == 2:
            x = k5(x)
            x = k6(x)
            x = k7(x)
            x = k8(x)
            x = k9(x)
            x = k10(x)
            x = k11(x)
            x = k12(x)
        if z == 3:
            x = k6(x)
            x = k7(x)
            x = k8(x)
            x = k9(x)
            x = k10(x)
            x = k11(x)
            x = k12(x)
        if z == 4:
            x = k7(x)
            x = k8(x)
            x = k9(x)
            x = k10(x)
            x = k11(x)
            x = k12(x)
        if z == 5:
            x = k8(x)
            x = k9(x)
            x = k10(x)
            x = k11(x)
            x = k12(x)
        if z == 6:
            x = k9(x)
            x = k10(x)
            x = k11(x)
            x = k12(x)
        if z == 7:
            x = k10(x)
            x = k11(x)
            x = k12(x)
        if z == 8:
            x = k11(x)
            x = k12(x)
        if z == 9:
            x = k12(x)
    
        y,z = k13(x,y)
    return x
    
        
    


def k3(x):
    if x < 5*10**9:
        x += 5*10**9
    print(x)
    return x

def k4(x):
    x = int(x**2 / 10**5)%10**10
    print(x)
    return x

def k5(x):
    x = (1001001001*x)%10**10
    print(x)
    return x

def k6(x):
    if x < 10**8:
        x += 9814055677
    else:
        x = 10**10 - x
    print(x)
    return x

def k7(x):
    x = 10**5*(x%10**5) + int(x/10**5)
    print(x)
    return x

def k8(x):
    x = k5(x)
    print(x)
    return x

def k9(x):
    res = []
    digits = list(str(x))
    for dig in digits:
        if int(dig) == 0:
            res.append(dig)
        else:
            res.append(str(int(dig) - 1))
    r = ''.join(res)
    x = int(r)
    print(x)
    return x

def k10(x):
    if x < 10**5:
        x = x**2 + 99999
    else:
        x = x - 99999
    return x

def k11(x):
    while True:
        if x < 10**9:
            x = 10*x
        else: break
    print(x)
    return x

def k12(x):
    x = int(x*(x-1)/10**5)%10**10
    print(x)
    return x

def k13(x,y):
    y -= 1
    z = int(x/10**8)%10
    return y,z

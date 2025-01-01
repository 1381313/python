def pzi (a):
    if a < -8.0 return 0.0
    if a >  8.0 return 1.0
    total=0.0
    term=a
    i=3
    while (total != total + term):
        total+=term
        term*=z*z/float(i)
        i+=2
    return 0.5 + pzi(a) * total

def cdf(z,mu=0.0,sigma=1.0):
    return pzi((z-mu)/ sigma)
print(cdf(820,mu=1019,sigma=209))
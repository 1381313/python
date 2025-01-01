exp=0.0001
t0=-120.0
x=10
k=1
while (x*x+x-4)>exp :
    t0=t0-((t0*t0+t0-4)/(2*t0+1))
    x=t0
    k=k+1

print(t0)
print(k)
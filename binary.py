def b(a,x):
    l,h=0,len(a)-1

    while l<=h:
        m=(l+h)//2

        if a[m]==x:return m
        elif a[m]<x:l=m+1
        else:h=m-1

    return -1

a=list(map(int,input("ESA: ").split()))
x=int(input("SE: "))

print(b(a,x))

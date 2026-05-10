def commission(p,o):

    if p<0 or o<0:
        return "Invalid"

    ps=p*60
    os=o*40
    ts=ps+os

    if ts<=1000:
        c=ts*0.10
    elif ts<=1800:
        c=100+(ts-1000)*0.15
    else:
        c=220+(ts-1800)*0.20

    return ps,os,ts,c

p=int(input("Peanut Butter: "))
o=int(input("Oats: "))

r=commission(p,o)

if r=="Invalid":
    print("Invalid Input")
else:
    print("PB Sales =",r[0])
    print("Oats Sales =",r[1])
    print("Total Sales =",r[2])
    print("Commission =",r[3])

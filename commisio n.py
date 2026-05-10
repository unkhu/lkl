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


| Variable | Purpose                |
| -------- | ---------------------- |
| p        | Peanut Butter quantity |
| o        | Oats quantity          |
| ps       | Peanut Butter sales    |
| os       | Oats sales             |
| ts       | Total sales            |
| c        | Calculated commission  |

    | TC No | Peanut Butter | Oats | PB Sales | Oats Sales | Total Sales | Expected Commission | Purpose             |
| ----- | ------------- | ---- | -------- | ---------- | ----------- | ------------------- | ------------------- |
| TC1   | 5             | 5    | 300      | 200        | 500         | 50                  | Below 1000 range    |
| TC2   | 10            | 10   | 600      | 400        | 1000        | 100                 | Boundary value      |
| TC3   | 15            | 10   | 900      | 400        | 1300        | 145                 | 15% slab            |
| TC4   | 20            | 15   | 1200     | 600        | 1800        | 220                 | Upper boundary      |
| TC5   | 25            | 20   | 1500     | 800        | 2300        | 320                 | Above 1800 slab     |
| TC6   | 0             | 0    | 0        | 0          | 0           | 0                   | Minimum input       |
| TC7   | -1            | 5    | Invalid  | Invalid    | Invalid     | Invalid             | Negative PB input   |
| TC8   | 5             | -2   | Invalid  | Invalid    | Invalid     | Invalid             | Negative oats input |
| TC9   | 8             | 7    | 480      | 280        | 760         | 76                  | Normal low sales    |
| TC10  | 30            | 25   | 1800     | 1000       | 2800        | 420                 | Large sales         |


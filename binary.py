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
    | Path ID | Path Description                                |
| ------- | ----------------------------------------------- |
| P1      | Element found at middle                         |
| P2      | Element greater than middle → search right side |
| P3      | Element smaller than middle → search left side  |
| P4      | Element not found after loop termination        |



| TC ID | Independent Path | Input Key | Expected Output             | Actual Output               | Status |
| ----- | ---------------- | --------- | --------------------------- | --------------------------- | ------ |
| TC1   | IP1              | 40        | Element Found at position 3 | Element Found at position 3 | PASS   |
| TC2   | IP2              | 60        | Element Found at position 5 | Element Found at position 5 | PASS   |
| TC3   | IP3              | 20        | Element Found at position 1 | Element Found at position 1 | PASS   |
| TC4   | IP4              | 25        | Element Not Found           | Element Not Found           | PASS   |
| TC5   | IP2              | 70        | Element Found at position 6 | Element Found at position 6 | PASS   |
| TC6   | IP3              | 10        | Element Found at position 0 | Element Found at position 0 | PASS   |
| TC7   | IP4              | 100       | Element Not Found           | Element Not Found           | PASS   |
| TC8   | IP4              | -5        | Element Not Found           | Element Not Found           | PASS   |
| TC9   | IP2              | 50        | Element Found at position 4 | Element Found at position 4 | PASS   |
| TC10  | IP3              | 30        | Element Found at position 2 | Element Found at position 2 | PASS   |


| IP ID | Independent Path                                 |
| ----- | ------------------------------------------------ |
| IP1   | Start → mid element equals key → Found           |
| IP2   | Start → key > mid → move right → Found           |
| IP3   | Start → key < mid → move left → Found            |
| IP4   | Start → multiple comparisons → Element not found |

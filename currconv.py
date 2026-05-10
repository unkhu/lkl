r = {"USD":1, "EUR":0.92, "INR":83, "GBP":0.79}

c = list(r.keys())

amt = float(input("Amount: "))
f = int(input("From(USD:1,EUR:2,INR:3,GBP:4):"))
t = int(input("To(USD:1,EUR:2,INR:3,GBP:4): "))

if f<1 or f>4 or t<1 or t>4:
    print("Invalid Choice")
else:
    ans = (amt/r[c[f-1]]) * r[c[t-1]]
    print("Converted:", round(ans,2), c[t-1])

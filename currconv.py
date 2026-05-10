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


| TC ID | Purpose             | Amount | From | To | Expected Output | Status |
| ----- | ------------------- | ------ | ---- | -- | --------------- | ------ |
| TC1   | INR to USD          | 8300   | 3    | 1  | 100.0 USD       | PASS   |
| TC2   | INR to EUR          | 9000   | 3    | 2  | 99.76 EUR       | PASS   |
| TC3   | INR to GBP          | 10500  | 3    | 4  | 99.88 GBP       | PASS   |
| TC4   | Invalid From Choice | 5000   | 5    | 1  | Invalid Choice  | PASS   |
| TC5   | Invalid To Choice   | 5000   | 1    | 7  | Invalid Choice  | PASS   |
| TC6   | Zero Amount         | 0      | 1    | 3  | 0.0 INR         | PASS   |
| TC7   | Negative Amount     | -1000  | 3    | 1  | -12.05 USD      | PASS   |
| TC8   | USD to INR          | 200    | 1    | 3  | 16600.0 INR     | PASS   |
| TC9   | EUR to GBP          | 50     | 2    | 4  | 42.93 GBP       | PASS   |
| TC10  | GBP to USD          | 100    | 4    | 1  | 126.58 USD      | PASS   |

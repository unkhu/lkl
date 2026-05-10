p=float(input("Enter Percentage: "))

if p<0 or p>100:
    print("Invalid Percentage")

elif p>=90:
    print("Your percentage is",p,"Grade: A+ Excellent")

elif p>=80:
    print("Your percentage is",p,"Grade: A Very Good")

elif p>=70:
    print("Your percentage is",p,"Grade: B Good")

elif p>=60:
    print("Your percentage is",p,"Grade: C Average")

elif p>=50:
    print("Your percentage is",p,"Grade: D Pass")

else:
    print("Your percentage is",p,"Grade: F Fail")

| Path No | Condition        | Output             |
| ------- | ---------------- | ------------------ |
| P1      | p < 0 or p > 100 | Invalid Percentage |
| P2      | p >= 90          | Grade A+ Excellent |
| P3      | 80 <= p < 90     | Grade A Very Good  |
| P4      | 70 <= p < 80     | Grade B Good       |
| P5      | 60 <= p < 70     | Grade C Average    |
| P6      | 50 <= p < 60     | Grade D Pass       |
| P7      | p < 50           | Grade F Fail       |


    
| TC ID | Input | Expected Output    | Status |
| ----- | ----- | ------------------ | ------ |
| TC1   | -5    | Invalid Percentage | PASS   |
| TC2   | 105   | Invalid Percentage | PASS   |
| TC3   | 95    | Grade A+ Excellent | PASS   |
| TC4   | 85    | Grade A Very Good  | PASS   |
| TC5   | 75    | Grade B Good       | PASS   |
| TC6   | 65    | Grade C Average    | PASS   |
| TC7   | 55    | Grade D Pass       | PASS   |
| TC8   | 30    | Grade F Fail       | PASS   |
| TC9   | 90    | Grade A+ Excellent | PASS   |
| TC10  | 50    | Grade D Pass       | PASS   |

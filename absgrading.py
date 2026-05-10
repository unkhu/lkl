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

name=input("What is your name")
print("Hello", name)
maths=float(input("Enter your maths mark :"))
english=float(input("Enter your english mark:"))
physics=float(input("Enter your physics mark:"))
average=(maths+english+physics)/3
print("Your average is:",average)
if average >=80:
  grade="A"
elif average >=70:
  grade="B"
elif average >=60:
  grade="C"
elif average >=50:
  grade="D"
else:
  grade="E"

print(Your grade is:", grade)

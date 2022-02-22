weight=float(input("enter the weight in KG: "))
height=float(input("enter the height in Centimeters: "))
BMI=weight/(height/100) ** 2 # 
print("BMI is", BMI)
if BMI <= 8.4:
    print("Under weight")
elif BMI >= 18.5 and BMI <= 24.9: # after collon 4 spaces for indentation
    print("Normal weight")
elif BMI >= 25 and BMI <= 29.9:
    print("Over wight")
elif BMI >= 30 and BMI <= 34.9:
    print("obesity - class 1")
elif BMI >= 35 and BMI <= 35.9:
    print("obesity - class 2")
else:
    print("obesity class 3")

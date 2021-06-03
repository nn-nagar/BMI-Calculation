def BMI(height, weight):
    bmi = weight/(height**2)
    return bmi
 
# Driver code
height = 1.79832
weight = 70
 
# calling the BMI function
bmi = BMI(height, weight)
print("The BMI is", format(bmi), "so ", end='')

if (bmi <= 18.4):
    print("underweight")
 
elif ( bmi >= 18.5 and bmi < 24.9):
    print("Normal weight")
 
elif ( bmi >= 24.9 and bmi < 30):
    print("overweight")
 
elif ( bmi >=30 and bmi < 34.9):
    print("Modarately obese")

elif ( bmi >=35 and bmi < 39.9):
    print("Severely obese")

elif ( bmi >=40):
    print("Severely obese")

else:
    print("Very Severely obese")
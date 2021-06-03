import pandas as pd


def BMI(height, weight):
    bmi = weight/(height**2)
    return bmi
 
# Driver code


# Height input
height = float(input("Please enter height in meters(m)"))
# Weight input
weight = float(input("Please enter Mass/Weight in Kilograms(Kg)"))
 
# calling the BMI function
bmi = BMI(height, weight)
print("The BMI is", format(bmi), "so ")

if (bmi <= 18.4):
	dict = {"bmi_category" : "underweight",
    "health_risk" : "Malnutrition risk", "bmi_range" : "<= 18.4" }
 
elif ( bmi >= 18.5 and bmi < 24.9):
	dict = {"bmi_category" : "Normal weight",
    "health_risk" : "Low risk",
    "bmi_range" : "18.5 - 24.9"}
 
elif ( bmi >= 24.9 and bmi < 30):
	dict = {"bmi_category" : "overweight",
    "health_risk" : "Enhanced risk",
    "bmi_range" : "25 - 29.9"}
 
elif ( bmi >=30 and bmi < 34.9):
	dict = {"bmi_category": "Modarately obese",
    "health_risk" : "Medium risk",
    "bmi_range" : "30 - 34.9"}

elif ( bmi >=35 and bmi < 39.9):
	dict = {"bmi_category" : "Severely obese",
    "health_risk" : "High risk",
    "bmi_range" : "35 - 39.9"}

elif ( bmi >=40):
	dict = {"bmi_category" : "Severely obese",
    "health_risk" : "Very high risk",
    "bmi_range" : ">= 40"}

else:
	print("Very Severely obese")
    

data = {
  		 "Height": height,
  
  		 "Weight": weight,
  
  		   "BMI" : bmi,
           
  "BMI Category" : dict["bmi_category"],
  
   "Health Risk" : dict["health_risk"],
   
   "BMI Range"   : dict["bmi_range"]
}

df = pd.DataFrame(data, index = ["Gender"])

print(df) 

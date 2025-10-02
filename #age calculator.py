#age calculator 

from datetime import datetime

year = input("what year were you born?: ")
if "in" in year:
    year = year.replace("in","").strip()
else:
    pass

try:
    year = int(year)
    age =  datetime - year
    if age <= 0 :
        print("boi aint no way boy")
    elif age >= 100:
        print ("what were the dinosaurs like")    
    else:
        print(f"you are {age}")
except ValueError: 
    print("year is invalid")
    

weight_lbs = int(input("weight (lbs): "))

weight_kgs = weight_lbs * 0.45

if weight_lbs >= 300:
    print("GYYYAAAATTTT")
elif weight_lbs <= 150:
    print("YOU NEED A BURGER")
else:
    print (f"this is your weight in kg {weight_kgs}.")




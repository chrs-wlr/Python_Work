#Mini Float Project

bill = float(input("Enter your bill amount?:$ "))
tip_percent = float(input("Enter your tip percentage?: "))

tip = bill * tip_percent/100
final_bill = bill + tip

print (round(final_bill,2))

#user friendly tips represent money and percentages with their
#correct symbols ie $ and %
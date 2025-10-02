# meal cost between groups

meal = float(input("Enter meal total: "))

party = float(input("how many in your party?: "))

FinalPay = float(round(meal/party,2))              

tip_confirmation = input("would you like to leave a tip? (yes or no): ")


if tip_confirmation == "yes":
    tip = float(input("input tip %: "))
    tip_amount = round(FinalPay *(tip/100), 2)
    total_with_tip = round(FinalPay + tip_amount,2)
    print(f"your total with tip will be {total_with_tip} ")
elif tip_confirmation == "no":
    print(f"Your split should be {FinalPay}. enjoy your meal")
else:
    print("plese put yes or no.")

    

    


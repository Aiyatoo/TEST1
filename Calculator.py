print("====Welcom to the Tip Calculator====")
bill=int(input("What was the total bill ?"))
tip=int(input("How much tip would you like to give? 10,12,15 "))
peopel=int(input("How many people to split the bill?"))
total_tip = tip/100
total_people=total_tip*2
total=(bill+total_people)/peopel
print("Each person should pay:",total,"$")
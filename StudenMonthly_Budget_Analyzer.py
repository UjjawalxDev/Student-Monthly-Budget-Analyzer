# Student Monthly Budget Analyzer



#Collect Input

student=input("Enter Your Name:")

Monthly_Income=float(input("Enetr Your Monthly Income:"))

food=float(input("Enter your food expenses:"))
travel=float(input("Enter Your travel expenses:"))
study_materials=float(input("Enter Your expenses:"))
mobile_internet=float(input("Enter Your Mobile/Internet Expenses:"))
other_expenses=float(input("Enter your other expenses:"))

#Calcuate total expenses

total_expenses=(food+travel+study_materials+mobile_internet+other_expenses)

#Calculate Remaining Balance

remaining_balance=Monthly_Income-total_expenses

#calculate percentages
if total_expenses > 0:
	food_percentage=(food/total_expenses)*100
	travel_percentage=(travel/total_expenses)*100
	study_percentage=(study_materials/total_expenses)*100
	mobile_percentage=(mobile_internet/total_expenses)*100
	other_percentage=(other_expenses/total_expenses)*100
else:
	food_percentage=0
	travel_percentage=0
	study_percentage=0
	mobile_percentage=0
	other_percentage=0


if Monthly_Income>0:
	savings_rate=(remaining_balance/Monthly_Income)*100
else:
	savings_report=0

# Display the report

print("========MONTHLY BUDGET REPORT======")
print("Student:", student)
print("Monthly Income:", Monthly_Income)
print("Total Expenses:", total_expenses)
print("Remaining Balance:", remaining_balance)
print("Food Expenses:", food, "(", food_percentage, "% )")
print("Travel Expenses:", travel, "(", travel_percentage, "% )")
print("Study Materials:", study_materials, "(", study_percentage, "% )")
print("Mobile/Internet Expenses:", mobile_internet, "(", mobile_percentage, "% )")
print("Other Expenses:", other_expenses, "(", other_percentage, "% )")
print("Savings Rate:", savings_rate if Monthly_Income > 0 else 0)

print("============================================")
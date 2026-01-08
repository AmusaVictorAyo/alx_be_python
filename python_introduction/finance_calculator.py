Monthly_Income = int(input("Enter your monthly income: ")) #Enter User Monthly Income
Monthly_Expenses = int(input("Enter your total monthly expenses: "))    #Enter total Monthly Expenses
Monthly_Savings =  Monthly_Income - Monthly_Expenses  #total User Savings
Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)
print(f"Your monthly savings are ${Monthly_Savings}.")
print(f"Projected savings after one year, with interest, is: ${round(Projected_Savings)}.")

#INSTRUCTIONS: run the program, it will request and print the information to the command line
money = eval(raw_input("How much money (in dollars) is in your lunch account? "))
date = eval(raw_input("What day of the month is it today? "))
daysLeft = eval(raw_input("How many days are in this month? "))
allowedExpense = money/(daysLeft-date)
print("You can spend ${0:0.2f} each day for the rest of the month".format(allowedExpense))

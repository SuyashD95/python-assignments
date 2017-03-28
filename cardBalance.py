""" 
Q9- Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly
payment required by the credit card company each month.  

The following variables contain values as described below: 
1. balance - the outstanding balance on the credit card 
2. annualInterestRate - annual interest rate as a decimal 
3. monthlyPaymentRate - minimum monthly payment rate as a decimal 

For each month, calculate statements on the monthly payment and remaining balance, and print to screen something of the format: 
Month: 1 
Minimum monthly payment: 96.0
Remaining balance: 4784.0  

Be sure to print out no more than two decimal digits of accuracy - so print  
Remaining balance: 813.41  

instead of 
Remaining balance: 813.4141998135   

Finally, print out the total amount paid that year and the remaining balance at the end of the year in the format: 
Total paid: 96.0 
Remaining balance: 4784.0  

A summary of the required math is found below: 

Monthly interest rate= (Annual interest rate) / 12.0 
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""

def cardBalance( balance, annual_interest_rate, monthly_payment_rate ):

	"""
	EQUATIONS TO BE USED:

	1. monthly_interest_rate = annual_interest_rate / 12.0

	2. minimum_monthly_payment = monthly_payment_rate * balance
	
	3. monthly_unpaid_balance = balance - minimum_monthly_payment
	
	4. updated_balance_month = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
	"""

	# print("Balance: " + str( balance ) )
	# print("Annual Interest Rate: " + str( annual_interest_rate ) )
	# print("Monthly Payment Rate: " + str( monthly_payment_rate ) )
	
	for month in range( 1, 13 ):

		# Output format for each month
		print("\nMonth: " + str( month ) )
		print("Minimum monthly payment: " ) # + str( minimum_monthly_payment ) )
		print("Remaining balance: " ) # + str( balance ) )

	# Output format for the whole year
	print("\nTotal paid: " ) # + str( total_paid ) )
	print("Remaining balance: " ) # + str( balance ) )


print( "NOTE TO REMEMBER: Both the ANNUAL INTEREST RATE and MONTHLY PAYMENT RATE needs to be taken as a DECIMAL..." )
print( "For example:-\n\nIf Annual Interest Rate is 8%, then, the user needs to enter it as:\n\n0.08 which is the result of 8 / 100\n")

balance = input( "Enter the outstanding balance of the credit card: ")
annual_interest_rate = input( "Enter the annual interest rate: " )
monthly_payment_rate = input( "Enter the monthly payment rate: " )

cardBalance( balance, annual_interest_rate, monthly_payment_rate )

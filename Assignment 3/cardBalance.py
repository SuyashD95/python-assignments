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

# Function STARTS
def cardBalance( balance, annual_interest_rate, monthly_payment_rate ):

	"""
	EQUATIONS TO BE USED:

	1. monthly_interest_rate = annual_interest_rate / 12.0

	2. minimum_monthly_payment = monthly_payment_rate * balance

	3. monthly_unpaid_balance = balance - minimum_monthly_payment

	4. updated_balance_month = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
	"""
	balance = int( balance )
	annual_interest_rate = float( annual_interest_rate )
	monthly_payment_rate = float( monthly_payment_rate )
        
	monthly_interest_rate = annual_interest_rate / 12.0
	total_paid = 0

	for month in range( 1, 13 ):

		# Calculating the minimum monthly payment and adding to the total amount to be paid in a course of a year
		minimum_monthly_payment = monthly_payment_rate * balance
		total_paid += minimum_monthly_payment

		# Updating the balance after the monthly payments has been paid by the user
		monthly_unpaid_balance = balance - minimum_monthly_payment
		updated_balance_month = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
		balance = updated_balance_month

		# This statement is used to set the precision of a floating point number and converting it into string. (Used in Python 3.6)
		# Syntax: f"{FLOATING_POINT_VARIABLE:.PRECISIONf}"
		# Example: f"{minimum_monthly_payment:.2f}"

		# To achieve the same functionality in Python < 3 (e.g 2.7), use the following method:
		# Syntax: "%.PRECISIONf" % FLOATING_POINT_VARIABLE
		# Example: "%.2f" % minimum_monthly_payment

		# Output format for each month
		print( "\nMonth: " + str( month ) )
		print( "Minimum monthly payment: " + f"{minimum_monthly_payment:.2f}" )
		print( "Remaining balance: " + f"{balance:.2f}" )

	# Output format for the whole year
	print( "\nTotal paid: " + f"{total_paid:.2f}" )
	print( "Remaining balance: " + f"{balance:.2f}" )

# Function ENDS

print( "NOTE TO REMEMBER: Both the ANNUAL INTEREST RATE and MONTHLY PAYMENT RATE needs to be taken as a DECIMAL..." )
print( "For example:-\n\nIf Annual Interest Rate is 8%, then, the user needs to enter it as:\n\n0.08 which is the result of 8 / 100\n" )

balance = input( "Enter the outstanding balance of the credit card: " )
annual_interest_rate = input( "Enter the annual interest rate: " )
monthly_payment_rate = input( "Enter the monthly payment rate: " )

cardBalance( balance, annual_interest_rate, monthly_payment_rate )

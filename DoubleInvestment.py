#Program to double the investment
#DoubleInvestment.py

def main():

	#Declare variables
	rateOfInterest = 0.0
	initialAmount = 0
	targetAmount = 0
	year = 0

	initialAmount = eval(input("Enter initial amount: "))
	rateOfInterest = eval(input("Enter interest rate: "))

	'''
	year = calculateInterest(intitialAmount, rateOfInterest)
	'''

	targetAmount = 2*initialAmount

	balance = initialAmount #1000

	while (balance < targetAmount):
		year += 1
		interestAmount = balance * rateOfInterest/100

		#balance += interestAmount
		balance = balance + interestAmount

		#Allocate 4 spaces for year
		#Allocate 10 spaces for balance
		print("%4d%10.2f" %(year,balance))

	print("The investment doubles after %d years" %year)

#Call main
main()
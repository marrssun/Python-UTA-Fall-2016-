crsr.execute("INSERT INTO WeatherTable Values (4,'Dallas', 'USA',4,27.6,346.0)")

crsr.execute("INSERT INTO WeatherTable Values (5, 'London', 'United Kingdom',1,4.2,207.7)")

crsr.execute("INSERT INTO WeatherTable Values (6, 'London', 'United Kingdom',2,8.3,169.6)")

crsr.execute("INSERT INTO WeatherTable Values (7, 'London', 'United Kingdom',3,15.7,157.0)")

crsr.execute("INSERT INTO WeatherTable Values (8, 'London', 'United Kingdom',4,10.4,218.5)")

crsr.execute("INSERT INTO WeatherTable Values (9, 'Cairo', 'Egypt',1,13.6,16.5)")

crsr.execute("INSERT INTO WeatherTable Values (10, 'Cairo', 'Egypt',2,20.7,6.5)")

crsr.execute("INSERT INTO WeatherTable Values (11, 'Cairo', 'Egypt',3,27.7,0.1)")

crsr.execute("INSERT INTO WeatherTable Values (12, 'Cairo', 'Egypt',4,22.2,4.5)")

cnxn.commit()

except lite.OperationalError as dbex:
	print("\nError\n",dbex)
else:
	crsr.xecute(SELECT_LONDON)
	output = crsr.fetchall()
	displayLondon(output,crsr)
	#crsr.execute()
	if(output == []):
		print("\nNo records found.")
	else:
		crsr.execute(SELECT_SUMMER)
		summerOutput = crsr.fetchall()

display2B(summerOutput,crsr)

crsr.execute(SELECT_LESS_20) 
	
	lessTwenty = crsr.fetchall()

crsr.execute(SELECT_MORE_20) 
	
	moreTwenty = crsr.fetchall()
	display2D(moreTwenty)
	crsr.execute(SELECT_MAX)
	maxRecord = crsr.fetchall()
	display2E(maxRecord)

crsr.execute(SELECT_DESCENDING)
	
	descending = crsr.fetchall()
	display2F(descending)

crsr.execute(SELECT_Cairo_SUM)
	totalRainfall = crsr.fetchall()
	display2G(totalRainfall)

	LastList = []
	crsr.execute(SELECT_L1)
	output1 = crsr.fetchall()

	crsr.execute(SELECT_L2)
	output2 = crsr.fetchall()

display2H(output1,output2,totalRainfall)

def display2H(output1,output2,totalRainfall):
	print()
	print("\n2h)")
	print("City\tSeason\tRainfall\n")
	for record in output1:
		print("%s\t%d\t%.2f" %(record[0], record[1], record[2]))

	for record in output2:
		print("%s\t%d\t%.2f" %(record[0], record[1], record[2]))

print("Cairo\tEgypt\t\t\t%.2f" %totalRainfall[0])
print()

'''
	Something code

'''

def displayLondon(output,crsr):
	print()
	print()
	print("\n2a)")
	print("ID\tCity\tCountry\t\tSeason\tTemperature\tRainfall")
	print()

	for record in output:
		print("%d\t%s\t%s\t%d\t%f" %(record[0], record[1], record[2],record[3], record[4], record[5]),end='\t')
		print()


main()
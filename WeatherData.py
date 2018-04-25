import sqlite3 as lite
import sys 

DATABASE_FILE = 'weather.db'



SELECT_WEATHER = "SELECT * FROM WeatherTable"
SELECT_LONDON = "SELECT * FROM WeatherTable WHERE City = 'London' "
SELECT_SUMMER = "SELECT * FROM WeatherTable WHERE SEASON = 2"
SELECT_LESS_20 = "SELECT City, Country, Season FROM WeatherTable WHERE (Temperature < 20)"
SELECT_MORE_20 = "SELECT City, Country, Season FROM WeatherTable WHERE (Temperature > 20) AND (RAINFALL <10)"


SELECT_MAX = "SELECT MAX (Rainfall) FROM WeatherTable"
SELECT_DESCENDING = "SELECT City,Season,Rainfall FROM WeatherTable ORDER BY Rainfall DESC"


SELECT_CAIRO_SUM = "SELECT sum(Rainfall) FROM WeatherTable WHERE City = 'Cairo'"
SELECT_L1 = "SELECT City,Country,sum(Rainfall) FROM WeatherTable WHERE City = 'Dallas'"
SELECT_L2 = "SELECT City,Country,sum(Rainfall) FROM WeatherTable WHERE City = 'London'"

def main():
	try:
		cnxn = lite.connect('weather.db')
		print("Database connection successful")

	except lite.OperationalError as dbex:
		print("Error",dbex)
		
	else:

		crsr = cnxn.cursor()
		#crsr.execute(SELECT_LONDON)
		#output = crsr.fetchall()
		#a
		output = ExecuteLondon(crsr,SELECT_LONDON)
		
		if(output == []):
			print("No records")
		else:
			DisplayLondon(output,crsr) #a
		#b	
		output = ExecuteSummer(crsr,SELECT_SUMMER)
		if(output == []):
			print("No records")
		else:
			DisplaySummer(output,crsr) 
		#c
		output = ExecuteQC(crsr,SELECT_LESS_20)
		
		if(output == []):
			print("No records")
		else:
			DisplayQC(output,crsr)

		#d
		output = ExecuteQD(crsr,SELECT_MORE_20)
		
		if(output == []):
			print("No records")
		else:
			DisplayQD(output,crsr)
		#e
		output = ExecuteQE(crsr,SELECT_MAX)
		
		if(output == []):
			print("No records")
		else:
			DisplayQE(output,crsr)
		#f
		output = ExecuteQF(crsr,SELECT_DESCENDING)
		
		if(output == []):
			print("No records")
		else:
			DisplayQF(output,crsr)


#a 
def ExecuteLondon(crsr,query):
	
	crsr.execute(query)
	return crsr.fetchall()

		
#a
def DisplayLondon(output,crsr):
	print("\nQ2-A")
	print("ID\tCity\tCountry\t\tSeason\tTemperature\tRainfall")
	print()
	for record in output:
		print("%d\t%s\t%s\t%d\t%f\t%f"%(record[0],record[1],record[2],record[3],record[4],record[5]))

#b
def ExecuteSummer(crsr,query):
	
	crsr.execute(query)
	return crsr.fetchall()

		
#b
def DisplaySummer(output,crsr):
	print("\nQ2-B")
	print("ID\tCity\tCountry\t\tSeason\tTemperature\tRainfall")
	print()
	for record in output:
		print("%d\t%s\t%s\t%d\t%f\t%f"%(record[0],record[1],record[2],record[3],record[4],record[5]))

#c
def ExecuteQC(crsr,query):
	
	crsr.execute(query)
	return crsr.fetchall()

		
#c
def DisplayQC(output,crsr):
	print("\nQ2-C")
	print("%20s%20s%6s" %("City","Country","Season"))
	print()
	for record in output:
		print("%20s%20s%3d" %(record[0],record[1],record[2]))

#d
def ExecuteQD(crsr,query):
	
	crsr.execute(query)
	return crsr.fetchall()		
#d
def DisplayQD(output,crsr):
	print("\nQ2-D")
	print("%20s%20s%6s" %("City","Country","Season"))
	print()
	for record in output:
		print("%20s%20s%3d" %(record[0],record[1],record[2]))

#e
def ExecuteQE(crsr,query):
	
	crsr.execute(query)
	return crsr.fetchall()

def DisplayQE(output,query):
	print("\nQ2-E")
	for record in output:
		print("Max Rainfall: %.3f\n" %output[0])
#f
def ExecuteQF(crsr,query):
	
	crsr.execute(query)
	return crsr.fetchall()		

def DisplayQF(output,crsr):
	print("\nQ2-F")
	print("%20s%f%d"%("City","Season","Rainfall"))
	print()
	for record in output:
		print("%20s%f%d"%(record[0],record[1],record[2]))


main()
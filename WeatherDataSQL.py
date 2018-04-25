import sqlite3 as lite
import sys


try:


	cnxn = lite.connect('weather.db') #connecting to weather.db & returns an object of type, .db exisits in the current working directory 
	print("Databse opened successfully")
	crsr = cnxn.cursor() #cursor- is the workhorse of database processing supports the excute() method
	crsr.execute("DROP TABLE IF EXISTS WeatherTable") #takes a sql statement, as a string, and executes it
	crsr.execute('''CREATE TABLE WeatherTable(
		ID INT NOT NULL, #holds integer values
		City TEXT(20)NOT NULL, #holds string values, delimited w/quotes
		Country TEXT(20)NOT NULL,
		Season INT NOT NULL, 
		Temperature REAL, #holds floating-point values 
		Rainfall REAL,
		PRIMARY KEY (ID));''')




	print("Table Created successfully")


	crsr.execute("INSERT INTO WeatherTable VALUES (1, 'Dallas', 'USA',1,24.8,5.9) ") #Insert- used to insert new record into database.
	crsr.execute("INSERT INTO WeatherTable VALUES (2, 'Dallas', 'USA',2,28.4,16.2) ") # Insert- is passed as an input to the execute() function 
	crsr.execute("INSERT INTO WeatherTable VALUES (3, 'Dallas', 'USA',3,27.9,1549.4) ") #ID, City, Country, Season, Temp, Rainfall
	crsr.execute("INSERT INTO WeatherTable Values (4, 'Dallas', 'USA',4,27.6,346.0)")
	crsr.execute("INSERT INTO WeatherTable Values (5, 'London', 'United Kingdom',1,4.2,207.7)")
	crsr.execute("INSERT INTO WeatherTable Values (6, 'London', 'United Kingdom',2,8.3,169.6)")
	crsr.execute("INSERT INTO WeatherTable Values (7, 'London', 'United Kingdom',3,15.7,157.0)")
	crsr.execute("INSERT INTO WeatherTable Values (8, 'London', 'United Kingdom',4,10.4,218.5)")
	crsr.execute("INSERT INTO WeatherTable Values (9, 'Cairo', 'Egypt',1,13.6,16.5)")
	crsr.execute("INSERT INTO WeatherTable Values (10, 'Cairo', 'Egypt',2,20.7,6.5)")
	crsr.execute("INSERT INTO WeatherTable Values (11, 'Cairo', 'Egypt',3,27.7,0.1)")
	crsr.execute("INSERT INTO WeatherTable Values (12, 'Cairo', 'Egypt',4,22.2,4.5)")


	cnxn.commit()
	cnxn.close()
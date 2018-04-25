#Program to compute distance between
#Two points in a plane

import Point
import math

def main():

	#Create two points
	pointA = Point.Point() #Initializes x and y of pA to zeros

	#Intializes x and y of pointB to 3 and 4 respectively
	pointB = Point.Point(3,4) 

	#Distance between pointA and pointB
	dist = math.sqrt((pointB.getX()-pointA.getX())**2 +
		(pointB.getY()-pointA.getY())**2)

	print("Distance between A and B: ", dist)

	#Create two points in plane
	pointC = Point.Point(2,3)
	pointD = Point.Point(2,3)

	print(pointC)
	print(pointD)
	
	if(pointC == pointD):
		print("Points c and d are same")
	else:
		print("Points c and d are different")


#Call main
main()
#Class Point

class Point:
	'Class that represents a point in plane'

	def __init__ (self, xcoord=0, ycoord=0):
		'This function initializes x and y coordinates'
		self.__x = xcoord
		self.__y = ycoord

	#Accessor and mutator methods
	#Set method
	def setX(self, xcoord):
		'Method to set x to xcoord'
		self.__x = xcoord

	def setY(self, ycoord):
		self.__y = ycoord

	#Get methods
	def getX(self):
		return self.__x

	def getY(self):
		return self.__y

	def __eq__(self,otherPoint):
		if( (self.getX() == otherPoint.getX()) and
			self.getY() == otherPoint.getY()):
			return True

		return False 
	'''
	def __str__(self):
		return str.format("x = %d\ny = %d\n"
		%(self.getX(),self.getY()) )
	'''
	def __repr__(self):
		return 'Point({},{})'.format(self.getX(),self.getY())
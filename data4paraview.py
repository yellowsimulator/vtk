"""
Extrat relevent data from filename: data4paraview.
step one:
---------
The function readpoints() extracts
the latitude, longitude and depth of the earthquake and store it in
x,y,z, which is stored into a vtk array

The function readVector() extracts
the latitude, longitude and depth of the earthquake and store it in
x,y,z, which is stored into a vtk vector

step two:
---------
The function readMagnitude() extracts the magnitude of the earthquake
and return an array containing the magniture of the array
"""

def readPoints(filename):
	#create an array of points
	points = vtkPoints()
	myfile = open(filename,'r')
	#ignore the first line containing the name of the elemements
	line = myfile.readline()
	
	# loop over line to extract latitude longitude and depth
	lines = myfile.readlines()
	for line in lines:
		words = line.split(',')
		x,y,z = float(words[4]),float(words[5]),float(words[6])
		# insert points into the point array
		points.InsertNextPoint(x,y,z)
	return points
		
	
	


def readVectors(filename):
	#create a double array which represent the vector
	vectors = vtkDoubleArray()
	
	# define number of elements
	vectors.SetNumberOfComponents(3)
	
	myfile = open(filename,'r')
	#ignore the first line containing the name of the elemements
	line = myfile.readline()
	
	# loop over line to extract latitude longitude and depth
	lines = myfile.readlines()
	for line in lines:
		words = line.split(',')
		x,y,z = float(words[4]),float(words[5]),float(words[6])
		# insert points into the point array
		vectors.InsertNextTuplet3(x,y,z)
	return vectors
		

def readMagnitude(filename):
	pointArray=[]
	myfile = open(filename,'r')
	#ignore the first line containing the name of the elemements
	line = myfile.readline()
	
	# loop over line to extract latitude longitude and depth
	lines = myfile.readlines()
	for line in lines:
		words = line.split(',')
		p = float(words[11])
		pointArray.append(p)
	return pointArray
	
print readMagnitude('data4paraview.txt')

	


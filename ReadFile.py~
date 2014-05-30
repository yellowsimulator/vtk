"""
A function that reads points from file
and create a vtk point array object and a vtk vector object ?
"""

import vtk


def ReadPoints(filename):
	#create a vtk array to store points coordinate
	points = vtk.vtkPoints()
	myfile = open(filename,'r')
	# read the first line
	line = myfile.readline()
	
	#loop over the line and assign coordinates x,y,z to points
	lines = myfile.readlines()
	for line in lines:
		data = line.split()
		x,y,z = float(data[0]),float(data[1]),float(data[2])
		
		# insert x,y,z into vtk point array
		points.InsertNextPoint(x,y,z)
		
	return points
		
		
		
def ReadVectors(filename):
	#create a vtk double array which represents the vectors
	vectors = vtk.vtkDoubleArray()
	
	# define number of elements
	vectors.SetNumberOfComponents(3)
	myfile = open(filename,'r')
	# read the first line
	line = myfile.readline()
	
	#loop over the line and assign coordinates x,y,z to points
	lines = myfile.readlines()
	for line in lines:
		data = line.split()
		x,y,z = float(data[0]),float(data[1]),float(data[2])
		
		# insert x,y,z into vtk point array
		vectors.InsertNextTuple3(x,y,z)	
		
	return vectors
		
		
"""		
f = sys.argv[1]
myvtkArray = ReadPoints(f)
myvtkvector = ReadVectors(f)
print myvtkArray
print myvtkvector
"""



"""
this function creates a dictionary with parameters:
iteration, rms, data_rms, parameters as properties.
we want to access the property p at iteration i as:

Access[p][i] = value, whre value is the value of property p at iteration i
"""
import sys

def get_property(filename):
	getMyProperty = {}
	myfile = open(filename,'r')
	newfile = open('f.dat','w')
	# skeep the first line
	myfile.readline()
	
	# store property on second line in an array named properties
	properties = myfile.readline().split()
	
	#create inner dictionary
	for p in properties:
		getMyProperty[p] = {}
		
	# arrage file
	
	
	# fill in the values now
	myfile.readline()
	"""
	for line in myfile:
		words = line.split()
		if isinstance(int(words[0]),int):
			
			iterationNumber = int(words[0])
			propertyvalues = words[1:]
			for p,v in zip(properties,propertyvalues):
				if v!='No':
					getMyProperty[p][iterationNumber] = v
				
	return getMyProperty
	"""

	for line in myfile:
		if 'No' in line:
			del(line) # delete line starting with string No
			k = myfile.next() #delete next line
			del(k)
			
		else:
			newfile.write(line)
			
			

		
		
		

filename = sys.argv[1]

print get_property(filename)



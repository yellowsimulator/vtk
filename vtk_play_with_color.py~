"""
 Learn to play with color with vtk
"""

from vtk import *

# create a source: a cylinder
cylinder = vtkCylinderSource()
cylinder.SetResolution(8)
cylinder.SetHeight(4)
cylinder.SetRadius(4)


#create a mapper
cylinderMapper = vtkPolyDataMapper()
cylinderMapper.SetInput(cylinder.GetOutput())

# create an actor and take Mapper as input, set actor color property
# actors are defined in terms of Mappers, property and transform object
cylinderActor = vtkActor()
cylinderActor.SetMapper(cylinderMapper)
cylinderActor.GetProperty().SetColor(0.0,1.0,1.0)
################################################################

#Create a second source: a cone
cone = vtkConeSource()
cone.SetResolution(12)
cone.SetHeight(12)
cone.SetRadius(3)
cone.SetCenter(5,0,0)

# Create a mapper for the cone
coneMapper = vtkPolyDataMapper()
coneMapper.SetInputConnection(cone.GetOutputPort())

# create an actor for cone, give Mapper as argument, set property
# Actors are defines in terms of Mapper, property andtransform objects
coneActor = vtkActor()
coneActor.SetMapper(coneMapper)
coneActor.GetProperty().SetColor(1.0,0.0,1.0)
####################################################

# create a renderer and assign the actor to the renderer
ren = vtkRenderer()
ren.AddActor(cylinderActor)
ren.AddActor(coneActor)
ren.SetBackground(0.6,0.6,0.7)

# create a redering window, put a renderer in it and set name and size
renWin = vtkRenderWindow()
renWin.AddRenderer(ren)
renWin.SetWindowName("Cone & Cylinder having fun")
renWin.SetSize(500,500)

# interaction with window
iren = vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# initialize and start the application
iren.Initialize()
iren.Start()





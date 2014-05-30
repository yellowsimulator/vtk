"""
Read the file name teapot.obj and generate 3D Image from it

"""
from vtk import *
# read teapot.obj file, which is the source
obj = vtkOBJReader()
obj.SetFileName("teapot.obj")


# define mapper
objectMapper = vtkPolyDataMapper()
objectMapper.SetInputConnection(obj.GetOutputPort())



#create a color mapper function
# create a color transfer function
"""
colorTransferFunction = vtkColorTransferFunction()
colorTransferFunction.AddRGBPoint(5.0,0.0,0.0, 1.0)
colorTransferFunction.AddRGBPoint(10.0,0.0,1.0, 1.0)
colorTransferFunction.AddRGBPoint(15.0,0.0,1.0, 0.0)
colorTransferFunction.AddRGBPoint(20.0,0.0,1.0, 0.0)
colorTransferFunction.AddRGBPoint(25.0,1.0,0.0, 0.0)
colorTransferFunction.AddRGBPoint(20.0,1.0,0.0, 1.0)
objectMapper.SetLookupTable(colorTransferFunction)
"""

# define actor and give mapper as input, and set property (color, shading...)
objectActor = vtkActor()
objectActor.SetMapper(objectMapper)
objectActor.GetProperty().SetColor(0.2,0.6,0.6)

# define renderer
ren = vtkRenderer()
ren.AddActor(objectActor)
ren.SetBackground(0.6,0.6,0.7)

# add rendering window

renWin = vtkRenderWindow()
renWin.AddRenderer(ren)
renWin.SetWindowName("Teapot")
renWin.SetSize(500,500)

# make sure we can interact with the actor
iren = vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
iren.Initialize()
iren.Start()








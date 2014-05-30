"""
Read coordnate of pints from file: file names: file1.dat and file2.dat
visualise the result
"""
import sys
import vtk
from earthquake_data4paraview import *
###################################################################################



#######################################################################################

#read the data into a vtkPolyData using the function ReadFile()
data = vtk.vtkUnstructuredGrid()

# read arguments
data.SetPoints(readPoints(sys.argv[1]))
data.GetPointData().SetVectors(readVectors(sys.argv[1]))



# put sphere at each points of the data set
ball = vtk.vtkSphereSource()
radius = readMagnitude(sys.argv[1])
for r in radius:
	ball.SetRadius((r/50.))
ball.SetThetaResolution(12)
ball.SetPhiResolution(12)

# need to understand this better 
ballGlyph = vtk.vtkGlyph3D()
ballGlyph.SetInput(data)
ballGlyph.SetSourceConnection(ball.GetOutputPort())

# maper for ball
ballMapper = vtk.vtkPolyDataMapper()
ballMapper.SetInputConnection(ballGlyph.GetOutputPort())

# actor for ball
ballActor = vtk.vtkActor()
ballActor.SetMapper(ballMapper)
ballActor.GetProperty().SetColor(0.8,0.4,0.4)


# create arrow
arrow = vtk.vtkArrowSource()
arrow.SetTipRadius(2.)
arrow.SetShaftRadius(0.075)

# Glyph for arrow
arrowGlyph = vtk.vtkGlyph3D()
arrowGlyph.SetInput(data)
arrowGlyph.SetSourceConnection(arrow.GetOutputPort()) # I put arrowGlyph instead of arrow----> I got segmentation fault
arrowGlyph.SetScaleFactor(0.2)

# create mapper for arrow
arrowMapper = vtk.vtkPolyDataMapper()
arrowMapper.SetInputConnection(arrowGlyph.GetOutputPort())

# create actor for arrow
arrowActor = vtk.vtkActor()
arrowActor.SetMapper(arrowMapper)
arrowActor.GetProperty().SetColor(0.9,0.9,0.1)


# create a renderer and associate the renderer to ballActor and arrowActor
ren = vtk.vtkRenderer()
ren.AddActor(ballActor)
ren.AddActor(arrowActor)
ren.SetBackground(0.4,0.4,0.6)

# create rendering window add a renderer in the window, set the size
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
renWin.SetWindowName("Earthquacks")
renWin.SetSize(500,500)

# make sure we can interact with the application. Initialize and start
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
iren.Initialize()
iren.Start()    ### If Start is written start then now output in generated




"""
Render a text using vtk. Let the user interact with the text
"""


import vtk

# create a text source and set the text
text = vtk.vtkTextSource()
text.SetText(" MAMAMIYA ")
#text.SetForegroundColor(0.6,0.2,0.2)

# create a mapper and set the Text source as input
textMapper = vtk.vtkPolyDataMapper()
textMapper.SetInputConnection(text.GetOutputPort())
#textMapper.SetInput(text.GetOutput())

# create an actor and set the mapper as input
textActor = vtk.vtkActor()
textActor.SetMapper(textMapper)

# create a renderer()
ren = vtk.vtkRenderer()

# assign the actor to the renderer
ren.AddActor(textActor)

# create a redering window
renWin = vtk.vtkRenderWindow()

# add the renderer to the window
renWin.AddRenderer(ren)

# set the name of the window
renWin.SetWindowName("My Window")

# Interact with the application
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# initialize and start the application
iren.Initialize()
renWin.Render()
iren.Start()



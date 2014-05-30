import vtk
# create a rendering window and render
ren = vtk.vtkRenderer()  # create a renderer
renWin = vtk.vtkRenderWindow() # create a rendering window
renWin.AddRenderer(ren)        # add the renderer to the rendering window
renWin.SetWindowName(" Cylinder ") # set he name of the window
renWin.SetSize(800,800)


#create a rendering window interacter
iren = vtk.vtkRenderWindowInteractor() 
iren.SetRenderWindow(renWin)

# create source

source = vtk.vtkCylinderSource()
source.SetCenter(0,0,0)
source.SetRadius(5.0)
source.SetHeight(7.0)
source.SetResolution(100.0)



#mapper
mapper = vtk.vtkPolyDataMapper()
#mapper.SetInput(source.GetOutput())
mapper.SetInputConnection(source.GetOutputPort())

#actor
actor = vtk.vtkActor()
actor.SetMapper(mapper)

#assign actor to the renderer
ren.AddActor(actor)

# unable user interaction
iren.Initialize() # initialise the application
renWin.Render()
iren.Start() # start the application


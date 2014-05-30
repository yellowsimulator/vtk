#! /usr/bin/env python
from array import *
from vtk import *
 
def create_points(array):
    """Create vtkPoints from double array"""
    vtk_points = vtkPoints()
    double_array = vtkDoubleArray()
    double_array.SetVoidArray(array, len(array), 1)
    double_array.SetNumberOfComponents(3)
    vtk_points.SetData(double_array)
    return vtk_points
 
def create_cells(array):
    """Create a vtkCellArray from long array"""
    vtk_cells = vtkCellArray()
    vtk_id_array = vtkIdTypeArray()
    vtk_id_array.SetVoidArray(array, len(array), 1)
    vtk_cells.SetCells(len(array)/4, vtk_id_array)
    return vtk_cells
 
def vtk_to_array(vtk_array):
    at = vtk_array.GetDataType()
    if at == 11:
        #vtkDoubleArray
        pt='d'
    elif at == 12:
        #vtkIdTypeArray
        pt='l'
    #this is slow. numpy.zeros would be faster.
    r = array(pt, [0]*vtk_array.GetSize())
    vtk_array.ExportToVoidPointer(r)
    return r
 
#Create polydata
points = array('d', [0,0,0,1,0,0,1,1,0,1,1,1])
triangles = array('l', [3 ,0,1,2, 3, 0,1,3])
polydata = vtkPolyData()
polydata.SetPoints(create_points(points))
polydata.SetPolys(create_cells(triangles))
 
#Save it
writer = vtkXMLPolyDataWriter()
writer.SetFileName("zob.vtp")
writer.SetInput(polydata)
writer.Write()
 
#Read it
reader = vtkXMLPolyDataReader()
reader.SetFileName("zob.vtp")
reader.Update()
polydata = reader.GetOutput()
 
#Display arrays
print vtk_to_array(polydata.GetPoints().GetData())
print vtk_to_array(polydata.GetPolys().GetData())

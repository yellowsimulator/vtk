from numpy import *

try:
    from enthought.mayavi.mlab import *
except ImportError:
    from mayavi.mlab import *
   
#from enthought.mayavi.mlab import *
# this creates a 3D grid which is ranges from -100 to 100 in all
# coordinates, with intersections at every 20th value
# (-100, -80, -60, ...). See 'help mgrid' for details.
x,y,z = mgrid[-100.:101.:20., -100.:101.:20., -100.:101.:20.]
# We will now store the coordinates of our charge as a
# vector. All vectors in Python should be stored as arrays.
# Note that we are placing this charge in between the grid points.
# This is to get the best possible symmetry in this specific field
# If you place the charge _on_ the grid, you get a division of zero
# when calculating the E-field.
qpos = array([10.,10.,10.])
# the magnitude of our charge. This could be any number
# at the moment.
qcharge = 1.0
# Create a grid for the electric field. This has the size of
# x,y and z, but all the values are now set to zero.
Ex, Ey, Ez = x*0, y*0, z*0
 
# Calculate the x, y and z distance to the charge at every point in the grid:
rx = x - qpos[0]
ry = y - qpos[1]
rz = z - qpos[2]
 
# Calculate the distance at every point in the grid:
r = sqrt(rx**2 + ry**2 + rz**2)
 
# Calculate the field for each component at every point in the grid:
Ex = (qcharge / r**2) * (rx / r)
Ey = (qcharge / r**2) * (ry / r)
Ez = (qcharge / r**2) * (rz / r)
 
# Draw the vector field in 3D
quiver3d(x,y,z,Ex,Ey,Ez)

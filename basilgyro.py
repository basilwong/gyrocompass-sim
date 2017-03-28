from visual import *

##constants
BASE_POSITION = (0,-12.1 - 1.5,0)
BASE_AXIS = (0,1,0)
BASE_SIZE = (1.5, 1.5, 1.5)

ROD_POSITION = (0,0,0)
ROD_AXIS = (0.3,0,0)
ROD_RADIUS = 10

GYRO_POSITION = (-11,0,0)
GYRO_AXIS = (22,0,0)
GYRO_RADIUS = 0.3

IRING_POSITION = (0,0,0)
IRING_AXIS = (0,1,0)
IRING_RADIUS = 11.1
IRING_THICKNESS = 0.1
IRING_COLOUR = (0.9,0.5,6)

ORING_POSITION = (0,0,0)
ORING_AXIS = (0,0,1)
ORING_RADIUS = 12
ORING_THICKNESS = 0.1
ORING_COLOUR =(0.4,0.1,0.3)

f1 = frame()    ## frame containing rod and gyro



base = pyramid(pos = BASE_POSITION, axis = BASE_AXIS, size = BASE_SIZE) ## create the suppport for the outer ring 
rod = cylinder(frame = f1, pos= ROD_POSITION, axis= ROD_AXIS , radius= ROD_RADIUS) #Inner Rotating Circle
gyro = cylinder(frame = f1, pos= GYRO_POSITION, axis= GYRO_AXIS, radius= GYRO_RADIUS) #Circle Supports
IRING = ring(pos = IRING_POSITION , axis = IRING_AXIS, radius = IRING_RADIUS, thickness = IRING_THICKNESS, color = IRING_COLOUR) #XZ Plane Ring
ORING = ring(pos = ORING_POSITION, axis = ORING_AXIS, radius = ORING_RADIUS, thickness = ORING_THICKNESS, color = ORING_COLOUR ) ## this is the outer ring, might be part of a frame later? (Y- Plane ring)


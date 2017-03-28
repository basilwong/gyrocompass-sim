from visual import *
import wx



##constants
BASE_POSITION = (0,-12.1 - 1.5,0)
BASE_AXIS = (0,1,0)
BASE_SIZE = (1.5, 1.5, 1.5)

ROD_POSITION = (-11,0,0)
ROD_AXIS = (22,0,0)
ROD_RADIUS = 0.3

GYRO_POSITION = (0,0,0)
GYRO_AXIS = (0.3,0,0)
GYRO_RADIUS = 10

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

WINDOW_POSX = 0;
WINDOW_POSY = 0;
WINDOW_HEIGHT = 1000;
WINDOW_WIDTH = 1000;


##setup window and displays
w = window(title = 'gyrocompass',x=WINDOW_POSX,y=WINDOW_POSY,width=WINDOW_WIDTH,height=WINDOW_HEIGHT)
scene1 = display(window = w, title = 'Gyrocompass up close', x=w.x,y=w.y,width=w.width/2,height=400,
                 background=(1,1,1))
scene2 = display(window = w, title = 'earth', x=w.x+scene1.width, y=0, width=w.width/2, height = 400)


#theta = 0;
#dtheta = 0.0001;


## frame containing rod and gyro


scene1.select()
base = pyramid(pos = BASE_POSITION, axis = BASE_AXIS, size = BASE_SIZE) ## create the suppport for the outer ring 
rod = cylinder(pos= ROD_POSITION, axis= ROD_AXIS , radius= ROD_RADIUS) #Inner Rotating Circle
gyro = cylinder(pos= GYRO_POSITION, axis= GYRO_AXIS, radius= GYRO_RADIUS,material = materials.wood) #Circle Supports
IRING = ring(pos = IRING_POSITION , axis = IRING_AXIS, radius = IRING_RADIUS, thickness = IRING_THICKNESS, color = IRING_COLOUR) #XZ Plane Ring
ORING = ring(pos = ORING_POSITION, axis = ORING_AXIS, radius = ORING_RADIUS, thickness = ORING_THICKNESS, color = ORING_COLOUR ) ## this is the outer ring, might be part of a frame later? (Y- Plane ring)

scene2.select()
sphere(pos = GYRO_POSITION)

## this code rotates the rings, however we wont use this becuase all it does is rotate and accelerate, we need the actual physics. should also do it in spherical coordinates
#while true:
 #   rate(30)
  #  IRING.rotate(angle = theta, axis = (1,0,0))
   # ORING.rotate(angle = theta, axis = (0,1,0))
    #theta += dtheta

    

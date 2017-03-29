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
w = window(title = 'Gyrocompass',x=WINDOW_POSX,y=WINDOW_POSY,width=WINDOW_WIDTH,height=WINDOW_HEIGHT,
           menus = True, style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)

L = 500
d = 20
scene1 = display(window=w, x=d, y=d, width=L-2*d, height=L-2*d, forward=-vector(0,1,2),background = (1,1,1))
scene2 = display(window=w, x=d+scene1.width, y=d, width=L-2*d, height=L-2*d, forward=-vector(0,1,2))

##populate scene1
scene1.select()
base = pyramid(pos = BASE_POSITION, axis = BASE_AXIS, size = BASE_SIZE) ## create the suppport for the outer ring 
rod = cylinder(pos= ROD_POSITION, axis= ROD_AXIS , radius= ROD_RADIUS) #Inner Rotating Circle
gyro = cylinder(pos= GYRO_POSITION, axis= GYRO_AXIS, radius= GYRO_RADIUS,material = materials.wood) #Circle Supports
IRING = ring(pos = IRING_POSITION , axis = IRING_AXIS, radius = IRING_RADIUS, thickness = IRING_THICKNESS, color = IRING_COLOUR) #XZ Plane Ring
ORING = ring(pos = ORING_POSITION, axis = ORING_AXIS, radius = ORING_RADIUS, thickness = ORING_THICKNESS, color = ORING_COLOUR ) ## this is the outer ring, might be part of a frame later? (Y- Plane ring)

##populate scene 2
scene2.select()
sphere(pos = GYRO_POSITION,material = materials.earth)

p = w.panel # Refers to the full region of the window in which to place widgets

wx.StaticText(p, pos=(d,4), size=(L-2*d,d), label='Gyroscope',
              style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)
wx.StaticText(p, pos=(d+scene1.width,4), size=(L-2*d,d), label='Earth',
              style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)





    

from visual import *
import numpy as np
import wx
import scipy as sp
from scipy.integrate import odeint
#import matplotlib.pyplot as plt



##constants
LEFTMARGIN = 20

BASE_POSITION = (0,-12.1 - 1.5,0)
BASE_AXIS = (0,1,0)
BASE_SIZE = (1.5, 1.5, 1.5)
BASE_COLOUR = (0,0,0)

INDICATOR_POSITION = (12.5, 0, 0)
INDICATOR_AXIS = (3, 0, 0)
INDICATOR_WIDTH = 0.2
INDICATOR_COLOR = (0,1,0)
INDICATOR_OPACITY = 0.3

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
IRING_COLOUR =(0.1,0.1,1)

ORING_POSITION = (0,0,0)
ORING_AXIS = (0,0,1)
ORING_RADIUS = 12
ORING_THICKNESS = 0.1
ORING_COLOUR =(0.5,0.5,1)

WINDOW_POSX = 0
WINDOW_POSY = 0
WINDOW_HEIGHT = 1000
WINDOW_WIDTH = 1000

TEXTBOX1_POSX = LEFTMARGIN
TEXTBOX1_POSY = WINDOW_HEIGHT / 2 + 20


##setup window and displays
w = window(title = 'Gyrocompass',x=WINDOW_POSX,y=WINDOW_POSY,width=WINDOW_WIDTH,height=WINDOW_HEIGHT,
           menus = True, style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)

L = 500
d = LEFTMARGIN
scene1 = display(window=w, x=d, y=d, width=L-2*d, height=L-2*d, forward=-vector(0,1,2),background = (1,1,1))
scene2 = display(window=w, x=d+scene1.width, y=d, width=L-2*d, height=L-2*d, forward=-vector(0,1,2))

##populate scene1
scene1.select()
gyro = frame()
indicator = arrow(frame = gyro, pos= INDICATOR_POSITION, axis= INDICATOR_AXIS , shaftwidth= INDICATOR_WIDTH, color = INDICATOR_COLOR, opacity = INDICATOR_OPACITY) #North Indicator
base = pyramid(pos = BASE_POSITION, axis = BASE_AXIS, size = BASE_SIZE, color = BASE_COLOUR) ## create the suppport for the outer ring 
rod = cylinder(frame = gyro, pos= ROD_POSITION, axis= ROD_AXIS , radius= ROD_RADIUS) #Inner Rotating Circle
spinner = cylinder(frame = gyro, pos= GYRO_POSITION, axis= GYRO_AXIS, radius= GYRO_RADIUS,material = materials.wood) #Circle Supports
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

##setup textbox 1
tc = wx.TextCtrl(p, pos=(d,WINDOW_HEIGHT / 2), value='You can type here:\n',
            size=(150,90), style=wx.TE_MULTILINE)
tc.SetInsertionPoint(len(tc.GetValue())+1) # position cursor at end of text
tc.SetFocus() # so that keypresses go to the TextCtrl without clicking it

#For defining the axis rotation on the inner ring from the point frame.
def perpendicular_vector(v):
    if (v.x == 0) and (v.y == 0):
        if (v.z == 0):
            raise ValueError('zero vector')
        return (0, 1, 0)
    return (-v.y, v.x, 0)


print(tc.GetValue())




def g(y, x):
    y0 = y[0]
    y1 = y[1]
    y2 =-100*y0
    return y1, y2

# Initial conditions on y, y' at x=0
init = 1.5, 0.0
# First integrate from 0 to 2
x = np.linspace(0,5,20000)
sol=odeint(g, init, x)
# Then integrate from 0 to -2
x = np.linspace(0,5,20000)
sol=odeint(g, init, x)

# The analytical answer in red dots
exact_x = np.linspace(-2,2,10)
exact_y = 2*np.exp(2*exact_x)-exact_x*np.exp(-exact_x)

for i in range(0,20000):
    rate(100)
    #gyro.rotate(angle=sol[i,0])
    gyro.axis = vector(sin(sol[i,0]), sin(sol[i,0]), cos(sol[i,0]))
    IRING.axis = perpendicular_vector(gyro.axis)
    

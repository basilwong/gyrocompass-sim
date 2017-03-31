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

TEXTBOX_HEIGHT = 20
TEXTBOX_WIDTH = 150
TEXTBOX1_POSX = LEFTMARGIN
TEXTBOX1_POSY = WINDOW_HEIGHT / 2 + 20
TEXTBOX2_POSX = TEXTBOX1_POSX + LEFTMARGIN + TEXTBOX_WIDTH
TEXTBOX2_POSY = TEXTBOX1_POSY

EARTH_RADIUS = 1.0

## this function converts a latitude and longitude in degrees into spherical coordinates
def coordsToSphere(latitude,longitude):
    r = EARTH_RADIUS
    phi = latitude*pi/180
    theta = longitude*pi/180
    x = r *np.cos(phi) *np.sin(theta);
    y = r *np.sin(phi);
    z = r * np.cos(phi) * np.cos(theta)
    spherical = (x,y,z)
    return spherical


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
earth = sphere(pos = GYRO_POSITION,material = materials.earth, radius = EARTH_RADIUS)
little_sphere = sphere(pos = earth.pos + (0,0,earth.radius) + (0,0,earth.radius/32), material = materials.emissive, color = (1,0,1),radius = earth.radius/32)

p = w.panel # Refers to the full region of the window in which to place widgets

wx.StaticText(p, pos=(d,4), size=(L-2*d,d), label='Gyroscope',
              style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)
wx.StaticText(p, pos=(d+scene1.width,4), size=(L-2*d,d), label='Earth',
              style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)

##setup textbox 1
lat = wx.TextCtrl(p, pos=(TEXTBOX1_POSX,TEXTBOX1_POSY), size=(TEXTBOX_WIDTH,TEXTBOX_HEIGHT), style=wx.TE_MULTILINE)
lat.SetInsertionPoint(len(lat.GetValue())+1) # position cursor at end of text

##setup textbox 2
lon = wx.TextCtrl(p, pos=(TEXTBOX2_POSX,TEXTBOX2_POSY),size=(TEXTBOX_WIDTH,TEXTBOX_HEIGHT), style=wx.TE_MULTILINE)
lon.SetInsertionPoint(len(lon.GetValue())+1) # position cursor at end of text

##if you want to see the little sphere respond to changes in lat and lon use line below
##little_sphere.pos = coordsToSphere(lat,lon)

wx.StaticText(p, pos=(TEXTBOX1_POSX,TEXTBOX1_POSY - d), size=(L-2*d,d), label='Latitude')
              #style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)
wx.StaticText(p, pos=(TEXTBOX2_POSX,TEXTBOX2_POSY - d), size=(L-2*d,d), label='Longitude')
              #style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)

#For defining the axis rotation on the inner ring from the point frame.
def perpendicular_vector(v):
    if (v.x == 0) and (v.y == 0):
        if (v.z == 0):
            raise ValueError('zero vector')
        return (0, 1, 0)
    return (-v.y, v.x, 0)

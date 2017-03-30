from visual import *
import numpy as np
import wx



##constants
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

#For defining the axis rotation on the inner ring from the point frame.
def perpendicular_vector(v):
    if (v.x == 0) and (v.y == 0):
        if (v.z == 0):
            raise ValueError('zero vector')
        return (0, 1, 0)
    return (-v.y, v.x, 0)

Lshaft = 1. # length of gyroscope shaft
r = Lshaft/2. # distance from support to center of mass
Rshaft = 0.03 # radius of gyroscope shaft
M = 1. # mass of gyroscope (massless shaft)
Rrotor = 0.4 # radius of gyroscope rotor
Drotor = 0.1 # thickness of gyroscope rotor
I3 = 0.5*M*Rrotor**2 # moment of inertia of gyroscope about its own axis
I1 = M*r**2 + .5*I3 # moment of inertia about a line through the support, perpendicular to the axis
hpedestal = Lshaft # height of pedestal
wpedestal = 0.1 # width of pedestal
tbase = 0.05 # thickness of base
wbase = 3*wpedestal # width of base
g = 22.5
Fgrav = vector(0,-M*g,0)
top = vector(0,0,0) # top of pedestal

theta = 0.3*pi # initial polar angle of shaft (from vertical)
thetadot = 0 # initial rate of change of polar angle
psi = 0 # initial spin angle
psidot = 30 # initial rate of change of spin angle (spin ang. velocity)
phi = -pi/2 # initial azimuthal angle
phidot = 0 # initial rate of change of azimuthal angle
if False: # Set to True if you want pure precession, without nutation
    a = (1-I3/I1)*sin(theta)*cos(theta)
    b = -(I3/I1)*psidot*sin(theta)
    c = M*g*r*sin(theta)/I1
    phidot = (-b+sqrt(b**2-4*a*c))/(2*a)

dt = 0.0001
t = 0.1
Nsteps = 30

while True:
    rate(100)
    for step in range(Nsteps): # multiple calculation steps for accuracy
        # Calculate accelerations of the Lagrangian coordinates:
        atheta = sin(theta)*cos(theta)*phidot**2+(
            M*g*r*sin(theta)-I3*(psidot+phidot*cos(theta))*phidot*sin(theta))/I1
        aphi = (I3/I1)*(psidot+phidot*cos(theta))*thetadot/sin(theta)-2*cos(theta)*thetadot*phidot/sin(theta)
        apsi = phidot*thetadot*sin(theta)-aphi*cos(theta)
        # Update velocities of the Lagrangian coordinates:
        thetadot += atheta*dt
        phidot += aphi*dt
        psidot += apsi*dt
        # Update Lagrangian coordinates:
        theta += thetadot*dt
        phi += phidot*dt
        psi += psidot*dt

    gyro.axis = vector(sin(theta)*sin(phi),cos(theta),sin(theta)*cos(phi))
    # Display approximate rotation of rotor and shaft:
    gyro.rotate(angle=psidot*dt*Nsteps)
    IRING.axis = perpendicular_vector(gyro.axis)
    t = t+dt*Nsteps




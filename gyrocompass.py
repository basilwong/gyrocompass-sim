from visual import *



## frame that comprises the rod and the gyro
f1 = frame()
#Inner Rotating Circle
rod = cylinder(frame = f1, pos=(0,0,0), axis=(1,0,0), radius=10)
#Circle Supports
rod = cylinder(frame = f1, pos=(-11,0,0), axis=(22,0,0), radius=0.3)

## create the suppport for the outer ring
base = pyramid(pos = (0,-5,0), axis = (0,1,0), size = (1.5, 1.5, 1.5))

## this is the outer ring, might be part of a frame later?
ring(pos = (0,0.5,0), axis = (0,0,1), radius = 4, thickness = 0.1, color = (0.4,0.1,0.3))



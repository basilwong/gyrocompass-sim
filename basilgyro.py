from visual import *

## create the suppport for the outer ring 
base = pyramid(pos = (0,-12.1 - 1.5,0), axis = (0,1,0), size = (1.5, 1.5, 1.5))

#Inner Rotating Circle
rod = cylinder(pos=(0,0,0), axis=(0.3,0,0), radius=10)

#Circle Supports
rod = cylinder(pos=(-11,0,0), axis=(22,0,0), radius=0.3)

#XZ Plane Ring
ring(pos = (0,0,0), axis = (0,1,0), radius = 11.1, thickness = 0.1, color = (0.9,0.5,6))

## this is the outer ring, might be part of a frame later? (Y- Plane ring)
ring(pos = (0,0,0), axis = (0,0,1), radius = 12, thickness = 0.1, color = (0.4,0.1,0.3))


import scipy.integrate as integrate
import matplotlib.pyplot as plt
import numpy as np


pi = np.pi
sqrt = np.sqrt
cos = np.cos
sin = np.sin

omega = 0.00007295
I1 = .125 * 0.30 * 3 / 2
I2 = I1 / 2
delta = pi/3;
phidot = -50;

def solvr(z, t):
    alpha, alphadot = z
    return [alphadot, (I1*omega*(phidot - omega*sin(delta)*cos(alpha))*sin(delta)*sin(alpha) +
	1/2 * I2 *omega*omega * (sin(delta))*(sin(delta))*sin(2*alpha))/I2 - alphadot*0.001]

phi = np.linspace(0, 3000, 30000)
zinit = [2*pi/3,0]
z = integrate.odeint(solvr, zinit, phi)
u, udot = z.T
plt.plot(phi, u)

plt.show()


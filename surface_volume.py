import numpy as np

x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)
dx = dy =  x[1] - x[0]

X,Y =np.meshgrid(x, y)
Z= X**2 + Y**2


volume = np.sum(Z) * dx * dy
print("pproximate Volume under surface:", volume)
from scipy.integrate import odeint
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
def lorenz(w, t):
    sigma = 10; rho = 28; beta  = 8/3
    x, y, z=w;
    return np.array([sigma*(y-x), rho*x-y-x*z, x*y-beta*z])
t = np.arange(0, 50, 0.01)  #创建时间戳
sol1 = odeint(lorenz, [0.0, 1.0, 0.0], t)
sol2 = odeint(lorenz, [0.0, 1.001,0.0],t)
plt.rc('font', size = 16);
ax1 = plt.subplot(121,projection = '3d')
ax1.plot(sol1[:,0],sol1[:,1],sol1[:,2],'r')
ax1.set_xlabel('x');ax1.set_ylabel('y');ax1.set_zlabel('z')
ax2 = plt.subplot(122,projection = '3d')
ax2.plot(sol1[:,0]-sol2[:,0], sol1[:,1]-sol2[:,1], sol1[:,2]-sol2[:,2],'g')
plt.savefig('choatic.jpg',dpi = 500)
print("sol1:",sol1.shape,'\n\n',"sol2 =",sol2)

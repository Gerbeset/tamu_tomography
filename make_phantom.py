import sys
import matplotlib.pyplot as plt
sys.path.append("phantoms")

from phantoms import bumps_1
import numpy as np

class create_phantom:
    def __init__(self, dofs, phantom_class):
        self.dofs = dofs
        self.coarse_x_vals = np.linspace(-1,1,dofs)
        self.coarse_y_vals = np.linspace(-1,1,dofs)
        self.phantom_class = phantom_class
    
    
my_phantom = bumps_1.phantom_bumps_1

coarse_x_vals = np.linspace(0,1,10)
coarse_y_vals = np.linspace(0,1,10)

fine_x_vals = np.linspace(0,1, 20)
fine_y_vals = np.linspace(0,1,20)

coarse_phantom = np.zeros((10,10))
fine_phantom = np.zeros((20,20))

for i in range(0,len(coarse_x_vals)-1):
    for j in range(0,len(coarse_y_vals)-1):
        coarse_phantom[i][j] = bumps_1.phantom_bumps_1_function(coarse_x_vals[i], coarse_y_vals[j])

for i in range(len(fine_x_vals)-1):
    for j in range(len(fine_y_vals)-1):
        fine_phantom[i][j] = bumps_1.phantom_bumps_1_function(fine_x_vals[i], fine_y_vals[j])
        
plt.imshow(fine_phantom, extent=(0, 1, 0, 1), origin='lower', cmap='viridis')
plt.colorbar(label='Phantom Value')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Fine Phantom')
plt.grid(False)
plt.show()
        
#plt.imshow(coarse_phantom, extent=(0, 1, 0, 1), origin='lower', cmap='viridis')
#plt.colorbar(label='Phantom Value')
#plt.xlabel('X')
#plt.ylabel('Y')
#plt.title('Coarse Phantom')
#plt.grid(False)
#plt.show()

        

#coarse_phantom = bumps_1.phantom_bumps_1(coarse_x, coarse_y)
#fine_phantom = bumps_1.phantom_bumps_1(fine_x, fine_y)




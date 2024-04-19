import sys
import matplotlib.pyplot as plt

from phantoms import single_bump
from phantoms import bumps_1
import numpy as np

class create_phantom:
    def __init__(self, dofs, phantom_class):
        self.dofs = dofs
        self.x_vals = np.linspace(-1,1,dofs)
        self.y_vals = np.linspace(-1,1,dofs)
        self.phantom_class = phantom_class
        self.phantom = np.zeros((dofs,dofs))
    
    def generate_phantom(self):
        for i in range(0, len(self.x_vals)-1):
            for j in range(0, len(self.y_vals)-1): 
                self.phantom[i][j] = self.phantom_class.values(self.x_vals[i], self.y_vals[j])

    def val_of_phantom(self, x,y):
        return self.phantom_class.values(x,y)
    
    def display_phantom(self):
        plt.imshow(self.phantom, extent=(-1,1,-1,1), origin = 'lower', cmap = 'viridis' )
        plt.colorbar(label= 'Phantom Value')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Phantom')
        plt.grid(False)
        plt.show()
        
    
my_phantom = bumps_1()

test_phantom = create_phantom(100, my_phantom)
test_phantom.generate_phantom()
test_phantom.display_phantom()

'''
coarse_x_vals = np.linspace(-1,1,20)
coarse_y_vals = np.linspace(-1,1,20)

fine_x_vals = np.linspace(-1,1,40)
fine_y_vals = np.linspace(-1,1,40)

coarse_phantom = np.zeros((20,20))
fine_phantom = np.zeros((40,40))

for i in range(0,len(coarse_x_vals)-1):
    for j in range(0,len(coarse_y_vals)-1):
        coarse_phantom[i][j] = bumps_1.phantom_bumps_1_function(coarse_x_vals[i], coarse_y_vals[j])

for i in range(len(fine_x_vals)-1):
    for j in range(len(fine_y_vals)-1):
        fine_phantom[i][j] = bumps_1.phantom_bumps_1_function(fine_x_vals[i], fine_y_vals[j])
        
plt.imshow(fine_phantom, extent=(-1, 1, -1, 1), origin='lower', cmap='viridis')
plt.colorbar(label='Phantom Value')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Fine Phantom')
plt.grid(False)
plt.show()
'''

#plt.imshow(coarse_phantom, extent=(0, 1, 0, 1), origin='lower', cmap='viridis')
#plt.colorbar(label='Phantom Value')
#plt.xlabel('X')
#plt.ylabel('Y')
#plt.title('Coarse Phantom')
#plt.grid(False)
#plt.show()

        

#coarse_phantom = bumps_1.phantom_bumps_1(coarse_x, coarse_y)
#fine_phantom = bumps_1.phantom_bumps_1(fine_x, fine_y)




import smooth_decay

import numpy as np

class bump:
    def __init__(self, center_x, center_y, inner_radius, outer_radius, amp):
        self.center_x = center_x
        self.center_y = center_y
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius
        self.amp = amp

    def value(self, x,y): 
        distance = np.sqrt((x - self.center_x)**2 + (y - self.center_y)**2)
        return self.amp*smooth_decay.smooth_decay(self.inner_radius, self.outer_radius,distance)
    
test_bump = bump(0,0, 0.3, 0.24, 1)

print(test_bump.value(0,0))

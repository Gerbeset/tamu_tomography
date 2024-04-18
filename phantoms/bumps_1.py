import sys
sys.path.append("base_phantoms")

from base_phantoms import bump

bump_1 = bump.bump(0,0, 0.3, 0.24, 1)
bump_2 = bump.bump(0.7, 0, 0.15, 0.135, 1)
bump_3 = bump.bump(-0.35, -0.606, 0.08, 0.072, 1)
bump_4 = bump.bump(-0.350, 0.606, 0.04, 0.036, 1)

class phantom_bumps_1:
    def __init__(self):
        self.bump_1 = bump.bump(0,0, 0.3, 0.24, 1)
        self.bump_2 = bump.bump(0.7, 0, 0.15, 0.135, 1)
        self.bump_3 = bump.bump(-0.35, -0.606, 0.08, 0.072, 1)
        self.bump_4 = bump.bump(-0.350, 0.606, 0.04, 0.036, 1)
        
    def values(self,x,y): 
        return self.bump_1.value(x,y) + self.bump_2.value(x,y) +self.bump_3.value(x,y) + self.bump_4.value(x,y)

def phantom_bumps_1_function(x,y): 
    return bump_1.value(x,y) + bump_2.value(x,y) + bump_3.value(x,y) + bump_4.value(x,y)

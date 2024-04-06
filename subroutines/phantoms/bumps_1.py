from base_phantoms import bump

bump_1 = bump(0,0, 0.3, 0.24, 1)
bump_2 = bump(0.7, 0, 0.15, 0.135, 1)
bump_3 = bump(-0.35, -0.606, 0.08, 0.072, 1)
bump_4 = bump(-0.350, 0.606, 0.04, 0.036, 1)

def phantom_bumps_1(x,y): 
    return bump_1.value(x,y) + bump_2.value(x,y) + bump_3.value(x,y) + bump_4.value(x,y)

print(phantom_bumps_1(0,0))
from make_phantom import create_phantom
from phantoms import bumps_1
from phantoms import single_bump


myphantom_class = bumps_1()

myphantom = create_phantom(100, myphantom_class)

myphantom.generate_phantom()
myphantom.display_phantom()


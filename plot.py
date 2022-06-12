from random import gauss
from matplotlib import pyplot as plt
import numpy as np
from classes import Atom, Electron

TEMPERATURE = 0.5
NUMBER_OF_ELECTRONS = 50
SIZE = 1000
MAX_DEVIATION = 2

x = [x for x in range(5, 86, 10)]
y = [y for y in range(5, 46, 10)]

atoms = []
for a in x:
    for b in y:
        atom = Atom(a, b, MAX_DEVIATION, SIZE, TEMPERATURE)
        atoms.append(atom)

electrons = []
for _ in range(0, NUMBER_OF_ELECTRONS):
    electron = Electron(gauss(-10, 10), gauss(25, 15), 10)
    electrons.append(electron)

plt.ion()
fig = plt.figure(figsize=(18, 9), dpi=100)
ax = fig.add_subplot()
fig.canvas.draw()
axbackground = fig.canvas.copy_from_bbox(ax.bbox)
plt.show(block=False)

while(1):
    drif = 0
    for atom in atoms:
        x = atom.get_dim_x()
        y = atom.get_dim_y()
        colors = "red"
        ax.scatter(x, y, s=SIZE, c=colors)
        atom.random_move()
    
    for electron in electrons:
        x = electron.get_location_x()
        y = electron.get_location_y()
        sizes = electron.get_size()
        colors = "blue"
        ax.scatter(x, y, s=sizes, c=colors)
        electron.move(atoms)
        drif += electron.get_velocity_x()

    ax.set(xlim=(0, 90), xticks=np.arange(10, 81, 10),
        ylim=(0, 50), yticks=np.arange(10, 41, 10))
    
    fig.canvas.restore_region(axbackground)
    fig.canvas.blit(ax.bbox)
    fig.canvas.flush_events()
    ax.clear()
    drif /= len(electrons)
    print(drif / electrons[0].get_max_x_velocity())

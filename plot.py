from random import gauss
from matplotlib import pyplot as plt
import numpy as np
from classes import Atom, Electron

TEMPERATURE = 0.5 # <0, 0.5>
NUMBER_OF_ELECTRONS = 50 # <0, 100>
SIZE = 12 # <8, 12>

x = [x for x in range(5, 86, 10)]
y = [y for y in range(5, 46, 10)]

atoms = []
for a in x:
    for b in y:
        atom = Atom(a, b, max(7 - SIZE + TEMPERATURE, 2), SIZE, TEMPERATURE)
        atoms.append(atom)

electrons = []
for _ in range(0, NUMBER_OF_ELECTRONS):
    electron = Electron(gauss(-15, 10), gauss(25, 15), 4)
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
        sizes = atom.get_size()
        ax.scatter(x, y, s=2**sizes, c=colors)
        atom.random_move()
    
    for electron in electrons:
        x = electron.get_location_x()
        y = electron.get_location_y()
        sizes = electron.get_size()
        colors = "blue"
        ax.scatter(x, y, s=2**sizes, c=colors)
        electron.move(atoms)
        drif += electron.get_velocity_x()

    ax.set(xlim=(0, 90), xticks=np.arange(10, 81, 10),
        ylim=(0, 50), yticks=np.arange(10, 41, 10))
    
    fig.canvas.restore_region(axbackground)
    fig.canvas.blit(ax.bbox)
    fig.canvas.flush_events()
    ax.clear()
    if(len(electrons)):
        drif /= len(electrons)
        print(drif / electrons[0].get_max_x_velocity())

#TODO dziesieciokrotnie spowolnic symulacje i przyspieszyc rysowanie 100 razy ;)
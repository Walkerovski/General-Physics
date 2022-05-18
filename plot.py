import matplotlib.pyplot as plt
import numpy as np
from classes import Atom, Electron

x = [x for x in range(10, 101, 10)]
y = [y for y in range(10, 51, 10)]

atoms = []
for a in x:
    for b in y:
        atom = Atom(a, b, 2, 50, 5)
        atoms.append(atom)

electrons = []
for b in y:
    electron = Electron(0, b, 2)
    electrons.append(electron)

plt.ion()
fig, ax = plt.subplots()

while(1):
    for atom in atoms:
        x = atom.get_dim_x()
        y = atom.get_dim_y()
        sizes = atom.get_size()
        colors = "red"
        ax.scatter(x, y, s=sizes, c=colors)
        atom.random_move(10)
    
    for electron in electrons:
        x = electron.get_new_location_x()
        y = electron.get_new_location_y()
        sizes = electron.get_new_size()
        colors = "blue"
        ax.scatter(x, y, s=sizes, c=colors)
        electron.move()

    ax.set(xlim=(0, 110), xticks=np.arange(10, 101, 10),
        ylim=(0, 60), yticks=np.arange(10, 51, 10))
    
    fig.canvas.draw()
    fig.canvas.flush_events()
    ax.clear()

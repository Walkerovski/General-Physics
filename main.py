import pygame
from time import sleep
from random import gauss
from classes import Atom, Electron
from consts import *

# Initialize the pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

atoms_centres_x = [WIDTH/20 + n*WIDTH/10 for n in range(10)]
atoms_centres_y = [HEIGHT/10 + n*HEIGHT/5 for n in range(5)]
atoms_centres = []
atoms = []
for x in atoms_centres_x:
    for y in atoms_centres_y:
        atoms_centres.append((x, y))
for xy in atoms_centres:
    atoms.append(Atom(xy[0], xy[1], MAX_DEVIATION, SIZE, TEMPERATURE))

electrons = []
for index in range(NUMBER_OF_ELECTRONS):
    electrons.append(Electron(gauss(-WIDTH/100, WIDTH/50), gauss(HEIGHT/2, HEIGHT/5), 3))


running = True
size = 1
temperature = 5
# atom_size = 10
# game loop

while running:
    screen.fill(BLACK)
    drif = 0

    sleep(0.03)
    for atom in atoms:
        atom.move()
        x = atom.get_dim_x()
        y = atom.get_dim_y()
        location = (x, y)
        atom_size = atom.get_size()
        pygame.draw.circle(screen, RED, location, atom_size)
    for electron in electrons:
        electron.move(atoms, HEIGHT, WIDTH)
        x = electron.get_location_x()
        y = electron.get_location_y()
        location = (x, y)
        atom_size = electron.get_size()
        drif += electron.get_velocity_x()
        pygame.draw.circle(screen, BLUE, location, atom_size)
    output = (drif / len(electrons) / electrons[0].get_max_x_velocity())
    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render(f"Drif: {round(output, 2)}", True, TEXTCOLOR)
    screen.blit(text, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()
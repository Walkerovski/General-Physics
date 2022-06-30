import imp
from pickle import TRUE
import pygame
from time import sleep
from random import gauss
from classes import Atom, Electron
from consts import *
from slider import Slider


def gen_atoms(atoms_centres):
    temperature = round(interface[0].val)
    size = round(interface[2].val)
    atoms = []
    for xy in atoms_centres:
        atoms.append(Atom(xy[0], xy[1], 15, size, temperature))
    return atoms


def gen_electrons():
    no_of_electrons = round(interface[1].val)
    electrons = []
    for _ in range(no_of_electrons):
        electrons.append(Electron(gauss(-WIDTH/100, WIDTH/50), gauss(HEIGHT/2, HEIGHT/5), 3))
    return electrons


def initial_setup():
    atoms_centres_x = [WIDTH/20 + n*WIDTH/10 for n in range(10)]
    atoms_centres_y = [HEIGHT/10 + n*HEIGHT/5 for n in range(5)]
    atoms_centres = []
    for x in atoms_centres_x:
        for y in atoms_centres_y:
            atoms_centres.append((x, y))
    atoms = gen_atoms(atoms_centres)
    electrons = gen_electrons()
    return atoms, electrons


def set_params():
    temperature = round(interface[0].val)
    size = round(interface[2].val)
    for _ in atoms:
        _.set_temperature(temperature)
        _.set_size(size)
    return gen_electrons()


# Initialize the pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT + 100))
font = pygame.font.SysFont('calibri', 20)

interface = [
        Slider(screen, "Temperature", 10, 100, 55, 390, HEIGHT + 15, font),
        Slider(screen, "No of electrons", 1, 100, 50, 140, HEIGHT + 15, font),
        Slider(screen, "Size of atoms", 10, 30, 20, 640, HEIGHT + 15, font)
    ]

atoms, electrons = initial_setup()
running = TRUE

#############################################
# Simulation:
while running:
    screen.fill(BLACK)
    pygame.draw.rect(screen, GRAY, (0, HEIGHT + 10, WIDTH, HEIGHT + 100))
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
    text = font.render(f"Drif: {round(output, 2)}", True, TEXTCOLOR)
    screen.blit(text, (0, 0))
    
    for _ in interface:
        _.draw()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for _ in interface:
            if _.handle_event(event):
                electrons = set_params()
    pygame.display.flip()
pygame.quit()
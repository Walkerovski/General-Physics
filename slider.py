import pygame
from consts import *

class Slider():
    def __init__(self, screen, name, mini, maxi, val, xpos, ypos, font):
        self.screen = screen
        self.mini = mini  # minimum at slider position left
        self.maxi = maxi  # maximum at slider position right
        self.val = val    # start value
        self.xpos = xpos
        self.ypos = ypos
        self.surf = pygame.surface.Surface((200, 80))
        self.surf.fill(BLACK)
        self.txt_surf = font.render(name, True, WHITE)
        self.txt_rect = self.txt_surf.get_rect(center=(100, 15))
        self.hit = False  # the hit attribute indicates slider movement due to mouse interaction
        self.button_surf = self.button_render()
        self.button_rect = None

    def button_render(self):
        pygame.draw.rect(self.surf, WHITE, [20, 35, 160, 20], 0)
        self.surf.blit(self.txt_surf, self.txt_rect)
        button_surf = pygame.surface.Surface((40, 40))
        button_surf.fill(WHITE)
        button_surf.set_colorkey(WHITE)
        pygame.draw.circle(button_surf, BLACK, (20, 20), 10, 0)
        pygame.draw.circle(button_surf, GREEN, (20, 20), 7, 0)
        return button_surf

    def draw(self):
        surf = self.surf.copy()
        pos = (20 + int((self.val - self.mini) / (self.maxi - self.mini) * 160), 45)
        self.button_rect = self.button_surf.get_rect(center=pos)
        surf.blit(self.button_surf, self.button_rect)
        self.button_rect.move_ip(self.xpos, self.ypos)  # move of button box to correct screen position
        self.screen.blit(surf, (self.xpos, self.ypos))

    def move(self):
        self.val = (pygame.mouse.get_pos()[0] - self.xpos - 20) / 160 * (self.maxi - self.mini) + self.mini
        if self.val < self.mini:
            self.val = self.mini
        if self.val > self.maxi:
            self.val = self.maxi
        print(self.val)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.button_rect.collidepoint(pos):
                self.hit = True
                return True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.hit = False
        elif event.type == pygame.MOUSEMOTION:
            if self.hit:
                self.move()
                return True
        return False
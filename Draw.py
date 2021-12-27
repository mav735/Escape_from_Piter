import pygame
import os
import configparser


class DrawFloor:
    def __init__(self, screen, type_texture, Map):
        """:parameter screen: surface where you draw
           :parameter type_texture: key in self.materials"""
        self.screen = screen

        config = configparser.ConfigParser()
        config.read('Settings.cfg')
        self.cell_size = int(config['Cell_size']['cell_size'])

        self.type_texture = type_texture
        self.materials = {
            '1': pygame.transform.scale(
                pygame.image.load(os.path.join('Floor', 'floor1.png')).convert(),
                (self.cell_size, self.cell_size)),
            '2': pygame.transform.scale(
                pygame.image.load(os.path.join('Walls', 'wall2.png')).convert(),
                (self.cell_size, self.cell_size)),
            '3': pygame.transform.scale(
                pygame.image.load(os.path.join('Walls', 'wall3.png')).convert(),
                (self.cell_size, self.cell_size)),
            '4': pygame.transform.scale(
                pygame.image.load(os.path.join('Walls', 'wall4.png')).convert(),
                (self.cell_size, self.cell_size)),
            '5': pygame.transform.scale(
                pygame.image.load(os.path.join('Walls', 'wall5.png')).convert(),
                (self.cell_size, self.cell_size)),
            '6': pygame.transform.scale(
                pygame.image.load(os.path.join('Walls', 'wall6.png')).convert(),
                (self.cell_size, self.cell_size)),
            '7': pygame.transform.scale(
                pygame.image.load(os.path.join('Walls', 'wall7.png')).convert(),
                (self.cell_size, self.cell_size))
        }
        self.map = Map

    def blit_floor(self, coords):
        """:parameter coords: left and top border(x, y)"""
        for row in range(50):
            for column in range(50):
                if self.map[row][column] != '-1' and self.map[row][column] != '0':
                    self.screen.blit(self.materials[str(self.map[row][column])],
                                     (coords[0] + row * self.cell_size,
                                      coords[1] + column * self.cell_size))
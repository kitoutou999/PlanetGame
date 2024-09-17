# -*- coding: utf-8 -*-

import pygame
import os
from random import *
from world.player import *
class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self,entity,grille):
        super().__init__()
        self.grille = grille
        self.sprite_sheet = None
        self.random_choice(entity)
        

        self.animation_index = 0
        self.sprite_size=48#Taille de chaque image de chaque entité (chaque mouvement differencier)
        self.images ={#Permet de lire la bonne ligne sur chaque sprites sheat en fonction d'un mot donner(dans notre cas les direction)
            'down':self.get_images(0),
            'left':self.get_images(self.sprite_size),
            'right':self.get_images(self.sprite_size*2),
            'up':self.get_images(self.sprite_size*3),
        }
        self.time =0#Initialise un compteur pour la vitesse de l'animation
        self.speed = 2#Vitesse de deplacement de l'entité Movable
        
    def random_choice(self,name):
        """Permet de liée les flaque d'eau dans le monde"""
        if name.get_name() == "Water":
            text = ""
            grid = [1 if elt != None and elt.get_name() == "Water" else 0 for elt in self.grille]
            grid[0]=0
            grid[2]=0
            grid[4]=0
            grid[6]=0
            for elt in grid:
                text+=str(elt)
            try:
                sprite_name=f"{text}.png"
                self.sprite_sheet = pygame.image.load(f"./images/{name.get_name()}/{sprite_name}").convert_alpha()
            except FileNotFoundError:
                sprite_name=f"11111111.png"
                self.sprite_sheet = pygame.image.load(f"./images/{name.get_name()}/{sprite_name}").convert_alpha()
        else:
            sprite_name=choice( os.listdir(f"./images/{name.get_name()}"))
            self.sprite_sheet = pygame.image.load(f"./images/{name.get_name()}/{sprite_name}").convert_alpha()


    def change_animation(self, name):
        """Cette fonction gere les animations, prend en parametre le nom(str) de chaque direction"""
        self.image = self.images[name][self.animation_index]#Lire la ligne et l'index en fonction de l'index
        self.time += self.speed * 5

        if self.time >= 100:#change chaque image toute les 100 tick
            self.animation_index+=1
            if self.animation_index >= len(self.images[name]):
                self.animation_index = 0
            self.time = 0


    def get_images(self,y):
        """Permet de lire chaque frame de chaque sprite sheat de chaque animation"""
        images = []
        for i in range(0,3):
            x=i*self.sprite_size
            image = self.get_image(x,y)
            images.append(image)
        return images


    def get_image(self,x,y):
        """Est utilisé dans la fonction get_images() et permet de couper les sprite sheat 
        pour avoir chaque frame de chaque animation"""
        image = pygame.Surface((self.sprite_size, self.sprite_size), pygame.SRCALPHA)
        image.blit(self.sprite_sheet, (0, 0), (x, y, self.sprite_size, self.sprite_size))
        image = image.subsurface(image.get_bounding_rect())  # Extraire la zone utilisée
        return image
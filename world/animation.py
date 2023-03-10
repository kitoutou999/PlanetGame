# -*- coding: utf-8 -*-

import pygame
import os
from random import *
class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self,name):
        super().__init__()
        sprite_name=choice( os.listdir(f"./images/{name}"))
        self.sprite_sheet = pygame.image.load(f"./images/{name}/{sprite_name}").convert_alpha()

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
        
        



    def change_animation(self, name):
        """Cette fonction gere les animations, prend en parametre le nom(str) de chaque direction"""
        self.image = self.images[name][self.animation_index]#Lire la ligne et l'index en fonction de l'index
        #self.image.set_colorkey(0,0)#Met le fond Alpha des image en transparent(noir de base)
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
        image = pygame.Surface([self.sprite_size,self.sprite_size])
        image.blit(self.sprite_sheet,(0,0),(x,y,self.sprite_size,self.sprite_size))
        image
        return image
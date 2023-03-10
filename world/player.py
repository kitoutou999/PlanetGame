# -*- coding: utf-8 -*-

from random import *
from world.config import *
from world.animation import *
from world.elements import *
from world.affichage import *

class Player(AnimateSprite):

    def __init__(self,entity,x,y):

        super().__init__(entity.get_name())
        self.entity = entity  #Permet de lié une class Sprite et la class de sont element exemple: Herb()
        self.name = entity.get_name()#Recupere la nom de l'entité element
        self.image = self.get_image(0,0) #Recupere l'image en haut a gauche 
        #self.image.set_colorkey(0,0)#Met le fond de l'image en transparent (noir de base)
        self.rect = self.image.get_rect()#Permet de recuperer les coordonnées de en fonction du sprite 
        self.position = [x,y] #Position du sprite
        self.clock = randint(0,1000) #Permet de faire bouger les entité pas en meme temps
        self.pos = [randint(-1,1),randint(-1,1)] #Initialise une direction aleatoire pour commencer les mouvement
        
        

    def update(self) :
        #Permet de mettre les coordonnées sur la position en haut a gauche de chaque sprite(ne pas toucher c'est le mieux)
        self.rect.topleft = self.position


    
    def change_direction(self):
        """Permet de changer le sprite en fonction de la direction(ne pas toucher, les animations sont les plus realistes)"""
        if self.pos[0]==1:
            self.change_animation("right")
        elif self.pos[0]==-1:
            self.change_animation("left")
        elif self.pos[1]==1:
            self.change_animation("down")
        elif self.pos[1]==-1:
            self.change_animation("up")


    def move(self):
        """Permet de deplacer les sprites en fonction des coordonnées et change les animation avec un certain temp entre chaque
        (permet de ne pas sortir de la map)"""
        if self.position[0]+self.pos[0] and self.position[0]+self.pos[0]<PYGAME_SIZE-48:
            if self.position[1]+self.pos[1]and self.position[1]+self.pos[1]<PYGAME_SIZE-48:
                self.change_direction()
                self.position[0]+=self.pos[0]#Ajoute la direction aleatoire a la position de l'entité
                self.position[1]+=self.pos[1]#Ajoute la direction aleatoire a la position de l'entité
            else:
                self.clock = 0#Permet de repartir vite si l'entité fonce dans un mur
        else:
            self.clock = 0#Permet de repartir vite si l'entité fonce dans un mur
            
        
        self.clock -= MOVE_SPEED#Permet de determiner le temp entre chaque changement de direction
        if self.clock <= 0:
            self.clock = 1000
            self.pos=[randint(-1,1),randint(-1,1)]#Determine une direction aleatoire


    
            

                        


        
        
            
        
   


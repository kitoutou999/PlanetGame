# -*- coding: utf-8 -*-

from random import *
from world.animation import AnimateSprite
from world.config import *
from world.animation import *
from world.elements import *
from world.game import *

class Player(AnimateSprite):

    def __init__(self, entity, x, y, grille, no_temp = True):

        super().__init__(entity, grille)
        
        self.entity = entity  #Permet de lié une class Sprite et la class de sont element exemple: Herb()
        self.name = entity.get_name()#Recupere la nom de l'entité element
        self.no_temp = no_temp
        if self.no_temp == True:
            self.position = [x*PLANET_PYGAME_SIZE_GRID+500,y*PLANET_PYGAME_SIZE_GRID+500] #Position du sprite
        else:
            self.position = [x,y]

        self.pos = [randint(-1,1),randint(-1,1)] #Initialise une direction aleatoire pour commencer les mouvement




        self.image = self.get_image(0,0) #Recupere l'image en haut a gauche 
        self.rect = self.image.get_rect()#Permet de recuperer les coordonnées de en fonction du sprite 
        self.clock = randint(0,1000) #Permet de faire bouger les entité pas en meme temps
        
        

    def update(self) :
        """Permet de mettre les coordonnées sur la position en haut a gauche de chaque sprite(ne pas toucher c'est le mieux)"""
        self.rect.topleft = self.position


    
    def change_anim_dir(self):
        """Permet de changer le sprite en fonction de la direction(ne pas toucher, les animations sont les plus realistes)"""
        if self.pos[0]==1:
            self.change_animation("right")
        elif self.pos[0]==-1:
            self.change_animation("left")
        elif self.pos[1]==1:
            self.change_animation("down")
        elif self.pos[1]==-1:
            self.change_animation("up")



    def human_move(self):
        """Effectue les mouvements du joueur"""
        presssed = pygame.key.get_pressed()
        if presssed[pygame.K_RIGHT]:
            self.pos[0] = 1
        elif presssed[pygame.K_LEFT]:
            self.pos[0] = -1
        else:
            self.pos[0] = 0

        if presssed[pygame.K_DOWN]:
            self.pos[1] = 1
        elif presssed[pygame.K_UP]:
            self.pos[1]=-1
        else:
            self.pos[1]=0
        



    def move(self):
        """Permet de deplacer les sprites en fonction des coordonnées et change les animation avec un certain temp entre chaque
        (permet de ne pas sortir de la map)"""
        
        for i in range(animals[self.name]["speed"]): 
            if self.name == "Humain":
                self.human_move()
            if self.position[0]+self.pos[0]>500 and self.position[0]+self.pos[0]<WORLD_SIZE[0]-40+500:
                if self.position[1]+self.pos[1]>500 and self.position[1]+self.pos[1]<WORLD_SIZE[1]-40+500:
                    self.change_anim_dir()
                    self.position[0]+=self.pos[0]#Ajoute la direction aleatoire a la position de l'entité
                    self.position[1]+=self.pos[1]#Ajoute la direction aleatoire a la position de l'entité
                else:
                    self.pos = [self.pos[0]*-1,self.pos[1]*-1]
            else:
                self.pos = [self.pos[0]*-1,self.pos[1]*-1]
           
        self.clock -= animals[self.name]["move_size"]#Permet de determiner le temp entre chaque changement de direction
        if self.clock <= 0:
            self.clock = 500
            if self.name != "Humain":
                self.pos = [choice([-1,0,0,1]),choice([-1,0,0,1])]#Determine une direction aleatoire

            



    
            

                        


        
        
            
        
   


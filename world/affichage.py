# -*- coding: utf-8 -*-

import pygame
import pytmx
import pyscroll
import os
from world.planets import PlanetAlpha
from world.grid import Grid
from world.elements import *
from world.player import Player
from world.config import *
from world.animation import *


class Game(PlanetAlpha):
    
    def __init__(self,longitude_cells_count,latitude_cells_count,ground) :

        PlanetAlpha.__init__(self, longitude_cells_count, latitude_cells_count, ground)#Heritage de PlanetAlpha
        self.screen = pygame.display.set_mode((PYGAME_SIZE, PYGAME_SIZE))#Initialise la taille de la fenetre
        pygame.display.set_caption("PlanetGame")#Initialise le nom de la fenetre pygame

        tmx_data = pytmx.util_pygame.load_pygame(f'./map/carte.tmx')#Initialisation de la carte(arriere plan du monde)
        map_data = pyscroll.data.TiledMapData(tmx_data)#Recupere les data de la map(layer,collision ect)mais inutile pour l'instant
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data,self.screen.get_size())#Initialise le zoom
        map_layer.zoom = 1#Multiplicateur de zoom

        self.entity_group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)#Groupe de toute les entité presente sur la fenetre(class player et non Elements)
        





    def entity_add(self):
        """Fonction qui ajoute toute les entité (sauf Ground())
          avec leur textures qui ont pour nom le fichier ou son les sprites"""
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j].get_name() != 'Ground':#Igniore l'entité Ground()
                    entity = Player( self.grid[i][j],i*PLANET_PYGAME_SIZE_GRID+5,j*PLANET_PYGAME_SIZE_GRID+5)#Crée chaque entité avec leur class,leur positions + valeur en fonction de la taille de la fenetre
                    self.entity_group.add(entity)#Ajoute les entité au groupe generale
           
                    
    def entity_move(self):
        """Cette fonction appelle la fonction move dans Player qui fait bouger toute
          les entité dans la liste MOVABLE_ELEMENT dans le dossier config"""
        for elt in self.entity_group:
            if elt.name in MOVABLE_ELEMENT:
                elt.move()
  
    def voisin(self,element):
        """Cette fonction prend en parametre une class Player et qui s'occupe a detecter les collisions de 'element'  
        et renvoie une liste de toute les entitées qui le touche(renvoie une liste de class Element exemple [Herb(),Cow()])"""
        voisin_list=[]
        for cible in self.entity_group:
            if element.entity.get_id() != cible.entity.get_id():#Regarde si l'entité toucher n'est pas lui meme
                if(cible.position[0]>element.position[0]-48 and cible.position[0]<element.position[0]+48):#Regarde si les entité sont sur 'element' sur les axe X
                    if(cible.position[1]>element.position[1]-48 and cible.position[1]<element.position[1]+48):#Regarde si les entité sont sur 'element' sur les axe Y
                        voisin_list.append(cible.entity)
        return voisin_list
    


                    
    def update(self):
        """Refresh la position du rect de chaque sprites de chaque entité"""
        self.entity_group.update()
        


    def run(self):
        """Fonction principal qui est une boucle dans laquel on refresh la page de pygame, on deplace les entité ect"""
        clock = pygame.time.Clock()#Initialise une clock pour definir le nombre de fps au jeu
    
        self.entity_add()#Ajoute toute les entitées sur la fenetre pygame


        

        run=True
        while run:            
            self.entity_move()#Deplace toute les entitées
            self.update()#Refresh la position de toute les entitées
            self.entity_group.draw(self.screen)#Affiche sur la fenetre pyagme toute les entitées
            
            pygame.display.flip()#Refresh la page fenetre 

            for event in pygame.event.get():#Cette partie permet de couper le programe quand on ferme avec la croix en haut a droite
                if event.type == pygame.QUIT:
                    run=False


            clock.tick(60)#Changer le nombre d'actualisation par seconde (fps)
            

        pygame.quit()









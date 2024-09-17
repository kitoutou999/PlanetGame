# -*- coding: utf-8 -*-

import time
import pygame
import pytmx
import pyscroll
import math
import os
from world.planets import PlanetAlpha
from world.grid import Grid
from world.elements import *
from world.player import Player
from world.config import *
from world.animation import *


class Game(PlanetAlpha):
    pygame.init()
    def __init__(self) :
        
        PlanetAlpha.__init__(self)#Heritage de PlanetAlpha
        self.screen = pygame.display.set_mode(WINDOW_SIZES["game"])#Initialise la taille de la fenetre
        pygame.display.set_caption("PlanetGame")#Initialise le nom de la fenetre pygame


        tmx_data = pytmx.util_pygame.load_pygame(f'./map/carte.tmx')#Initialisation de la carte(arriere plan du monde)
        map_data = pyscroll.data.TiledMapData(tmx_data)#Recupere les data de la map(layer,collision ect)mais inutile pour l'instant
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data,(self.screen.get_size()))#Initialise le zoom
        map_layer.zoom = ZOOM#Multiplicateur de zoom

        self.screen_width,self.screen_height=self.screen.get_size()

        #Les valeurs initialise la texture des stats de l'entity
        self.rect_width, self.rect_height = 175, 250
        self.rect_x, self.rect_y = self.screen_width - self.rect_width, 0

        self.rect_width_G, self.rect_height_G = 175, 216

        self.sprite_sheet_stats = pygame.image.load(f"images/stats_icons/Stats.png").convert_alpha()
        self.sprite_sheet_stats = pygame.transform.scale(self.sprite_sheet_stats, (self.rect_width,self.rect_height))

        self.sprite_sheet_stats_G = pygame.image.load(f"images/stats_icons/global.png").convert_alpha()
        self.sprite_sheet_stats_G = pygame.transform.scale(self.sprite_sheet_stats_G, (self.rect_width_G,self.rect_height_G))



        self.fps = FPS
        self.entity_group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)#Groupe de toute les entité presente sur la fenetre(class player et non Elements)
        self.clock = 0
        self.player = None#Stock la class du player
        self.stats_entity = None#Stock la class de l'entité selectionné
        

        #Gere le zoom sur le monde
        self.zoom=ZOOM
        if self.zoom == 1:
            self.render_distance=950
        elif self.zoom == 2:
            self.render_distance=350
        elif self.zoom == 3:
            self.render_distance=250
        self.start_val=1


        






    def entity_add(self):
        """Fonction qui ajoute toute les entité (sauf Ground())
          avec leur textures qui ont pour nom le fichier ou son les sprites"""
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j].get_name() != 'Ground':#Igniore l'entité Ground()
                    entity = Player(self.grid[i][j], i, j, Grid.get_neighborhood(self,i,j,WIND_ROSE) if self.grid[i][j].get_name() == 'Water' else None)#Crée chaque entité avec leur class,leur positions + valeur en fonction de la taille de la fenetre
                    if self.grid[i][j].get_name() == "Humain":#Ajout de l'humain comme centre du monde
                        self.player = entity
                    if self.grid[i][j].get_name() in MOVABLE_ELEMENT:
                        self.entity_group.add(entity, layer=3)#Ajoute les entité qui se deplace au groupe et layer 3
                    elif self.grid[i][j].get_name() in PROPS_ELEMENT:
                        self.entity_group.add(entity, layer=2)#Ajoute les entité qui se deplace au groupe et layer 2
                    else:
                        self.entity_group.add(entity, layer=1)#Ajoute les entité qui se deplace au groupe et layer 1

                    
    def get_collision(self, element):
        """Cette fonction prend en parametre une class Player et qui s'occupe a detecter les collisions de 'element'  
        et renvoie une liste de toute les entitées qui le touche(renvoie une liste de class Element exemple [Herb(),Cow()])"""
        collisions_list=[]
        for cible in self.entity_group:
            if element.entity.get_id() != cible.entity.get_id():#Regarde si l'entité toucher n'est pas lui meme
                if(cible.position[0]>element.position[0]-48 and cible.position[0]<element.position[0]+48):#Regarde si les entité sont sur 'element' sur les axe X
                    if(cible.position[1]>element.position[1]-48 and cible.position[1]<element.position[1]+48):#Regarde si les entité sont sur 'element' sur les axe Y
                        collisions_list.append(cible)
        return collisions_list
    

    def is_render(self, cible):
        """Determine en fonction de la position si l'entité est calculé"""
        if cible.position[0]>self.player.position[0]-self.render_distance and cible.position[0]<self.player.position[0]+self.render_distance:
            if cible.position[1]>self.player.position[1]-self.render_distance and cible.position[1]<self.player.position[1]+self.render_distance:
                return True
        return False


    def start(self):
        """Initialisation du monde"""
        self.entity_add()#Ajoute toute les entitées sur la fenetre pygame
                    
    def entity_count(self, tipe=None):
        counter=0
        entity_dict = {}
        if tipe == MOVABLE_ELEMENT:
            for elt in self.entity_group:
                if elt.name in MOVABLE_ELEMENT:
                    counter+=1
            return counter
        elif tipe == PROPS_ELEMENT:
            for elt in self.entity_group:
                if elt.name in PROPS_ELEMENT:
                    counter+=1
            return counter
        elif tipe == None:
            for elt in self.entity_group:
                counter += 1
                if elt.name in entity_dict:
                    entity_dict[elt.name] += 1
                else:
                    entity_dict[elt.name] = 1
            return entity_dict
        
            


    def kill(self, elt):
        """ Kill l'entité """
        if elt.entity.get_name() not in ["Mort","Damage"]:
            self.entity_group.remove(elt)

            #Ajouter une entité
            entity = Player(Mort(), elt.position[0], elt.position[1], [], False)
            self.entity_group.add(entity, layer=2)
        else:
            self.entity_group.remove(elt)


    def percentage_chance(self, chance:int) -> bool:
        ''' Choisir un pourcentage de chance (entre 0 et 100) que True soit renvoyé.'''
        if chance >= 100:
            return True
        else:
            return choice([False if i != int(chance/2) or chance == 0 else True for i in range(100-chance)])


    def random_attack(self, elt, collision_list:list) -> None:
        ''' Les animaux (sauf l'humain) peuvent attaquer un animal aléatoirement.
        Certains animaux peuvent également se nourrir de l'herbe '''
        list_neighbors = [animal for animal in collision_list if animal.name != 'Water']
        if elt.name != 'Humain' and len(list_neighbors) > 0:
            alea = choice(list_neighbors)
            if elt.entity.is_prey(alea.name):
                if alea.name != 'Herb':
                    alea.entity.losing_life(elt.entity.get_damage())
                    if alea.entity.is_dead():
                        elt.entity.incr_food(alea.entity.get_life_max())
                        self.kill(alea)
                    else:
                        entity = Player(Damage(), elt.position[0], elt.position[1], [], False)
                        self.entity_group.add(entity,layer=3)
                else:
                    alea.entity.decr_bar_value(1)
                    elt.entity.incr_food(1)

    def neighboring_water(self, elt, collision_list:list) -> None:
        """ Si un animal a un voisin 'Water' alors sa bar de soif est régénérée à 100%  """
        for entite in collision_list:
            if entite.name == 'Water':
                elt.entity.reset_drink()
                break   

    def entity_event(self, elt) -> None:
        ''' Exécute les évènements pour les entitées '''
        collision_entity = self.get_collision(elt)
        self.birth(elt,collision_entity)
        elt.entity.set_time_life()
        self.catch_virus(elt)
        self.lose_virus(elt)
        if elt.entity.get_drink()[0] <= elt.entity.get_drink()[1] and elt.entity.get_food()[0] <= elt.entity.get_food()[1]:
            self.neighboring_water(elt, collision_entity)
            self.random_attack(elt, collision_entity)
            self.dying_hunger_thirst(elt)
    
    def dying_hunger_thirst(self, elt) -> None:
        ''' Si un animal est à zéro sur sa bar de soif ou sur sa bar de faim alors il perd 1 de vie '''
        if elt.entity.is_hungry() or elt.entity.is_thirsty():
            elt.entity.losing_life(1)

    def birth(self, elt, collision_list) -> None:
        ''' Si deux animaux de la même espèce et de sexe différent se croisent alors ils font un enfant.
            Il y a 25% de chance que les deux animaux fassent un enfant '''
        if self.percentage_chance(25):
            for entite in collision_list:
                if entite.name == elt.name and entite.entity.get_gender() != elt.entity.get_gender():
                    newAnimal = Animal(elt.name, elt.entity.get_char_repr(), elt.entity.get_life_max())
                    newAnimal.set_parents(entite if entite.entity.get_gender() == 0 else elt, entite if entite.entity.get_gender() == 1 else elt)
                    entity = Player(newAnimal, elt.position[0], elt.position[1], [], False)
                    self.entity_group.add(entity, layer=3)
                    break

    def catch_virus(self, elt) -> None:
        ''' L'animal a 10% de chance d'attraper un virus '''
        if self.percentage_chance(10) and elt.entity.get_virus() == False and elt.name != 'Humain':
            elt.entity.set_virus(True)

    def lose_virus(self, elt) -> None:
        ''' L'animal a 2% de chance de perdre le virus qu'il a attrapé '''
        if self.percentage_chance(2) and elt.entity.get_virus() == True:
            elt.entity.set_virus(False)

    def virus_damage(self, elt) -> None:
        ''' L'animal ayant un virus perd de la vie '''
        if elt.entity.get_virus() == True:
            elt.entity.losing_life(1)

    def print_info_entity(self, pos) -> None:
        """Determine vie un calcule la position du click sur la map grace a la position du click sur la fenetre.Renvoie l'entité a cette position"""
        coli_click=None
        for elt in self.entity_group:
            if self.is_render(elt):
                calc=[pos[0]-485+self.player.position[0],pos[1]-485+self.player.position[1]]
                if(elt.position[0]>calc[0]-24 and elt.position[0]<calc[0]+24):
                    if(elt.position[1]>calc[1]-24 and elt.position[1]<calc[1]+24):
                        coli_click=elt
                        break
        if coli_click != None:
            if coli_click.name not in PROPS_ELEMENT:
                self.stats_entity = elt
            else:
                self.stats_entity = elt
        else:
            self.stats_entity = None
            print("No entity on position(map)",calc,"pos(windows)",pos)
           
    def draw_global_stats(self) -> None:
        """Affiche les données global du monde"""
        self.screen.blit(self.sprite_sheet_stats_G, (795, 250))
        entity_nb = pygame.font.Font(None, 18).render(f"Entity = {self.get_current_animals_count()}" ,True, (255, 255, 255))
        self.screen.blit(entity_nb, (819, 295))

        props_nb = pygame.font.Font(None, 18).render(f"Props = {self.entity_count(PROPS_ELEMENT)}" ,True, (255, 255, 255))
        self.screen.blit(props_nb, (819, 310))
 
    def draw_stats(self):
        """Affiche les données de l'entité selectionner par le click gauche"""
    
        if self.stats_entity != None and self.stats_entity.name not in ["Mort","Damage"]:
        
            self.screen.blit(self.sprite_sheet_stats, (self.rect_x, self.rect_y))

            if self.stats_entity.name in PROPS_ELEMENT:
                entity_name = pygame.font.Font(None, 25).render(str(self.stats_entity.name) ,True, (255, 255, 255))
                self.screen.blit(entity_name, (866, 25))
                valeur_life = 44-((self.stats_entity.entity.get_bar_value()[1] - self.stats_entity.entity.get_bar_value()[0]) / self.stats_entity.entity.get_bar_value()[1] * 44)
                pygame.draw.rect(self.screen, "#FF0000", (837, 88, valeur_life, 2))
                self.screen.blit(self.stats_entity.image, (815, 18))
            else:

                valeur_life = 44-((self.stats_entity.entity.get_life_max() - self.stats_entity.entity.get_bar_life()[0]) / self.stats_entity.entity.get_life_max() * 44)
                valeur_food = 44-((self.stats_entity.entity.get_food()[1] - self.stats_entity.entity.get_food()[0]) / self.stats_entity.entity.get_food()[1] * 44)
                valeur_drink = 44-((self.stats_entity.entity.get_drink()[1] - self.stats_entity.entity.get_drink()[0]) / self.stats_entity.entity.get_drink()[1] * 44)

                pygame.draw.rect(self.screen, "#FF0000", (837, 88, valeur_life, 2))
                pygame.draw.rect(self.screen, "#F07800", (837, 109, valeur_food, 2))
                pygame.draw.rect(self.screen, "#0088E6", (837, 131, valeur_drink, 2))

                entity_name = pygame.font.Font(None, 25).render(str(self.stats_entity.name) ,True, (255, 255, 255))
                self.screen.blit(entity_name, (866, 25))
                entity_parent = pygame.font.Font(None, 25).render(str([p.get_id if p != None else 0 for p in self.stats_entity.entity.get_parents() ]), True, (255, 255, 255))
                self.screen.blit(entity_parent, (891, 53))

                entity_age = pygame.font.Font(None, 25).render(str(self.stats_entity.entity.get_time_life()), True, (255, 255, 255))
                self.screen.blit(entity_age, (832, 147))

                entity_virus = pygame.font.Font(None, 25).render(str(self.stats_entity.entity.get_virus()), True, (255, 255, 255))
                self.screen.blit(entity_virus, (835, 173))

                entity_genre = pygame.font.Font(None, 25).render(str(self.stats_entity.entity.get_gender()), True, (255, 255, 255))
                self.screen.blit(entity_genre, (833, 201))

                entity_damage = pygame.font.Font(None, 25).render(str(self.stats_entity.entity.get_damage()), True, (255, 255, 255))
                self.screen.blit(entity_damage, (905, 147))

                entity_speed = pygame.font.Font(None, 25).render(str(animals[self.stats_entity.name]['speed']), True, (255, 255, 255))
                self.screen.blit(entity_speed, (903, 171))

                entity_weight = pygame.font.Font(None, 25).render(str(animals[self.stats_entity.name]['weight']), True, (255, 255, 255))
                self.screen.blit(entity_weight, (902, 200))

            self.screen.blit(self.stats_entity.image, (815, 18))
        
 





    def update(self):
        ''' Boucle d'actualisation de chaque frame '''

        #boucle qui parcours toute les entité (class Player)
        self.clock -=1
        for elt in self.entity_group:
            if self.is_render(elt):
                if elt.name in MOVABLE_ELEMENT:
                    ###################################################
                    #----------------Boucle toute les frame------------
                    elt.move()#Deplace toute les entitées


                    ###################################################
                    #----------------Boucle toute les 4/1 secondes------------
                    if self.clock%(self.fps/4) == 0:
                        if elt.name == "Damage":
                            self.kill(elt)

                    ###################################################
                    #----------------Boucle toute les secondes------------
                    if self.clock%(self.fps) == 0:
                        self.entity_event(elt)
                    
                    ###################################################
                    #----------------Boucle toute les 5 secondes------------
                    if self.clock%(self.fps*5) == 0:
                        elt.entity.decr_drink(1)
                        elt.entity.decr_food(1)
                        self.virus_damage(elt)

                else: 
                    if self.clock%(self.fps*5) == 0:
                        if elt.entity.get_name() == 'Herb':
                            elt.entity.reset_bar_value()

        if self.clock <= 0:
            self.clock = 3600 
            for elt in self.entity_group:
                if elt.name == "Mort":
                    if self.is_render(elt):
                        self.kill(elt)




        self.entity_group.update()
        self.entity_group.center(self.player.rect.center)

    
    def run(self, screen):
        """Boucle principale de cette class"""
        if self.start_val==1:
            print("Start Initialisation")
            self.start()
            self.screen = screen
            self.start_val=0
        
        clock = pygame.time.Clock()
        self.update()
        
        self.entity_group.draw(self.screen)
    
        self.draw_stats()
        self.draw_global_stats()
        
        pygame.display.flip()
        
        clock.tick(self.fps)


    def get_event(self):
        """Récupere le nom de la fenetre(gere le changement d'affichage)"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.print_info_entity(event.pos)
        return "game"










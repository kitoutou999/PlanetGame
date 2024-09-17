import pygame
import os
import Menu.Option.param as option
from world.config import *
from world.elements import *

class menu():
    def __init__(self,world) -> None:
        
        self.world = world
        self.gap = 30
        # Définir le fond
        self.image_fond = pygame.image.load("Menu/images/fond.png").convert()

        self.largeur_bouton = 240
        self.hauteur_bouton = 126
        repertoire_images = "Menu/images/"
        self.image_bouton_start = pygame.image.load(os.path.join(repertoire_images, "start.png")).convert_alpha()
        self.image_bouton_start = pygame.transform.scale(self.image_bouton_start, (self.largeur_bouton,self.hauteur_bouton))

        self.image_bouton_option = pygame.image.load(os.path.join(repertoire_images, "option.png")).convert_alpha()
        self.image_bouton_option = pygame.transform.scale(self.image_bouton_option, (self.largeur_bouton,self.hauteur_bouton))

        self.image_bouton_quit = pygame.image.load(os.path.join(repertoire_images, "quit.png")).convert_alpha()
        self.image_bouton_quit = pygame.transform.scale(self.image_bouton_quit, (self.largeur_bouton,self.hauteur_bouton))

        # Calculer les coordonnées du centre de la fenêtre
        centre_x = WINDOW_SIZES["menu"][0] // 2
        centre_y = WINDOW_SIZES["menu"][0] // 2+50

        # Calculer les coordonnées des coins supérieurs gauche des boutons
        self.x_bouton_start = centre_x - (self.largeur_bouton // 2)
        self.y_bouton_start = centre_y - (self.hauteur_bouton // 2) - (self.hauteur_bouton+self.gap )

        self.x_bouton_option = centre_x - (self.largeur_bouton // 2)
        self.y_bouton_option = centre_y - (self.hauteur_bouton // 2)

        self.x_bouton_quit = centre_x - (self.largeur_bouton // 2)
        self.y_bouton_quit = centre_y - (self.hauteur_bouton // 2) + (self.hauteur_bouton+self.gap)

    
    def create_entity(self):
        """Initialise le monde en cas de lancement"""
        for animal_type, count in animals.items():
            for _ in range(count["count"]):
                animal = globals()[animal_type]()
                self.world.place_animals([animal])
                
        for props_type, count in props.items():
            for _ in range(count["count"]):
                animal = globals()[props_type]()
                self.world.place_resources([animal])

    def display(self,screen):
        """Affiche les boutons sur le menu de demarage"""
        screen.blit(pygame.transform.scale(self.image_fond, WINDOW_SIZES["menu"]), (0, 0))
        # Ajouter les boutons à la fenêtre
        screen.blit(self.image_bouton_start, (self.x_bouton_start, self.y_bouton_start))
        screen.blit(self.image_bouton_option, (self.x_bouton_option, self.y_bouton_option))
        screen.blit(self.image_bouton_quit, (self.x_bouton_quit, self.y_bouton_quit))

    def get_event(self):
        """Recupere l'evenement de la page"""
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.x_bouton_start <= event.pos[0] <= self.x_bouton_start + self.largeur_bouton and self.y_bouton_start <= event.pos[1] <= self.y_bouton_start + self.hauteur_bouton:               
                    self.create_entity()
                    return "game"
                elif self.x_bouton_option <= event.pos[0] <= self.x_bouton_option + self.largeur_bouton and self.y_bouton_option <= event.pos[1] <= self.y_bouton_option + self.hauteur_bouton:                 
                    return "param"
                elif self.x_bouton_quit <= event.pos[0] <= self.x_bouton_quit + self.largeur_bouton and self.y_bouton_quit <= event.pos[1] <= self.y_bouton_quit + self.hauteur_bouton:
                    return "quit"

            elif event.type == pygame.QUIT:
                return "quit"
        return "menu"

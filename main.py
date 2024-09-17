# -*- coding: utf-8 -*-

#####################################################################################
#         Boucle principale qui gère le changement d'affichage des fenetres         #
#####################################################################################

import pygame
from random import seed
from world.config import WINDOW_SIZES

from world.game import Game
from Menu.menu import menu
from Menu.Option.param import Option

def main():
    pygame.init()
    game = Game()
    menu_instance = menu(game)
    param = Option(game)
    current_interface = "menu"
    previous_interface = None
    
    #Cette boucle gere le changement de fenetres du jeu
    while current_interface != "quit":
        #Actualise la taille de la fenetre en fonction du mode(1 seul fois a chaque changement de menu)
        if current_interface != previous_interface:
            screen = pygame.display.set_mode(WINDOW_SIZES[current_interface])
            pygame.display.set_caption(f"PlanetGame - {current_interface}")
            previous_interface = current_interface

        #Actualise l'affichage de la fenetre en fonction du mode
        if current_interface == "menu":
            menu_instance.display(screen)
            current_interface = menu_instance.get_event()
        elif current_interface == "param":
            param.display(screen)
            current_interface = param.get_event()
        elif current_interface == "game":
            game.run(screen)
            current_interface = game.get_event()

        pygame.display.flip()


    pygame.quit()





if __name__ == '__main__':
    seed(1000)
    #Cree la fenetre pygame
    main()
    





    





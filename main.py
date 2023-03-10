# -*- coding: utf-8 -*-

import pygame


from world.elements import *
from world.affichage import Game
from world.config import *
from random import *

if __name__ == '__main__':

    seed(1000)
    
    planet = Game( PLANET_LONGITUDE_CELLS_COUNT, PLANET_LATITUDE_CELLS_COUNT, Ground())
    
    planet.place_resources([Herb()for _ in range (HERBS_COUNT)])
    planet.place_resources( [ Water()for _ in range (WATERS_COUNT)])

    planet.place_animals([Ane() for _ in range(ANE_COUNT)])
    planet.place_animals([Autruche() for _ in range(AUTRUCHE_COUNT)])
    planet.place_animals([Bizon() for _ in range(BIZON_COUNT)])
    planet.place_animals([Bouc() for _ in range(BOUC_COUNT)])
    planet.place_animals([Bouctin() for _ in range(BOUCTIN_COUNT)])
    planet.place_animals([Buffle() for _ in range(BUFFLE_COUNT)])
    planet.place_animals([Canard() for _ in range(CANARD_COUNT)])
    planet.place_animals([Chameau() for _ in range(CHAMEAU_COUNT)])
    planet.place_animals([Chat() for _ in range(CHAT_COUNT)])
    planet.place_animals([Cheval() for _ in range(CHEVAL_COUNT)])
    planet.place_animals([Chevre() for _ in range(CHEVRE_COUNT)])
    planet.place_animals([Chien() for _ in range(CHIEN_COUNT)])
    planet.place_animals([Chinchila() for _ in range(CHINCHILA_COUNT)])
    planet.place_animals([Cochon() for _ in range(COCHON_COUNT)])
    planet.place_animals([Fennec() for _ in range(FENNEC_COUNT)])
    planet.place_animals([Licorne() for _ in range(LICORNE_COUNT)])
    planet.place_animals([Mouton() for _ in range(MOUTON_COUNT)])
    planet.place_animals([Oie() for _ in range(OIE_COUNT)])
    planet.place_animals([Ours() for _ in range(OURS_COUNT)])
    planet.place_animals([Pingoin() for _ in range(PINGOIN_COUNT)])
    planet.place_animals([Poney() for _ in range(PONEY_COUNT)])
    planet.place_animals([Raton() for _ in range(RATON_COUNT)])
    planet.place_animals([Renard() for _ in range(RENARD_COUNT)])
    planet.place_animals([Renardeau() for _ in range(RENARDEAU_COUNT)])
    planet.place_animals([Sanglier() for _ in range(SANGLIER_COUNT)])
    planet.place_animals([Singe() for _ in range(SINGE_COUNT)])
    planet.place_animals([Tigre() for _ in range(TIGRE_COUNT)])

    planet.place_animals([Vache() for _ in range(VACHE_COUNT)])
    planet.place_animals([Lion() for _ in range(LION_COUNT)])
    planet.place_animals([Souris() for _ in range(SOURIS_COUNT)])
    planet.place_animals([Dragon() for _ in range(DRAGON_COUNT)])


    pygame.init()#Cree la fenetre pygame
    planet.run()#Lance la boucle de refresh de la fenetre pygame




    





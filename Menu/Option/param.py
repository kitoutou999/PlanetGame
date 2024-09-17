import pygame
import os
from random import *
import world.config as config
from world.elements import *



class Option():
    
    def __init__(self,world) -> None:
        pygame.init()
        self.world = world
        self.gap = 8
        self.screen = pygame.display.set_mode((900,900))
        # Définir le fond
        self.image_fond = pygame.image.load("Menu/images/fond_config.png").convert()
        self.screen.blit(pygame.transform.scale(self.image_fond, (900,900)), (0, 0))
        self.sprite_size = 48
        self.sprite_sheet=None
        
        
        self.liste_button_animal=[Button(elt,(10,20),(74,22),8,"animal_list") for elt in config.MOVABLE_ELEMENT]

        self.liste_button_param_1=[Button(elt,(282,149),(32,31),10,"param_1") for elt in config.ENTITY_PARAM]
        self.liste_button_param_10=[Button(elt,(318,149),(32,31),10,"param_10") for elt in config.ENTITY_PARAM]
        self.liste_button_param_n10=[Button(elt,(353,149),(32,31),10,"param_n10") for elt in config.ENTITY_PARAM]
        self.liste_button_param_0=[Button(elt,(388,149),(32,31),10,"param_0") for elt in config.ENTITY_PARAM]


        self.liste_button_param_humain_1=[Button(elt,(596,277),(32,31),10,"param__humain_1") for elt in config.HUMAN_PARAM]
        self.liste_button_param_humain_10=[Button(elt,(632,277),(32,31),10,"param__humain_10") for elt in config.HUMAN_PARAM]
        self.liste_button_param_humain_n10=[Button(elt,(667,277),(32,31),10,"param__humain_n10") for elt in config.HUMAN_PARAM]
        self.liste_button_param_humain_0=[Button(elt,(702,277),(32,31),10,"param__humain_0") for elt in config.HUMAN_PARAM]

        self.button_next_humain=50

        self.BLANC = (255, 255, 255)
        self.GREEN = (40, 180, 99)
        self.police_name = pygame.font.Font(None, 36)
        self.police_values = pygame.font.Font(None, 25)

        self.selecte_entity = 1

    def create_entity(self):
        """Initialise le monde au lancement du jeu"""
        for animal_type, count in config.animals.items():
            for _ in range(count["count"]):
                animal = globals()[animal_type]()
                self.world.place_animals([animal])
                
        for props_type, count in config.props.items():
            for _ in range(count["count"]):
                animal = globals()[props_type]()
                self.world.place_resources([animal])

       


    def entity_stat(self, i):
        """Affiche les stats des entitée a modifié"""
        entity = config.animals[self.liste_button_animal[i].name]
        entity_name = self.police_name.render(self.liste_button_animal[i].name, True, self.GREEN)
        self.screen.blit(entity_name, (187, 68))

        stats = [
            (str(entity["count"]), (202, 157)),
            (str(entity["speed"]), (206, 200)),
            (str(entity["move_size"]), (195, 240)),
            (str(entity["damage"]), (222, 283)),
            (str(entity["food"]), (195, 325)),
            (str(entity["drink"]), (196, 366)),
            (str(entity["weight"]), (220, 408)),
        ]

        for val, pos in stats:
            entity_stat = self.police_values.render(val, True, self.BLANC)
            self.screen.blit(entity_stat, pos)




    def afficher_humain(self):
        """Affiche les sprites d'humain"""
        self.sprite_sheet = pygame.image.load(os.path.join(f"./images/Humain/Humain ({config.HUMAIN_CP+1}).png")).convert_alpha()
        image = pygame.Surface((self.sprite_size , self.sprite_size), pygame.SRCALPHA) # modification de la taille
        image.blit(self.sprite_sheet, (0, 0), (0, 0, self.sprite_size, self.sprite_size))
        image = image.subsurface(image.get_bounding_rect())  # Extraire la zone utilisée
        return image



        
    def humain_stat(self):
        """Affiche les valeurs modifiables de l'humain"""
        # Créer les surfaces de texte une seule fois pour toutes
        entity_name = self.police_name.render(config.HUMAIN_NAME[config.HUMAIN_CP], True, self.GREEN)
        entity_speed = self.police_values.render(str(config.animals["Humain"]["speed"]), True, self.BLANC)
        entity_move_size = self.police_values.render(str(config.animals["Humain"]["move_size"]), True, self.BLANC)
        entity_damage = self.police_values.render(str(config.animals["Humain"]["damage"]), True, self.BLANC)
        entity_food = self.police_values.render(str(config.animals["Humain"]["food"]), True, self.BLANC)
        entity_drink = self.police_values.render(str(config.animals["Humain"]["drink"]), True, self.BLANC)

        # Afficher les surfaces de texte
        self.screen.blit(self.afficher_humain(), (565, 90))
        self.screen.blit(entity_name, (528, 213))
        self.screen.blit(entity_speed, (548, 325))
        self.screen.blit(entity_move_size, (528, 367))
        self.screen.blit(entity_damage, (550, 284))
        self.screen.blit(entity_food, (525, 410))
        self.screen.blit(entity_drink, (534, 452))


    def refresh(self,i):
        """Actualise les valeur du menu"""
        self.screen.blit(pygame.transform.scale(self.image_fond, (900,900)), (0, 0))
        self.humain_stat()
        self.entity_stat(i)


    def display(self,screen):
        self.screen = screen
        self.refresh(self.selecte_entity)
        

    def get_event(self):
        """Recupere les evenement de la fenetre parametre"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(config.MOVABLE_ELEMENT)):
                    if config.MOVABLE_ELEMENT[i] != "Humain" and self.liste_button_animal[i-1].x_button <= event.pos[0] <= self.liste_button_animal[i-1].x_button + self.liste_button_animal[i-1].largeur_bouton and self.liste_button_animal[i-1].y_button <= event.pos[1] <= self.liste_button_animal[i-1].y_button + self.liste_button_animal[i-1].hauteur_bouton:
                        self.selecte_entity = i
                for i in range(len(config.ENTITY_PARAM)):
                    if self.liste_button_param_1[i].x_button <= event.pos[0] <= self.liste_button_param_1[i].x_button + self.liste_button_param_1[i].largeur_bouton and self.liste_button_param_1[i].y_button <= event.pos[1] <= self.liste_button_param_1[i].y_button + self.liste_button_param_1[i].hauteur_bouton:
                        getattr(config, "animals")[config.MOVABLE_ELEMENT[self.selecte_entity]][self.liste_button_param_1[i].name]+=1
                    if self.liste_button_param_10[i].x_button <= event.pos[0] <= self.liste_button_param_10[i].x_button + self.liste_button_param_10[i].largeur_bouton and self.liste_button_param_10[i].y_button <= event.pos[1] <= self.liste_button_param_10[i].y_button + self.liste_button_param_10[i].hauteur_bouton:
                        getattr(config, "animals")[config.MOVABLE_ELEMENT[self.selecte_entity]][self.liste_button_param_10[i].name]+=10
                    if self.liste_button_param_n10[i].x_button <= event.pos[0] <= self.liste_button_param_n10[i].x_button + self.liste_button_param_n10[i].largeur_bouton and self.liste_button_param_n10[i].y_button <= event.pos[1] <= self.liste_button_param_n10[i].y_button + self.liste_button_param_n10[i].hauteur_bouton:
                        getattr(config, "animals")[config.MOVABLE_ELEMENT[self.selecte_entity]][self.liste_button_param_n10[i].name]+=-10
                    if self.liste_button_param_0[i].x_button <= event.pos[0] <= self.liste_button_param_0[i].x_button + self.liste_button_param_0[i].largeur_bouton and self.liste_button_param_0[i].y_button <= event.pos[1] <= self.liste_button_param_0[i].y_button + self.liste_button_param_0[i].hauteur_bouton:
                        getattr(config, "animals")[config.MOVABLE_ELEMENT[self.selecte_entity]][self.liste_button_param_0[i].name]=0
                
                for i in range(len(config.HUMAN_PARAM)):
                    if self.liste_button_param_humain_1[i].x_button <= event.pos[0] <= self.liste_button_param_humain_1[i].x_button + self.liste_button_param_humain_1[i].largeur_bouton and self.liste_button_param_humain_1[i].y_button <= event.pos[1] <= self.liste_button_param_humain_1[i].y_button + self.liste_button_param_humain_1[i].hauteur_bouton:
                        getattr(config, "animals")["Humain"][self.liste_button_param_humain_1[i].name]+=1
                    if self.liste_button_param_humain_10[i].x_button <= event.pos[0] <= self.liste_button_param_humain_10[i].x_button + self.liste_button_param_humain_10[i].largeur_bouton and self.liste_button_param_humain_10[i].y_button <= event.pos[1] <= self.liste_button_param_humain_10[i].y_button + self.liste_button_param_humain_10[i].hauteur_bouton:
                        getattr(config, "animals")["Humain"][self.liste_button_param_humain_10[i].name]+=10
                    if self.liste_button_param_humain_n10[i].x_button <= event.pos[0] <= self.liste_button_param_humain_n10[i].x_button + self.liste_button_param_humain_n10[i].largeur_bouton and self.liste_button_param_humain_n10[i].y_button <= event.pos[1] <= self.liste_button_param_humain_n10[i].y_button + self.liste_button_param_humain_n10[i].hauteur_bouton:
                        getattr(config, "animals")["Humain"][self.liste_button_param_humain_n10[i].name]+=-10
                    if self.liste_button_param_humain_0[i].x_button <= event.pos[0] <= self.liste_button_param_humain_0[i].x_button + self.liste_button_param_humain_0[i].largeur_bouton and self.liste_button_param_humain_0[i].y_button <= event.pos[1] <= self.liste_button_param_humain_0[i].y_button + self.liste_button_param_humain_0[i].hauteur_bouton:
                        getattr(config, "animals")["Humain"][self.liste_button_param_humain_0[i].name]=0
                self.refresh(self.selecte_entity)

                if 674 <= event.pos[0] <= 724 and 115 <= event.pos[1] <= 165:
                    config.HUMAIN_CP = (config.HUMAIN_CP + 1) % 78
                    self.refresh(self.selecte_entity)
                elif 445 <= event.pos[0] <= 495 and 115 <= event.pos[1] <= 165:
                    config.HUMAIN_CP = (config.HUMAIN_CP - 1) % 78
                elif 742 <= event.pos[0] <= 895 and 823 <= event.pos[1] <= 895:
                    self.create_entity()
                    return "game"

        return "param"

    
#Class pour crée des bouton plus simplement et vite(pas toalement optimiser)
class Button():
    __bt_count = -1
    __last="animal_list"
    

    @classmethod
    def bt_reset(cls) -> int:
        cls.__bt_count=0

    @classmethod
    def get_bt_count(cls) -> int:
        return cls.__bt_count

    @classmethod
    def incr_bt_count(cls) -> None:
        cls.__bt_count += 1
    
    @classmethod
    def get_last(cls) -> int:
        return cls.__last

    @classmethod
    def set_last(cls,name) -> None:
        cls.__last =name

    def __init__(self,name,start,dim_button,gap,tipe):
        self.type=tipe
        if self.type != Button.get_last():
            Button.set_last(self.type)
            Button.bt_reset()
        else:
            Button.incr_bt_count()
        
        self.name=name
        self.largeur_bouton = dim_button[0]
        self.hauteur_bouton = dim_button[1]
        self.start = start
        self.gap=gap
        self.x_button = self.start[0]
        if self.get_bt_count() != 0 :
            self.y_button = self.start[1]+(self.hauteur_bouton+self.gap)*self.get_bt_count() 
        else: 
            self.y_button = self.start[1]

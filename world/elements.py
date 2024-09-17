# -*- coding: utf-8 -*-

#####################################################################################
#      importation des bibliothèques nécéssaires au fonctionnement des classes      #
#####################################################################################

from random import randint, choice
from world.config import *

#####################################################################################################################
#      Création des classes : Element, Animal, Resource ainsi que leurs héritiers (vaches, herbes, sol, etc...)     #
#####################################################################################################################

class Element():

    __ids_count = 0

    @classmethod
    def get_ids_count(cls) -> int:

        return cls.__ids_count

    @classmethod
    def incr_ids_count(cls) -> None:

        cls.__ids_count += 1

    @classmethod
    def decr_ids_count(cls) -> None:

        cls.__ids_count -= 1

    def __init__(self, name:str, char_repr:str):

        Element.incr_ids_count()
        self.__id = Element.get_ids_count()
        self.__name = name
        self.__char_repr = char_repr
        
    def get_name(self) -> str:

        return self.__name

    def get_id(self) -> int:

        return self.__id

    def get_char_repr(self) -> str:

        return self.__char_repr

    def __repr__(self) -> str:
        return f"{self.get_char_repr()}"


class Animal(Element):

    def __init__(self, name:str, char_repr:str, life_max:int):
        
        Element.__init__(self, name, char_repr)
        self.__time_life:list = 0
        ''' 0 -> femelle et 1 -> mâle '''
        self.__gender:int = randint(0,1)
        self.__bar_life:list = [animals[name]['weight'], animals[name]['weight']]
        self.__current_direction:list = [choice([-1, 0, 1]), choice([-1, 0, 1])] 

        self.__bar_drink:list = [animals[name]['drink'], animals[name]['drink']]
        self.__bar_food:list = [animals[name]['food'], animals[name]['food']]

        self.__speed:int = animals[name]['speed']
        self.__move_size:int = animals[name]['move_size']
        self.__damage:int =  animals[name]['damage']
        self.__weight:int = animals[name]['weight']

        self.__prey:list = animals[name]['prey']

        ''' [maman, papa] '''
        self.__parents:list = [None, None]

        self.__virus:bool = False

    def get_time_life(self) -> int:
        """Renvoie le temps de vie de l'entitée"""
        return self.__time_life

    def set_time_life(self) -> None:
        """Determine le temp de vie de l'entitée"""
        self.__time_life += 1

    def get_gender(self) -> int:
        """Renvoie le genre de l'entitée"""
        return self.__gender

    def get_life_max(self) -> int:
        """Recupere la vie maximum de l'entitée"""
        return self.__bar_life[1]

    def get_life(self) -> int:
        """Recupere la vie actuelle de l'entitée"""
        return self.__bar_life[0]

    def get_bar_life(self) -> [int, int]:
        """Récupere la bar de vie de l'entitée"""
        return self.__bar_life

    def is_dead(self) -> bool:
        """Regarde si l'entitée est morte(inferieur ou egal a 0)"""
        if(self.get_life() <= 0):
            return True
        else:
            return False

    def recovering_life(self, value:int) -> None: 
        """Recupere de la vie"""
        if(self.get_life() + value <= self.get_life_max()):
            self.__bar_life[0] += value
        else:
            self.__bar_life[0] = self.get_life_max()

    def losing_life(self, value:int) -> None:
        """Decremente de value la vie de l'entitée"""
        if self.__bar_life[0] - value >= 0:
            self.__bar_life[0] -= value
        else:
            self.__bar_life[0]=0

    def get_current_direction(self) -> [int, int]:
        """Applique la direction a l'entitée"""
        return self.__current_direction

    def set_direction(self, line_direction:int, column_direction:int) -> None:
        """Applique une direction a l'entitée"""
        self.__current_direction = [line_direction, column_direction]

    def get_drink(self) -> [int, int]:
        """Renvoie la valeur de soif de l'entitée"""
        return self.__bar_drink 

    def decr_drink(self, value:int) -> None:
        """Decremente de value la soif de l'entitée"""
        if self.__bar_drink[0] - value >= 0:
            self.__bar_drink[0] -= value
        else:
            self.__bar_drink[0]=0

    def incr_drink(self, value:int) -> None:
        """Incremente al valeur de soif de l'entitée"""

        if  self.__bar_drink[0] + value <= self.__bar_drink[1]:
            self.__bar_drink[0] += value
        else:
            self.__bar_drink[0] = self.__bar_drink[1]

    def reset_drink(self) -> None:
        """Reset la valeur de soif de l'entitée"""

        self.__bar_drink[0] = self.__bar_drink[1]

    def is_thirsty(self) -> bool:
        ''' Retourne True si la bar de soif est à zéro '''
        if self.__bar_drink[0] == 0:
            return True
        else:
            return False

    def get_food(self) -> [int, int]:
        """Renvoie la valeur de nourriture de l'entitée"""
        return self.__bar_food

    def decr_food(self, value:int) -> None:
        """Decremente la nourriture de l'entitée"""
        if self.__bar_food[0] - value >= 0:
            self.__bar_food[0] -= value
        else:
            self.__bar_food[0]=0

    def incr_food(self, value:int) -> None:
        """Incremente la nourriture de l'entitée"""

        if self.__bar_food[0] + value <= self.__bar_food[1]:
            self.__bar_food[0] += value
        else:
            self.__bar_food[0]=self.__bar_food[1]
    
    def is_hungry(self) -> bool:
        ''' Retourne True si la bar de faim est à zéro '''
        if self.__bar_food[0] == 0:
            return True
        else:
            return False

    def get_damage(self) -> int:
        """Renvoie les degats de l'entitée"""
        return self.__damage

    def get_prey(self) -> list:
        """Renvoie la liste de ses proies"""
        return self.__prey

    def is_prey(self, name:str) -> bool:
        """Renvoie si l'entité est dans la liste de ses proies"""

        if name in self.__prey:
            return True
        else:
            return False

    def get_parents(self) -> list:
        """Renvoie les parents d'un enfant"""
        return self.__parents
        
    def set_parents(self, mother:str = None, father:str = None) -> None:
        """Determine les parents d'un enfant"""
        self.__parents[0] = mother
        self.__parents[1] = father

    def get_virus(self) -> bool:
        """Renvoie l'etat(virus) de l'entitée"""
        return self.__virus

    def set_virus(self, state:bool) -> None:
        """Applique l'etat(virus) de l'entitée"""
        self.__virus = state

class Resource(Element):

    def __init__(self, name:str, char_repr:str):

        Element.__init__(self, name, char_repr)

        self.__bar_value = [props[name]['value'], props[name]['value']]

    def get_bar_value(self) -> [int, int]:
        """Renvoie la valeur de la ressource"""
        return self.__bar_value

    def decr_bar_value(self, value:int) -> None:
        """decremente la valeur de la ressource"""
        if self.__bar_value[0] - value >= 0:
            self.__bar_value[0] -= value

    def reset_bar_value(self) -> None:
        """Reset la valeur de la ressource"""
        self.__bar_value[0] = self.__bar_value[1]

    def is_available(self) -> bool:
        ''' Vérifie si la ressource est encore disponible (c'est-à-dire que sa valeur n'est pas à zéro) '''
        if self.__bar_value[0] == 0:
            return False
        else:
            return True


######################################################################################
#              classe concernant le sol sur lequel marche les animaux                #
######################################################################################


class Ground(Element):

    def __init__(self):

        Element.__init__(self, "Ground", ".")


######################################################################################
#                      classes concernant les ressources du jeu                      #
######################################################################################


class Herb(Resource):

    def __init__(self):

        Resource.__init__(self, "Herb", "\U0001F33F")
        

class Water(Resource):

    def __init__(self):

        Resource.__init__(self, "Water", "\U0001F4A7")


#######################################################################################
#                        classes concernant les animaux du jeu                        #
#######################################################################################


class Humain(Animal):

    def __init__(self):

        Animal.__init__(self, "Humain", "\U0001F600", 100)

class Souris(Animal):

    def __init__(self):

        Animal.__init__(self, "Souris", "\U0001F42D", 2)


class Dragon(Animal):

    def __init__(self):

        Animal.__init__(self, "Dragon", "\U0001F432", 20)


class Vache(Animal):

    def __init__(self):

        Animal.__init__(self, "Vache", "\U0001F42E", 5)


class Autruche(Animal):

    def __init__(self):

        Animal.__init__(self, "Autruche", "\U0001F983", 5)


class Bizon(Animal):

    def __init__(self):

        Animal.__init__(self, "Bizon", "\U0001F9AC", 5)
 

class Bouc(Animal):

    def __init__(self):

        Animal.__init__(self, "Bouc", "\U0001F40F", 5)


class Bouctin(Animal):

    def __init__(self):

        Animal.__init__(self, "Bouctin", "\U0001F40F", 5)


class Buffle(Animal):

    def __init__(self):

        Animal.__init__(self, "Buffle", "\U0001F403", 5)
 

class Canard(Animal):

    def __init__(self):

        Animal.__init__(self, "Canard", "\U0001F986", 5)


class Chameau(Animal):

    def __init__(self):

        Animal.__init__(self, "Chameau", "\U0001F42A", 5)
 

class Chat(Animal):

    def __init__(self):

        Animal.__init__(self, "Chat", "\U0001F431", 5)
 

class Cheval(Animal):

    def __init__(self):

        Animal.__init__(self, "Cheval", "\U0001F434", 5)
 

class Chevre(Animal):

    def __init__(self):

        Animal.__init__(self, "Chevre", "\U0001F410", 5)
 

class Chien(Animal):

    def __init__(self):

        Animal.__init__(self, "Chien", "\U0001F436", 5)
 

class Chinchila(Animal):

    def __init__(self):

        Animal.__init__(self, "Chinchila", "\U0001F429", 5)
 

class Cochon(Animal):

    def __init__(self):

        Animal.__init__(self, "Cochon", "\U0001F437", 5)
 

class Dragon(Animal):

    def __init__(self):

        Animal.__init__(self, "Dragon", "\U0001F432", 5)


class Fennec(Animal):

    def __init__(self):

        Animal.__init__(self, "Fennec", "\U0001F98A", 5)
 

class Licorne(Animal):

    def __init__(self):

        Animal.__init__(self, "Licorne", "\U0001F984", 5)
 

class Mouton(Animal):

    def __init__(self):

        Animal.__init__(self, "Mouton", "\U0001F411", 5)
 

class Oie(Animal):

    def __init__(self):

        Animal.__init__(self, "Oie", "\U0001F9A2", 5)
 

class Ours(Animal):

    def __init__(self):

        Animal.__init__(self, "Ours", "\U0001F43B", 5)
 

class Pingoin(Animal):

    def __init__(self):

        Animal.__init__(self, "Pingoin", "\U0001F427", 5)
 

class Poney(Animal):

    def __init__(self):

        Animal.__init__(self, "Poney", "\U0001F40E", 5)


class Raton(Animal):

    def __init__(self):

        Animal.__init__(self, "Raton", "\U0001F99D", 5)
 

class Renard(Animal):

    def __init__(self):

        Animal.__init__(self, "Renard", "\U0001F98A", 5)


class Renardeau(Animal):

    def __init__(self):

        Animal.__init__(self, "Renardeau", "\U0001F98A", 5)
 

class Sanglier(Animal):

    def __init__(self):

        Animal.__init__(self, "Sanglier", "\U0001F417", 5)
 

class Singe(Animal):

    def __init__(self):

        Animal.__init__(self, "Singe", "\U0001F435", 5)


class Tigre(Animal):

    def __init__(self):

        Animal.__init__(self, "Tigre", "\U0001F42F", 5)        


######################################################################################
#              classes concernant la mort et les dommages des animaux                 #
######################################################################################


class Mort(Animal):

    def __init__(self):

        Animal.__init__(self, "Mort", "\U0001F480", 10)


class Damage(Animal):

    def __init__(self):

        Animal.__init__(self, "Damage", "\U0001F4A2", 10)
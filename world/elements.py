# -*- coding: utf-8 -*-

from random import *

from world.planets import *

class Element():

    __ids_count = 0

    @classmethod
    def get_ids_count(cls):
        return cls.__ids_count

    @classmethod
    def incr_ids_count(cls):
        cls.__ids_count += 1

    def __init__(self, name, char_repr):
        Element.incr_ids_count()
        self.__id = Element.get_ids_count()
        self.__name = name
        self.__char_repr = char_repr
        
    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_char_repr(self):
        return self.__char_repr

    def __repr__(self) -> str:
        return f"{self.get_char_repr()}"


class Animal(Element):

    def __init__(self,name,char_repr,life_max) -> None:
        
        super().__init__(name,char_repr)
        self.__age=0
        self.__gender = randint(0,1)
        self.__bar_life = [life_max,life_max]
        self.__current_direction = [choice([-1, 0, 1]), choice([-1, 0, 1])] 
        
    def get_age(self):
        return self.__age

    def ageing(self):
        self.__age+=1

    def get_gender(self):
        return self.__gender

    def get_life_max(self):
        return self.__bar_life[1]

    def get_life(self):
        return self.__bar_life[0]

    def get_bar_life(self):
        return self.__bar_life
    
    def is_alive(self):
        if(self.get_life() <= 0 ):
            return False
        else:
            return True

    def is_dead(self):
        if(self.get_life() <= 0 ):
            return True
        else:
            return False

    def recovering_life(self,value):
        if(self.get_life()+value<=self.get_life_max()):
            self.__bar_life[0]+=value
        else:
            self.__bar_life[0]=self.get_life_max()

    def losing_life(self,value):
        self.__bar_life[0]-=value

    def get_current_direction(self):
        return self.__current_direction

    def set_direction(self,line_direction,column_direction):
        self.__current_direction = [line_direction,column_direction]

    # def __repr__(self):
    #     if(self.get_gender()==0):
    #         return f"{self.get_char_repr()} : {self.get_name()} {self.get_id()} ( femelle de {self.get_age()} an (s)) \n Barre de vie : {self.get_life()}/{self.get_life_max()}"
    #     else:
    #         return f"{self.get_char_repr()} : {self.get_name()} {self.get_id()} ( male de {self.get_age()} an (s)) \n Barre de vie : {self.get_life()}/{self.get_life_max()}"


class Resource(Element):
    def __init__(self,name,char_repr,value) -> None:
        super().__init__(name,char_repr)
        self.__value=value

    def get_value(self):
        return self.__value
        

class Ground(Element):
    def __init__(self):
        super().__init__("Ground", ".")


class Herb(Resource):
    def __init__(self) -> None:
        super().__init__("Herb", "\U0001F33F", 1)
        

class Water(Resource):
    def __init__(self) -> None:
        super().__init__("Water", "\U0001F4A7", 2)




class Souris(Animal):
    def __init__(self) -> None:
        super().__init__("Souris","\U0001F42D",2)


class Lion(Animal):
    def __init__(self) -> None:
        super().__init__("Lion","\U0001F981",10)


class Dragon(Animal):
    def __init__(self) -> None:
        super().__init__("Dragon","\U0001F432",20)
    

class Vache(Animal):
    def __init__(self) -> None:
        super().__init__("Vache", "\U0001F42E", 5)      

class Ane(Animal):
    def __init__(self) -> None:
        super().__init__("Ane", "?", 5)

class Autruche(Animal):
    def __init__(self) -> None:
        super().__init__("Autruche", "?", 5)

class Bizon(Animal):
    def __init__(self) -> None:
        super().__init__("Bizon", "?", 5)

class Bouc(Animal):
    def __init__(self) -> None:
        super().__init__("Bouc", "?", 5)

class Bouctin(Animal):
    def __init__(self) -> None:
        super().__init__("Bouctin", "?", 5)

class Buffle(Animal):
    def __init__(self) -> None:
        super().__init__("Buffle", "?", 5)

class Canard(Animal):
    def __init__(self) -> None:
        super().__init__("Canard", "?", 5)


class Chameau(Animal):
    def __init__(self) -> None:
        super().__init__("Chameau", "?", 5)

class Chat(Animal):
    def __init__(self) -> None:
        super().__init__("Chat", "?", 5)

class Cheval(Animal):
    def __init__(self) -> None:
        super().__init__("Cheval", "?", 5)

class Chevre(Animal):
    def __init__(self) -> None:
        super().__init__("Chevre", "?", 5)

class Chien(Animal):
    def __init__(self) -> None:
        super().__init__("Chien", "?", 5)

class Chinchila(Animal):
    def __init__(self) -> None:
        super().__init__("Chinchila", "?", 5)

class Cochon(Animal):
    def __init__(self) -> None:
        super().__init__("Cochon", "?", 5)

class Dragon(Animal):
    def __init__(self) -> None:
        super().__init__("Dragon", "?", 5)

class Fennec(Animal):
    def __init__(self) -> None:
        super().__init__("Fennec", "?", 5)

class Licorne(Animal):
    def __init__(self) -> None:
        super().__init__("Licorne", "?", 5)

class Lion(Animal):
    def __init__(self) -> None:
        super().__init__("Lion", "?", 5)

class Mouton(Animal):
    def __init__(self) -> None:
        super().__init__("Mouton", "?", 5)

class Oie(Animal):
    def __init__(self) -> None:
        super().__init__("Oie", "?", 5)

class Ours(Animal):
    def __init__(self) -> None:
        super().__init__("Ours", "?", 5)

class Pingoin(Animal):
    def __init__(self) -> None:
        super().__init__("Pingoin", "?", 5)

class Poney(Animal):
    def __init__(self) -> None:
        super().__init__("Poney", "?", 5)

class Raton(Animal):
    def __init__(self) -> None:
        super().__init__("Raton", "?", 5)

class Renard(Animal):
    def __init__(self) -> None:
        super().__init__("Renard", "?", 5)

class Renardeau(Animal):
    def __init__(self) -> None:
        super().__init__("Renardeau", "?", 5)

class Sanglier(Animal):
    def __init__(self) -> None:
        super().__init__("Sanglier", "?", 5)

class Singe(Animal):
    def __init__(self) -> None:
        super().__init__("Singe", "?", 5)

class Tigre(Animal):
    def __init__(self) -> None:
        super().__init__("Tigre", "?", 5)
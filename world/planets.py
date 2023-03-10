# -*- coding: utf-8 -*-

from random import *

from world.elements import *
from world.grid import Grid
from world.config import *


class PlanetAlpha(Grid):
    def __init__(self,longitude_cells_count,latitude_cells_count,ground) -> None:
        self.NORTH,self.EAST,self.SOUTH,self.WEST = (-1,0),(0,1),(1,0),(0,-1)
        self.NORTH_EAST,self.SOUTH_EAST,self.SOUTH_WEST,self.NORTH_WEST = (-1,1),(1,1),(1,-1),(-1,-1)
        self.CARDINAL_POINT = (self.NORTH,self.EAST,self.SOUTH,self.WEST)
        self.WIND_ROSE = (self.NORTH,self.NORTH_EAST,self.EAST,self.SOUTH_EAST,self.SOUTH,self.SOUTH_WEST,self.WEST,self.NORTH_WEST)
        self.__current_animals_count=0
        self.__ground=ground
        self.longitude_cells_count=longitude_cells_count
        self.latitude_cells_count=latitude_cells_count
        Grid.__init__(self, [[ground for _ in range(longitude_cells_count)] for _ in range(latitude_cells_count)])

    # def __eq__(self,other):
    #     print("====================================")
    #     return isinstance(other, self.__class__)

    def get_current_animals_count(self):
        return self.__current_animals_count
    
    def incr_current_animals_count(self):
        self.__current_animals_count+=1

    def decr_current_animals_count(self):
        self.__current_animals_count-=1

    def get_ground(self):
        return self.__ground
    
    def is_free_place(self,cell_number):
        if(self.get_cell(cell_number)=='.'):
            return False
        return True

    def get_random_free_place(self):
        free_place = self.get_same_value_cell_numbers(self.__ground)
        if free_place == []:
            return -1
        else:
            return choice(free_place)
        
    def place_resources(self,resources):
        for elt in resources:
            self.set_cell(self.get_random_free_place(),elt)

    def place_animals(self,animal):
        for elt in animal:
            self.incr_current_animals_count()
            self.set_cell(self.get_random_free_place(),elt)


    def get_count(self, value):
        return len([elt for line in self.grid for elt in line if type(elt)==type(value)])
    





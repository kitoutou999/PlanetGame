# -*- coding: utf-8 -*-

import random

class Grid:

    def __init__(self, grid_init):

        self.grid = grid_init
        self.lines_count = len(grid_init)
        self.columns_count = len(grid_init[0]) if len(grid_init) else 0

    def fill_random(self, values):
        self.grid = [[random.choice(values)
                      for _ in range(self.columns_count)]
                     for _ in range(self.lines_count)]

    def get_line(self, line_number):
        """ Extrait la ligne numéro 'line_number' de la grille."""
        return self.grid[line_number]

    def get_column(self, column_number):
        """ Extrait la colonne numéro 'column_number' de la grille."""
        return [line[column_number] for line in self.grid]


    def get_grid_str(self, separator='\t'):
        return '\n'.join(self.get_line_str(line_number, separator) for line_number in range(self.lines_count))

    def get_grid_consol(self):
        for line in self.grid:
            chaine=[]
            for elt in line:
                chaine.append(" "+str(elt)+" ")
            print(chaine)
        
    

    def get_diagonal(self):
        """ Extrait la diagonale de la grille."""
        diagonal_size = min(self.lines_count, self.columns_count)
        return [self.grid[line_number][line_number]
                for line_number in range(diagonal_size)]

    def get_anti_diagonal(self):
        """ Extrait l'antidiagonale de la grille."""
        diagonal_size = min(self.lines_count, self.columns_count)
        return [self.grid[line_number][self.columns_count - line_number - 1]
                for line_number in range(diagonal_size)]


    def is_square(self):
        """ Teste si la grille a le même nombre de lignes et de colonnes."""
        return self.lines_count == self.columns_count


    def get_coordinates_from_cell_number(self, cell_number):
        """ Converti un numéro de case 'cell_number' de la grille vers les coordonnées (ligne, colonne)
        correspondants."""
        return cell_number // self.columns_count, cell_number % self.columns_count

    def get_cell_number_from_coordinates(self, line_number, column_number):
        """ Converti les coordonnées ('line_number', 'column_number') de la grille vers le numéro de case
        correspondant."""
        return line_number * self.columns_count + column_number

    def get_cell(self, cell_number):
        """ Extrait la valeur de la grille en position 'cell_number'."""
        line_number, column_number = self.get_coordinates_from_cell_number(cell_number)
        return self.grid[line_number][column_number]

    def set_cell(self, cell_number, value):
        """ Positionne la valeur 'value' dans la case 'cell_number' de la grille."""
        line_number, column_number = self.get_coordinates_from_cell_number(cell_number)
        self.grid[line_number][column_number] = value

    def get_neighbour(self, line_number, column_number, delta, is_tore=True):
        """ Retourne le voisin de la cellule ('line_number', 'column_number') de la grille. La définition de voisin
        correspond à la distance positionnelle indiquée par le 2-uplet 'delta' = (delta_ligne, delta_colonne). La case
        voisine est alors (ligne + delta_ligne, colonne + delta_colonne).
                Si 'is_tore' est à 'True' le voisin existe toujours en considérant la grille comme un tore.
                Si 'is_tore' est à 'False' retourne 'None' lorsque le voisin est hors de la grille."""
        new_line_number, new_column_number = line_number + delta[0], column_number + delta[1]
        if is_tore:
            return self.grid[new_line_number % self.lines_count][new_column_number % self.columns_count]
        if 0 <= new_line_number < self.lines_count and 0 <= new_column_number < self.columns_count:
            return self.grid[new_line_number][new_column_number]
        return None

    def get_neighborhood(self, line_number, column_number, deltas, is_tore=True):
        """ Retourne la liste des N voisins de la position ('lins_number', 'column_number') dans la grille correspondant
         aux N 2-uplet (delta_ligne, delta_colonne) fournis par la liste deltas.
                Si 'is_tore' est à 'True' le voisin existe toujours en considérant la grille comme un tore.
                Si 'is_tore' est à 'False' un voisin hors de la grille n'est pas considéré."""
        return [self.get_neighbour(line_number, column_number, delta, is_tore)
                for delta in deltas]
    
    def has_equal_values(self, value):
        """Regarde si la listes est rempli de la meme entité"""
        return all([all([type(grid_value) == type(value) for grid_value in line]) for line in self.grid])
    
    def get_same_value_cell_numbers(self, value):
        
        return [cell_number for cell_number in range(self.lines_count * self.columns_count) if type(self.get_cell(cell_number)) == type(value)]

    def get_line_str(self, line_number, separator='\t'):
        return separator.join(str(value) for value in self.grid[line_number])

    



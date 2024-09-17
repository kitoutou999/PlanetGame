# -*- coding: utf-8 -*-

NORTH, EAST, SOUTH, WEST = (-1,0), (0,1), (1,0), (0,-1)
NORTH_EAST, SOUTH_EAST, SOUTH_WEST, NORTH_WEST = (-1,1), (1,1), (1,-1), (-1,-1)
WIND_ROSE = (NORTH_WEST, WEST, SOUTH_WEST, SOUTH, SOUTH_EAST, EAST, NORTH_EAST, NORTH)

PLANET_LONGITUDE_CELLS_COUNT = 30
PLANET_LATITUDE_CELLS_COUNT = 30
WORLD_SIZE = [PLANET_LONGITUDE_CELLS_COUNT*48, PLANET_LATITUDE_CELLS_COUNT*48]
PLANET_PYGAME_SIZE_GRID = 48 #taille de la grille pour pas depacer de la fenetre pygame
PYGAME_SIZE = 960+10 #Taille de la fenetre pygame + espace de 5 pixel sur les bordure de la fenetre pour un meilleur rendu

WINDOW_SIZES = {
    "menu":(970,970),
    "game":(PYGAME_SIZE,PYGAME_SIZE),
    "param":(900,900)
}

ZOOM = 1
FPS = 40

PROPS_ELEMENT = ["Herb", "Water"]
MOVABLE_ELEMENT = ["Humain", "Autruche", "Bizon", "Bouc", "Bouctin", "Buffle", "Canard", "Chameau", "Chat", "Cheval", "Chevre", "Chien", "Chinchila", "Cochon", "Dragon", "Fennec", "Licorne", "Mouton", "Oie", "Ours", "Pingoin", "Poney", "Raton", "Renard", "Renardeau", "Sanglier", "Singe", "Souris", "Tigre", "Vache","Mort","Damage"]

HUMAIN_CP = 0 #Compteur d'id d'humain pour le menu config
HUMAIN_NAME = ['Ragnar', 'Astrid', 'Fenrir', 'Medusa', 'Castor', 'Althea', 'Evelina', 'Hera', 'Xander', 'Persephone', 'Zarek', 'Rhiannon', 'Soren', 'Ariana', 'Rainer', 'Eirwyn', 'Kian', 'Adira', 'Rune', 'Laelia', 'Enzo', 'Clio', 'Orion', 'Nyx', 'Poseidon', 'Fenrir', 'Lilith', 'Cyrus', 'Seraphina', 'Raze', 'Kian', 'Astrid', 'Fane', 'Vayne', 'Hestia', 'Laelia', 'Axton', 'Athena', 'Poseidon', 'Ryker', 'Raze', 'Adara', 'Raze', 'Calliope', 'Thetis', 'Zephyrine', 'Thor', 'Althea', 'Blade', 'Evelina', 'Helios', 'Lyra', 'Orion', 'Zahara', 'Jarek', 'Athena', 'Kian', 'Eirwyn', 'Fane', 'Laelia', 'Zarek', 'Athena', 'Raze', 'Astra', 'Orpheus', 'Zahara', 'Raze', 'Kyren', 'Galen', 'Thor', 'Phoenix', 'Kyren', 'Xander', 'Kaida', 'Valtor', 'Zephyrine', 'Thor', 'Atlas']

ENTITY_PARAM = ["count", "speed", "move_size", "damage", "food", "drink", "weight"]
HUMAN_PARAM = ["damage", "speed", "move_size", "food", "drink"]
#Nombre de props
#Valeur que l'entité donne en nourriture ou en eau

props = {
    "Herb": {
        "count":10,
        "value" : 10
    },
    "Water": {
        "count":20,
        "value" : 10
    }
}

animals = {
    "Humain": {
        "count": 1,
        "speed": 6,
        "move_size" : 10,
        "damage": 1,
        "weight": 65,
        "food": 150,
        "drink": 150, 
        "prey": []
        },

    "Autruche": {
        "count": 1,
        "speed": 2,
        "move_size" : 10,
        "damage": 1,
        "weight": 100,
        "food": 150,
        "drink": 150, 
        "prey": ['Herb']
        },

    "Bizon": {
        "count": 1,
        "speed": 2,
        "move_size" : 1,
        "damage": 1,
        "weight": 600,
        "food": 150,
        "drink": 150, 
        "prey": ['Herb']
        },

    "Bouc": {
        "count": 1,
        "speed": 4,
        "move_size" : 7,
        "damage": 1,
        "weight": 90,
        "food": 150,
        "drink": 150, 
        "prey": ['Herb']
        } ,

    "Bouctin": {
        "count": 1,
        "speed": 4,
        "move_size" : 10,
        "damage": 1,
        "weight": 70,
        "food": 150,
        "drink": 150, 
        "prey": ['Herb']
        },           

    "Buffle": {
        "count": 1,
        "speed": 2,
        "move_size" : 10,
        "damage": 1,
        "weight": 600,
        "food": 150,
        "drink": 150, 
        "prey": ['Herb']
        },  

    "Canard": {
        "count": 1,
        "speed": 2,
        "move_size" : 10,
        "damage": 1,
        "weight": 1,
        "food": 150,
        "drink": 150, 
        "prey": ['Herb']
        },  

    "Chameau": {
        "count": 1,
        "speed": 3,
        "move_size" : 10,
        "damage": 1,
        "weight": 480,
        "food": 150,
        "drink": 150, 
        "prey": ['Herb']
        },  

    "Chat": {
        "count": 1,
        "speed": 2,
        "move_size" : 10,
        "damage": 1,
        "weight": 5,
        "food": 150,
        "drink": 150, 
        "prey": ['Souris', 'Herb']
        },  

    "Cheval": {
        "count": 1,
        "speed": 4,
        "move_size" : 10,
        "damage": 1,
        "weight": 800,
        "food": 150,
        "drink": 150, 
        "prey": ['Herb']
        },  

    "Chevre": {
        "count": 1,
        "speed": 4,
        "move_size" : 10,
        "damage": 1,
        "weight": 80,
        "food": 150,
        "drink": 150, 
        "prey": ['Herb']
        },  

    "Chien": {
        "count": 1,
        "speed": 2,
        "move_size" : 10,
        "damage": 1,
        "weight": 30,
        "food": 150,
        "drink": 150, 
        "prey": ['Chat', 'Herb']
        },  

    "Chinchila": {
        "count": 1,
        "speed": 1,
        "move_size" : 10,
        "damage": 1,
        "weight": 1,
        "food": 150,
        "drink": 150, 
        "prey": ['Herb']
        },  

    "Cochon": {
        "count": 1,
        "speed": 1,
        "move_size" : 10,
        "damage": 1,
        "weight": 145,
        "food": 150,
        "drink": 150, 
        "prey": ['Herb']
        },  

    "Dragon": {
        "count": 1,
        "speed": 2,
        "move_size" : 10,
        "damage": 500,
        "weight": 1000,
        "food": 150,
        "drink": 150, 
        "prey": [ 'Tigre', 'Ours', 'Renard', 'Renardeau', 'Fennec', 'Autruche', 'Bizon', 'Bouc', 'Bouctin', 'Buffle', 'Canard', 'Chameau', 'Chat', 'Cheval', 'Chevre', 'Chien', 'Chinchila', 'Cochon', 'Licorne', 'Mouton', 'Oie', 'Pingoin', 'Poney', 'Raton', 'Sanglier', 'Singe', 'Souris', 'Vache']
        },  

    "Fennec": {
        "count": 10,
        "speed": 0,
        "move_size" : 10,
        "damage": 1,
        "weight": 100,
        "food": 150,
        "drink": 150, 
        "prey": ['Herb', 'Renard', 'Renardeau', 'Fennec', 'Autruche', 'Bizon', 'Bouc', 'Bouctin', 'Buffle', 'Canard', 'Chameau', 'Chat', 'Cheval', 'Chevre', 'Chien', 'Chinchila', 'Cochon', 'Licorne', 'Mouton', 'Oie', 'Pingoin', 'Poney', 'Raton', 'Sanglier', 'Singe', 'Souris', 'Vache']
        },  

    "Licorne": {
        "count": 1,
        "speed": 4,
        "move_size" : 10,
        "damage": 1,
        "weight": 800,
        "food": 150,
        "drink": 150, 
        "prey": ['Herb']
        },   

    "Mouton": {
        "count": 1,
        "speed": 2,
        "move_size" : 10,
        "damage": 1,
        "weight": 100,
        "food": 150,
        "drink": 150, 
        "prey": ['Herb']
        },  

    "Oie": {
        "count": 1,
        "speed": 4,
        "move_size" : 10,
        "damage": 1,
        "weight": 5,
        "food": 150,
        "drink": 150, 
        "prey": ['Herb']
        },  

    "Ours": {
        "count": 1,
        "speed": 3,
        "move_size" : 10,
        "damage": 1,
        "weight": 600,
        "food": 150,
        "drink": 150, 
        "prey": [ 'Herb','Tigre', 'Ours', 'Renard', 'Renardeau', 'Fennec', 'Autruche', 'Bizon', 'Bouc', 'Bouctin', 'Buffle', 'Canard', 'Chameau', 'Chat', 'Cheval', 'Chevre', 'Chien', 'Chinchila', 'Cochon', 'Licorne', 'Mouton', 'Oie', 'Pingoin', 'Poney', 'Raton', 'Sanglier', 'Singe', 'Souris', 'Vache']
        },  

    "Pingoin": {
        "count": 1,
        "speed": 1,
        "move_size" : 10,
        "damage": 1,
        "weight": 1,
        "food": 150,
        "drink": 150, 
        "prey": ['Herb']
        },  

    "Poney": {
        "count": 1,
        "speed": 1,
        "move_size" : 10,
        "damage": 1,
        "weight": 250,
        "food": 150,
        "drink": 150, 
        "prey": ['Herb']
        },  

    "Raton": {
        "count": 1,
        "speed": 2,
        "move_size" : 10,
        "damage": 1,
        "weight": 8,
        "food": 150,
        "drink": 150, 
        "prey": ['Herb']
        },  

    "Renard": {
        "count": 1,
        "speed": 3,
        "move_size" : 10,
        "damage": 1,
        "weight": 10,
        "food": 150,
        "drink": 150, 
        "prey": ['Herb', 'Renard', 'Renardeau', 'Fennec', 'Autruche', 'Bizon', 'Bouc', 'Bouctin', 'Buffle', 'Canard', 'Chameau', 'Chat', 'Cheval', 'Chevre', 'Chien', 'Chinchila', 'Cochon', 'Licorne', 'Mouton', 'Oie', 'Pingoin', 'Poney', 'Raton', 'Sanglier', 'Singe', 'Souris', 'Vache']
        },  

    "Renardeau": {
        "count": 1,
        "speed": 0,
        "move_size" : 10,
        "damage": 1,
        "weight": 8,
        "food": 150,
        "drink": 150, 
        "prey": ['Herb', 'Renard', 'Renardeau', 'Fennec', 'Autruche', 'Bizon', 'Bouc', 'Bouctin', 'Buffle', 'Canard', 'Chameau', 'Chat', 'Cheval', 'Chevre', 'Chien', 'Chinchila', 'Cochon', 'Licorne', 'Mouton', 'Oie', 'Pingoin', 'Poney', 'Raton', 'Sanglier', 'Singe', 'Souris', 'Vache']
        },  

    "Sanglier": {
        "count": 1,
        "speed": 2,
        "move_size" : 10,
        "damage": 1,
        "weight": 90,
        "food": 150,
        "drink": 150, 
        "prey": ['Herb']
        },  

    "Singe": {
        "count": 1,
        "speed": 3,
        "move_size" : 10,
        "damage": 1,
        "weight": 4,
        "food": 150,
        "drink": 150, 
        "prey": ['Herb']
        },  

    "Souris": {
        "count": 1,
        "speed": 2,
        "move_size" : 10,
        "damage": 1,
        "weight": 1,
        "food": 150,
        "drink": 150, 
        "prey": ['Herb']
        },  

    "Tigre": {
        "count": 1,
        "speed": 3,
        "move_size" : 10,
        "damage": 1,
        "weight": 300,
        "food": 150,
        "drink": 150, 
        "prey": [ 'Herb','Tigre', 'Ours', 'Renard', 'Renardeau', 'Fennec', 'Autruche', 'Bizon', 'Bouc', 'Bouctin', 'Buffle', 'Canard', 'Chameau', 'Chat', 'Cheval', 'Chevre', 'Chien', 'Chinchila', 'Cochon', 'Licorne', 'Mouton', 'Oie', 'Pingoin', 'Poney', 'Raton', 'Sanglier', 'Singe', 'Souris', 'Vache']
        },  

    "Vache": {
        "count": 1,
        "speed": 1,
        "move_size" : 10,
        "damage": 1,
        "weight": 900,
        "food": 150,
        "drink": 150, 
        "prey": ['Herb']
        },  

    "Mort": {
        "count": 1,
        "speed": 0,
        "move_size" : 0,
        "damage": 0,
        "weight": 10,
        "food": 0,
        "drink": 0, 
        "prey": []
        },  

    "Damage": {
        "count": 1,
        "speed": 0,
        "move_size" : 0,
        "damage": 0,
        "weight": 10,
        "food": 0,
        "drink": 0, 
        "prey": []
        }
}





from animals import *
from plants import *
from pygame import image
from pygame.transform import scale
from utils import Dimension


class Icons:

    def __init__(self, dim: Dimension):
        self.icons = {
            Antelope.name: scale(image.load('resources/antelope.png'), dim.as_tuple()),
            Fox.name: scale(image.load('resources/fox.png'), dim.as_tuple()),
            Human.name: scale(image.load('resources/girl.png'), dim.as_tuple()),
            Sheep.name: scale(image.load('resources/sheep.png'), dim.as_tuple()),
            CyberSheep.name: scale(image.load('resources/cybersheep.png'), dim.as_tuple()),
            Turtle.name: scale(image.load('resources/turtle.png'), dim.as_tuple()),
            Wolf.name: scale(image.load('resources/wolf.png'), dim.as_tuple()),
            Belladonna.name: scale(image.load('resources/belladonna.png'), dim.as_tuple()),
            Grass.name: scale(image.load('resources/grass.png'), dim.as_tuple()),
            Guarana.name: scale(image.load('resources/guarana.png'), dim.as_tuple()),
            Sosnowsky.name: scale(image.load('resources/sosnovsky.png'), dim.as_tuple()),
            SowThistle.name: scale(image.load('resources/sowthistle.png'), dim.as_tuple()),
            'potion': scale(image.load('resources/potion.png'), dim.as_tuple()),
            'bar': image.load('resources/green.png')
        }

    def __getitem__(self, item):
        return self.icons[item]

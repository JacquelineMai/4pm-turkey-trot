import pygame
from gameConstants import Dimensions
from groundConst import LevelOne
from berry import Berry
from spider import Spider
from spider import Hor_Spider


class Ground:
    # ground object will be initialized with a 2 lists containing
    # info for the spiders and berries

    def __init__(self, level, g):
        self.spiders = []
        self.foods = []
        self.h_spiders = []
        self.start(level, g)

    def start(self, level, g):
        for b in LevelOne.g.value[level][g][0]:
            self.foods.append(Berry(b[0], b[1]))
        for s in LevelOne.g.value[level][g][1]:
            self.spiders.append(Spider(s[0], s[1]*3, s[2]))
            
            #scaling for computers with lower pixel density
            #dividing by 3 for now; if this is too slow for your
            #computer, comment out the line below and uncomment
            #the one above
            #self.spiders.append(Spider(s[0], s[1], s[2]))

        for h in LevelOne.g.value[level][g][2]:
            self.h_spiders.append(Hor_Spider(h[0], h[1], h[2]))

    def food_pick(self, idx):
        del self.foods[idx]

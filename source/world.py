import pygame
from player import Player
from ground import Ground

from gameConstants import Color
from gameConstants import Dimensions
from gameConstants import Fonts
from groundConst import LevelOne


class World:
    def __init__(self):
        self.player = Player()
        self.obstacles = []
        self.events = []
        self.buttons = []
        self.texts = []
        self.objects = []
        self.mouse = None
        self.click = None
        # start = 0, end game = 1, ground1 = 2, ground2 = 3
        self.state = 0
        self.pressed_key = None
        self.ground = []
        self.end = False
        self.level = 0
        self.cleared_level = {1}
        self.pause = False

    def update(self):
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

    def start(self):
        self.player = Player()
        self.ground = []
        for i in range(len(LevelOne.g.value[self.level - 1])):
            self.ground.append(Ground(self.level - 1, i))

    # print(self.ground)

    def run(self):
        self.buttons = []
        self.texts = []
        self.objects = []

        # pause menu
        if self.pause:
            self.texts.append(('Resume Game', Color.WHITE.value, 400, 175, Fonts.SMALLFONT.value))
            if 325 + 150 > self.mouse[0] > 325 and 150 + 50 > self.mouse[1] > 150:
                self.buttons.append((325, 150, 150, 50, Color.BRIGHT_GREEN.value))
                if self.click[0] == 1:
                    self.pause = False
            else:
                self.buttons.append((325, 150, 150, 50, Color.GREEN.value))

            self.texts.append(('Return to Menu', Color.WHITE.value, 400, 275, Fonts.SMALLFONT.value))
            if 325 + 150 > self.mouse[0] > 325 and 250 + 50 > self.mouse[1] > 250:
                self.buttons.append((325, 250, 150, 50, Color.BRIGHT_GREEN.value))
                if self.click[0] == 1:
                    self.state = 0
                    self.pause = False
            else:
                self.buttons.append((325, 250, 150, 50, Color.GREEN.value))

            self.texts.append(('Quit Game', Color.WHITE.value, 400, 375, Fonts.SMALLFONT.value))
            if 325 + 150 > self.mouse[0] > 325 and 350 + 50 > self.mouse[1] > 350:
                self.buttons.append((325, 350, 150, 50, Color.BRIGHT_RED.value))
                if self.click[0] == 1:
                    pygame.quit()
                    quit()
            else:
                self.buttons.append((325, 350, 150, 50, Color.RED.value))
            return

        # start game
        if self.state == 0:
            self.buttons.append((285, 75, 230, 50, Color.WHITE.value))
            self.texts.append(('Turkey Trot!', Color.BLACK.value, 400, 100, Fonts.BASICFONT.value))
            self.texts.append(('Start Game', Color.WHITE.value, 400, 375, Fonts.SMALLFONT.value))
            # make the button bright if mouse is on it
            if 350 + 100 > self.mouse[0] > 350 and 350 + 50 > self.mouse[1] > 350:
                self.buttons.append((350, 350, 100, 50, Color.BRIGHT_GREEN.value))
                # switch state if user click
                if self.click[0] == 1:
                    self.state = 2
            else:
                self.buttons.append((350, 350, 100, 50, Color.GREEN.value))
            
        # end game
        elif self.state == 1:
            if not self.end:
                self.texts.append(('You didn\'t make it...', Color.BLACK.value, 400, 100, Fonts.BASICFONT.value))
                self.buttons.append((240, 75, 320, 50, Color.WHITE.value))
            elif self.player.score >= 20 and self.end:
                self.texts.append(('You did it!', Color.BLACK.value, 400, 100, Fonts.BASICFONT.value))
                self.buttons.append((310, 75, 180, 50, Color.WHITE.value))
                self.cleared_level.add(self.level + 1)
            elif self.player.score <=20 and self.end:
                self.texts.append(('Not enough food...', Color.BLACK.value, 400, 100, Fonts.BASICFONT.value))
                self.buttons.append((220, 75, 350, 50, Color.WHITE.value))
            self.buttons.append((275, 175, 250, 50, Color.WHITE.value))
            self.texts.append(
            ('Your Score:' + str(self.player.score), Color.BLACK.value, 400, 200, Fonts.BASICFONT.value))
            self.texts.append(('Start Again', Color.WHITE.value, 400, 375, Fonts.SMALLFONT.value))
            self.texts.append(('Exit Game', Color.WHITE.value, 400, 525, Fonts.SMALLFONT.value))
            # draw and detect start again button
            if 350 + 100 > self.mouse[0] > 350 and 350 + 50 > self.mouse[1] > 350:
                self.buttons.append((350, 350, 100, 50, Color.BRIGHT_GREEN.value))
                if self.click[0] == 1:
                    self.state = 2
                    self.player = Player()
                    self.ground = []
                    self.pressed_key = None
            else:
                self.buttons.append((350, 350, 100, 50, Color.GREEN.value))
            if 350 + 100 > self.mouse[0] > 350 and 500 + 50 > self.mouse[1] > 500:
                self.buttons.append((350, 500, 100, 50, Color.BRIGHT_RED.value))
                if self.click[0] == 1:
                    pygame.quit()
                    quit()
            else:
                self.buttons.append((350, 500, 100, 50, Color.RED.value))

        #map screen
        elif self.state == 2:
            #if berry clicked
            if 1 in self.cleared_level:
                if 70 + 200 > self.mouse[0] > 200 and 70 + 200 > self.mouse[1] >200:
                    self.buttons.append((200, 200, 70, 70, Color.BRIGHT_GREEN.value))
                    if self.click[0] == 1:
                        self.level = 1
                        self.start()
                        self.state = 3
                else:
                    self.buttons.append((200, 200, 70, 70, Color.GREEN.value))
            else:
                if 70 + 200 > self.mouse[0] > 200 and 70 + 200 > self.mouse[1] >200:
                    self.buttons.append((200, 200, 70, 70, Color.BRIGHT_RED.value))
                else:
                    self.buttons.append((200, 200, 70, 70, Color.RED.value))

            #if pumpkin clicked
            if 2 in self.cleared_level:
                if 70 + 310 > self.mouse[0] > 310 and 70 + 400 > self.mouse[1] >400:
                    self.buttons.append((310, 400, 70, 70, Color.BRIGHT_GREEN.value))
                    if self.click[0] == 1:
                        self.level = 2
                        self.start()
                        self.state = 3
                else:
                    self.buttons.append((310, 400, 70, 70, Color.GREEN.value))
            else:
                if 70 + 310 > self.mouse[0] > 310 and 70 + 400 > self.mouse[1] >400:
                    self.buttons.append((310, 400, 70, 70, Color.BRIGHT_RED.value))
                else:
                    self.buttons.append((310, 400, 70, 70, Color.RED.value))

            #if turkey clicked
            if 3 in self.cleared_level:
                if 70 + 500 > self.mouse[0] > 500 and 70 + 250 > self.mouse[1] >250:
                    self.buttons.append((500, 250, 70, 70, Color.BRIGHT_GREEN.value))
                    if self.click[0] == 1:
                        self.level = 3
                        self.start()
                        self.state = 3
                else:
                    self.buttons.append((500, 250, 70, 70, Color.GREEN.value))
            else:
                if 70 + 500 > self.mouse[0] > 500 and 70 + 250 > self.mouse[1] >250:
                    self.buttons.append((500, 250, 70, 70, Color.BRIGHT_RED.value))
                else:
                    self.buttons.append((500, 250, 70, 70, Color.RED.value))

         # ground 1, 2, 3, 4, 5, 6
        elif self.state == 3:
            self.end = False
            self.trackObjects()
            self.obstacles.append((350,500,100,50))
            if self.player.x >= 780:
                self.state += 1
                self.player.x = 10
        elif self.state in [4, 5]:
            self.trackObjects()
            if self.player.x >= 780:
                self.state += 1
                self.player.x = 10
            if self.player.x < 10:
                self.state -= 1
                self.player.x = 779
        elif self.state == 6:
            self.trackObjects()
            if self.player.x >= 780:
                self.end = True
                self.state = 1
            if self.player.x < 10:
                self.state -= 1
                self.player.x = 779
    
        else:
            print("Unknown state", self.state)

    def trackObjects(self):
        self.objects.append(self.player)
        self.user_input()
        for s in self.ground[self.state - 3].spiders:
            if self.check_col(self.player, s):
                if self.player.hit():
                    self.state = 1

        for h in self.ground[self.state - 3].h_spiders:
            if self.check_col(self.player, h):
                h.delta = -h.delta
                if self.player.hit():
                    
                    self.state = 1
     
        for b_idx, b in enumerate(self.ground[self.state - 3].foods):
            if self.check_col(self.player, b):
                self.player.pick()
                self.ground[self.state - 3].food_pick(b_idx)
        
        self.buttons.append((1, 10, 100, 30, Color.WHITE.value))
        self.texts.append(
                ('Score:' + str(self.player.score), Color.BLACK.value, 50, 25, Fonts.SMALLFONT.value))

    def check_col(self, sprite1, sprite2):
        return pygame.sprite.collide_rect(sprite1, sprite2)

    def user_input(self):
        # detect user key press, tell player to move, record key pressed until key up
        if self.pressed_key is not None:
            if self.pressed_key == pygame.K_a:
                self.player.move('left')
            elif self.pressed_key == pygame.K_d:
                self.player.move('right')
            elif self.pressed_key == pygame.K_SPACE:
                self.player.move('jump')
            elif self.pressed_key == pygame.K_w:
                self.player.move('jump')
        for event in self.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.pause = True
                elif event.key == pygame.K_a:
                    self.player.move('left')
                    self.pressed_key = pygame.K_a
                elif event.key == pygame.K_d:
                    self.player.move('right')
                    self.pressed_key = pygame.K_d
                elif event.key == pygame.K_SPACE:
                    self.player.move('jump')
                elif event.key == pygame.K_w:
                    self.player.move('jump')
                else:
                    print("Unknown key")
            elif event.type == pygame.KEYUP and self.pressed_key is not None and event.key == self.pressed_key:
                self.pressed_key = None

    def refresh(self, events):
        # the function being called each game loop
        self.update()
        self.events = events
        self.run()
        self.player.refresh(self.events)
        if self.state > 2:
            if not self.pause:
                for s in self.ground[self.state - 3].spiders:
                    s.update()
                for h in self.ground[self.state - 3].h_spiders:
                    h.update()
            return self.texts, self.buttons, self.objects, self.ground[self.state - 3]
        else:
            return self.texts, self.buttons, self.objects, None


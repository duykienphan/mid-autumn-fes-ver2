import pygame
import sys
from settings import *
from background import Background
import ui
import time

class Menu:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background()
        self.click_sound = pygame.mixer.Sound(f"Assets/Sounds/pop.wav")
        self.level = 1
        with open('DIFFICULTY.txt', 'w') as file:
            file.write(str(self.level))

    def draw(self):
        self.background.draw(self.surface)
        # draw title
        ui.draw_text(self.surface, GAME_TITLE, (SCREEN_WIDTH//2, 230), COLORS["title"], font=FONTS["big"],
                    shadow=True, shadow_color=(0,0,0), pos_mode="center")


    def update(self):
        self.draw()
        if ui.button(self.surface, 320, "START", click_sound=self.click_sound):
            return "game"
        
        if ui.button(self.surface, 455+BUTTONS_SIZES[1]*1.5, "LEVEL", click_sound=self.click_sound):
            if self.level == 1:
                self.level = 2
                with open('DIFFICULTY.txt', 'w') as file:
                    file.write(str(self.level))
            elif self.level == 2:
                self.level = 1
                with open('DIFFICULTY.txt', 'w') as file:
                    file.write(str(self.level))
            time.sleep(0.2)
            # draw the level
            print(f"Level {self.level}")

        if ui.button(self.surface, 320+BUTTONS_SIZES[1]*1.5, "QUIT", click_sound=self.click_sound):
           pygame.quit()
           sys.exit()
        
        ui.draw_text(self.surface, f"Level : {self.level}", (SCREEN_WIDTH//1.13, SCREEN_HEIGHT-35), COLORS["score"], font=FONTS["small"],
                    shadow=True, shadow_color=(255,255,255))

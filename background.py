import pygame
import image
from settings import *

class Background:
    def __init__(self):
        self.image = image.load("Assets/bg.png", size=(SCREEN_WIDTH, SCREEN_HEIGHT), convert="default")
        self.win_bg = image.load("Assets/win_bg.png", size=(SCREEN_WIDTH, SCREEN_HEIGHT), convert="default")
        self.lose_bg = image.load("Assets/lose_bg.png", size=(SCREEN_WIDTH, SCREEN_HEIGHT), convert="default")


    def draw(self, surface):
        image.draw(surface, self.image, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), pos_mode="center")

    def win_bg_display(self, surface):
        image.draw(surface, self.win_bg, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), pos_mode="center")

    def lose_bg_display(self, surface):
        image.draw(surface, self.lose_bg, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), pos_mode="center")
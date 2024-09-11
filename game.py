import pygame
import time
import random
from settings import *
from background import Background
from hand import Hand
from hand_tracking import HandTracking
from mooncake import MoonCake
from rabbit import Rabbit
import cv2
import ui
import imutils
from menu import Menu

class Game:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background()
        self.menu = Menu(self.surface)

        # Load camera
        self.cap = cv2.VideoCapture(0)

        self.sounds = {}
        self.sounds["pop"] = pygame.mixer.Sound(f"Assets/Sounds/pop.wav")
        self.sounds["pop"].set_volume(SOUNDS_VOLUME)
        self.sounds["screaming"] = pygame.mixer.Sound(f"Assets/Sounds/screaming.wav")
        self.sounds["screaming"].set_volume(SOUNDS_VOLUME)
        self.sounds["win"] = pygame.mixer.Sound(f"Assets/Sounds/Win.wav")
        self.sounds["win"].set_volume(SOUNDS_VOLUME-0.7)
        self.sounds["lose"] = pygame.mixer.Sound(f"Assets/Sounds/lose.wav")
        self.sounds["lose"].set_volume(SOUNDS_VOLUME-0.7)


    def reset(self): # reset all the needed variables
        self.hand_tracking = HandTracking()
        self.hand = Hand()
        self.object = []
        self.object_spawn_timer = 0
        self.score = 0
        self.game_start_time = time.time()


    def spawn_object(self):
        t = time.time()
        if t > self.object_spawn_timer:
            self.object_spawn_timer = t + MOONCAKE_SPAWN_TIME

            # increase the probability that the insect will be a bee over time
            nb = (GAME_DURATION-self.time_left)/GAME_DURATION * 100  / 2  # increase from 0 to 50 during all  the game (linear)
            if random.randint(0, 100) < nb:
                self.object.append(Rabbit())
            else:
                self.object.append(MoonCake())

            # spawn a other mosquito after the half of the game
            if self.time_left < GAME_DURATION/2:
                self.object.append(MoonCake())

    def load_camera(self):
        windows_size = 330
        _, self.frame = self.cap.read()
        self.frame = imutils.resize(self.frame, width=windows_size)

    def set_hand_position(self):
        self.frame = self.hand_tracking.scan_hands(self.frame)
        (x, y) = self.hand_tracking.get_hand_center()
        self.hand.rect.center = (x, y)

    def draw(self):
        # draw the background
        self.background.draw(self.surface)
        # draw the moon cakes
        for insect in self.object:
            insect.draw(self.surface)
        # draw the hand
        self.hand.draw(self.surface)
        # draw the score
        ui.draw_text(self.surface, f"Score : {self.score}", (5, 5), COLORS["score"], font=FONTS["small"],
                    shadow=True, shadow_color=(255,255,255))
        # draw the time left
        timer_text_color = (160, 40, 0) if self.time_left < 5 else COLORS["timer"] # change the text color if less than 5s left
        ui.draw_text(self.surface, f"Time left : {self.time_left}", (SCREEN_WIDTH//1.2, 5),  timer_text_color, font=FONTS["small"],
                    shadow=True, shadow_color=(255,255,255))

    def game_time_update(self):
        self.time_left = max(round(GAME_DURATION - (time.time() - self.game_start_time), 1), 0)


    def update(self):
        self.load_camera()
        self.set_hand_position()
        self.game_time_update()

        self.draw()

        if self.time_left > 0:
            self.flag = 0
            self.spawn_object()
            (x, y) = self.hand_tracking.get_hand_center()
            self.hand.rect.center = (x, y)
            self.hand.left_click = self.hand_tracking.hand_closed
            print("Hand closed", self.hand.left_click)
            if self.hand.left_click:
                self.hand.image = self.hand.image_smaller.copy()
            else:
                self.hand.image = self.hand.orig_image.copy()
            self.score = self.hand.kill_objects(self.object, self.score, self.sounds)
            for insect in self.object:
                insect.move()

        else: # when the game is over
            if self.score >= 10:
                self.background.win_bg_display(self.surface)
                if self.flag == 0:
                    self.sounds["win"].play()
                    self.flag = 1
            else:
                self.background.lose_bg_display(self.surface)
                if self.flag == 0:
                    self.sounds["lose"].play()
                    self.flag = 1
            if ui.button(self.surface, 600, "Continue", click_sound=self.sounds["pop"]):
                time.sleep(0.2)
                return "menu"

        cv2.imshow("Hand tracking", self.frame)
        cv2.waitKey(1)

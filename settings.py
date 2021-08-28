import pygame as p
import ctypes


class Settings:
    def __init__(self) -> None:
        ### Screen size and init
        user32 = ctypes.windll.user32
        height = round(user32.GetSystemMetrics(1) * 0.92)
        self.W, self.H = height, height
        self.screen = p.display.set_mode((self.W, self.H))
        
        ### Background
        self.bgColor = (176, 156, 156)
        
        
        
        ### PLAYER SETTINGS ###
        self.playerHealth = {
            "beginner": 200,
            "easy" : 100,
            "normal" : 50,
            "hard" : 25,
            "veryHard" : 10,
            "hardcore" : 1
        }
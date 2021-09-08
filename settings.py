import pygame as p
#import ctypes
from random import choice
import os


class Settings:
    def __init__(self) -> None:
        ### Screen size and init
        """
        user32 = ctypes.windll.user32
        height = round(user32.GetSystemMetrics(1) * 0.92)
        self.W, self.H = height, height
        """
        
        ### Screen
        self.screen = p.display.set_mode((0,0),p.DOUBLEBUF | p.FULLSCREEN)
        self.W, self.H = self.screen.get_width(), self.screen.get_height()
        
        ### Background
        self.bgColor = (15, 0, 61)
        self.BgCircleColor = (209, 254, 0)
        self.circleSize = 15
        self.noise = 125
        
        ### Fonts
        self.playerFont = p.font.SysFont(choice(p.font.get_fonts()), self.H // 35, True)
        self.playerLeftClickAmmoFontColor = (255, 255, 255)
        self.playerRightClickAmmoFontColor = (255, 255, 255)
        
        
        ### Rate of enemy spawning
        ### 10: 1 in every run of program main loop(REAAAALLLYYY FAST)
        self.spawnRate = 600
        
        ### Max number of enemies to be drawn on screen at once (Loading time is heavily impacted)
        self.waitingEnemyNumber = 100
            
        
        
        ### Music
        ###self.backgroundMusic = p.mixer.Sound(os.path.join(os.path.dirname(__file__), "music", "themesong.wav"))
        
        ### Framerate
        self.FPS = 60
        
        ### Difficulty
        self.difficulty = "hard"
        
        ### PLAYER SETTINGS ###
        self.playerSize = (self.H // 25 , self.H // 25)
        self.playerSpeed = 2
        self.playerLeftShootingCapacity = 25
        self.playerRightShootingCapacity = 5
        self.rightBulletCooldown = 7000 # Milliseconds
        self.numberOfBullets = 60 ### Has to be bigger than the capacity of the two magazines
        self.bulletColor = (255,255,255)
        self.reloadTime = 5000 ### Milliseconds
        
        self.playerHealth = {
            "beginner": 200,
            "easy" : 100,
            "normal" : 50,
            "hard" : 25,
            "veryHard" : 10,
            "hardcore" : 1
        }
        
        ### ENEMY SETTINGS ###
        
        self.enemySize = {
            "beginner": 30,
            "easy" : 40,
            "normal" : 70,
            "hard" : 125,
            "veryHard" : 280,
            "hardcore" : 300
        }
        
        
        self.enemySpeed = {
            "beginner": 0.7,
            "easy" : 1,
            "normal" : 1.2,
            "hard" : 1.6,
            "veryHard" : 2,
            "hardcore" : 2.3
        }
    
        
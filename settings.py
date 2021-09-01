import pygame as p
#import ctypes


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
        
        ### Rate of enemy spawning
        ### 10: 1 in every run of program main loop(REAAAALLLYYY FAST)
        self.spawnRate = 600
        
        ### Number of enemies / level (Loading time is heavily impacted)
        self.waitingEnemyNumber = {
            "beginner": 50,
            "easy" : 100,
            "normal" : 150, 
            "hard" : 200,
            "veryHard" : 300,
            "hardcore" : 500
        }
        
        self.FPS = 60
        
        ### Difficulty
        self.difficulty = "normal"
        
        ### PLAYER SETTINGS ###
        self.playerSize = (self.H // 25 , self.H // 25)
        self.playerSpeed = 2
        self.playerShootingCapacity = 25
        self.numberOfBullets = 60 ### Has to be bigger than the capacity of magazine
        self.bulletColor = (0,0,0)
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
    
        
import pygame as p
import os
from settings import Settings

class Player:
    def __init__(self, map, skin="basic") -> None:
        self.settings = Settings()
        self.map = map ### Later on this will tell which map the player is playing on
        self.skin = skin ### Later on the skin will be changeable
        self.difficulty = self.settings.difficulty
        """
        playerHealth : 200, 100, 50, 25, 10, 1
        """
        self.health = self.settings.playerHealth[self.difficulty]
        self.image = self.createPlayer(self.getImagePath(self.skin))
        self.rect = self.image.get_rect()
        self.x, self.y = self.settings.W // 2 - self.image.get_width() // 2, self.settings.H // 2  - self.image.get_height() // 2
        self.rect.x, self.rect.y = self.x, self.y
    
    def getImagePath(self, skin) -> str:
        ### CWD
        filepath = os.path.dirname(__file__)
        
        ### Whole path with skin name
        return os.path.join(filepath, "img", f"{skin}.png")
    
    
    
    def createPlayer(self, path) -> p.Surface:
        ### Get the image
        image = p.image.load(path)
        ### Transform the image
        image = p.transform.scale(image, (self.settings.playerSize))
        return image
        
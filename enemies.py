import pygame as p
from pygame.sprite import Sprite
from random import randint
import os
from settings import Settings

class Enemy(Sprite):
    
    def __init__(self) -> None:
        super().__init__()
        self.settings = Settings()
        self.difficulty = self.settings.difficulty
        self.image = self.createEnemy(self.getImagePath())
        self.rect = self.image.get_rect()
        self.x, self.y = self.rect.x, self.rect.y
        
        
        
    def getImagePath(self) -> str:
        ### CWD
        filepath = os.path.dirname(__file__)
        
        ### Number of pictures of enemy creatures
        numberOfEnemyPicture = len(os.listdir(os.path.join(filepath, "img","enemies")))
        
        ### Whole path with enemy name
        return os.path.join(filepath, "img","enemies", f"{randint(1, numberOfEnemyPicture)}.png")
    
    
    
    def createEnemy(self, path) -> p.Surface:
        ### Get the image
        image = p.image.load(path)
        ### Transform the image
        size = randint(15, self.settings.enemySize[self.difficulty])
        image = p.transform.scale(image, (size, size))
        return image
        
    
    
    
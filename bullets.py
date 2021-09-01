import pygame as p
from settings import Settings
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, radius, damage, screen, pos):
        super().__init__()
        self.settings = Settings()
        self.pos = pos
        self.screen = screen
        self.radius = radius
        self.damage = damage
        self.middleCoo = (self.settings.W // 2, self.settings.H // 2)
        self.color = self.settings.bulletColor
        self.rect = p.Rect(self.middleCoo[0], self.middleCoo[1], radius * 5, radius * 5)
        self.speed = 5
        self.rect.x, self.rect.y = self.middleCoo[0], self.middleCoo[1]
        self.shotX, self.shotY = None, None
        
        
    
    def update(self, xPos, yPos) -> None:
        if not self.shotX:
            self.shotX, self.shotY = xPos - self.middleCoo[0], yPos - self.middleCoo[1]
            
        x, y = self.shotX, self.shotY
        xNegative, yNegative = 1, 1
        if x < 0:
            xNegative = -1
        if y < 0:
            yNegative = -1
        absX, absY = abs(x), abs(y)
        if absX > absY:
            self.rect.x += self.speed * xNegative
            self.rect.y += self.speed * (absY / absX) * yNegative
        elif absY > absX:
            self.rect.y += self.speed * yNegative
            self.rect.x += self.speed * (absX / absY) * xNegative
        else:
            self.rect.x += self.speed * xNegative
            self.rect.y += self.speed * yNegative
            
            
    def checkCollision(self, enemies) -> bool or p.sprite.Sprite:
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                ### Reset the pos
                self.resetBullet()
                return enemy
        if 0 >= self.rect.x or self.rect.x >= self.settings.W or 0 >= self.rect.y or self.rect.y >= self.settings.H:
            ### Reset the pos
            self.resetBullet()
            return "Out"
        return False
    
    
    def draw(self) -> p.Rect:
        p.draw.rect(self.screen, self.color, self.rect)
    
    
    def resetBullet(self) -> None:
        self.shotX, self.shotY = None, None
        self.rect.x, self.rect.y = self.middleCoo
        
        
    ### SETTERS
    
    def setRadius(self, radius):
        self.radius = radius
        
    
    def setDamage(self, damage):
        self.damage = damage
        
        
    def setColor(self, color):
        self.color = color
        
        
    def setSpeed(self, speed):
        self.speed = speed
    
    
    
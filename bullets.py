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
        self.startingRadius = radius
        self.damage = damage
        self.width = 0
        self.leftClick = None
        self.startingDamage = damage
        self.middleCoo = (self.settings.W // 2, self.settings.H // 2)
        self.color = self.settings.bulletColor
        self.rect = p.Rect(self.middleCoo[0], self.middleCoo[1], radius, radius)
        self.speed = 5
        self.rect.x, self.rect.y = self.middleCoo[0], self.middleCoo[1]
        self.shotX, self.shotY = None, None
        
        self.currentTick = None
        
        
    
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
                return enemy
        if 0 >= self.rect.x or self.rect.x >= self.settings.W or 0 >= self.rect.y or self.rect.y >= self.settings.H:
            return "Out"
        return False
    
    
    def draw(self) -> p.Rect:
        if self.leftClick:
            p.draw.circle(self.screen, self.color, (self.rect.x, self.rect.y), self.radius, self.width)
        else:
            if not self.currentTick:
                self.currentTick = p.time.get_ticks()
            if self.currentTick + 30 <= p.time.get_ticks():
                p.draw.circle(self.screen, self.color, (self.rect.x, self.rect.y), self.radius, self.width)
                self.currentTick = p.time.get_ticks()
                self.radius += 1
        #p.draw.rect(self.screen, self.color, self.rect)
    
    
    def reset(self) -> None:
        self.shotX, self.shotY = None, None
        self.rect.x, self.rect.y = self.middleCoo
        self.damage = self.startingDamage
        self.radius = self.startingRadius
        self.width = 0
        self.leftClick = None
        
        
    def updateRect(self):
        self.rect = p.draw.circle(self.screen, self.color, self.middleCoo, self.radius, self.width)
        #self.rect = p.Rect(self.middleCoo[0], self.middleCoo[1], self.radius, self.radius)
    
    ### SETTERS
    
    def setRadius(self, radius):
        self.radius = radius
        self.updateRect()
        
    
    def setDamage(self, damage):
        self.damage = damage
        
        
    def setColor(self, color):
        self.color = color
        
        
    def setSpeed(self, speed):
        self.speed = speed
        
        
    def setWidth(self, width):
        self.width = width
        
        
    def setClick(self, click):
        if click == "l":
            self.leftClick = True
        elif click == "r":
            self.leftClick = False
        
    ### GETTERS
    
    def getClick(self) -> bool:
        return self.leftClick
    
    
    
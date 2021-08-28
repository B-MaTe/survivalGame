import pygame as p
from settings import Settings
from player import Player

class Main:
    
    def __init__(self) -> None:
        self.settings = Settings()
        self.active = True
        self.screen = self.settings.screen
        self.player = Player("basic", "easy")
        
        
    def events(self) -> None:
        for event in p.event.get():
            if event.type == p.QUIT:
                self.active = False
            elif event.type == p.KEYDOWN:
                if event.type == p.K_w:
                    self.moveObjects(0, -1)
                if event.type == p.K_s:
                    self.moveObjects(0, 1)
                if event.type == p.K_a:
                    self.moveObjects(-1, 0)
                if event.type == p.K_d:
                    self.moveObjects(1, 0)
                
    
    def moveObjects(self, x, y):
        ### Move everything except the player
        pass
    
    
    def blitPlayer(self) -> object:
        return self.screen.blit(self.player.image, (self.player.x, self.player.y))
        
                
    def run(self) -> None:
        ### Background
        self.screen.fill(self.settings.bgColor)
        ### Blit the player
        self.blitPlayer()
        
        
        p.display.flip()
    
    
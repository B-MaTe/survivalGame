import pygame as p
from settings import Settings
from player import Player
from enemies import Enemy
from random import randint
from pygame.time import Clock

class Main:
    def __init__(self) -> None:
        
        self.settings = Settings()
        self.screen = self.settings.screen
        self.player = Player("basic")
        self.enemies = p.sprite.Group()
        self.waitingEnemies = p.sprite.Group()
        self.active = True
        self.createAllEnemies(self.settings.waitingEnemyNumber[self.settings.difficulty])
        
        ### Movement
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        
        ### Pygame clock
        self.clock = Clock()
        
        ### Values for measuring enemy movement
        self.middleCoo = (self.settings.W // 2, self.settings.H // 2)
        
        
    
    def checkAnyCollision(self, character):
        ### Checking if colliding with other enemies
        if not p.sprite.spritecollideany(character, self.enemies):
            ### Checking if spawning point is near the player
            if abs(character.rect.x - (self.settings.W // 2 - self.player.image.get_width() // 2)) > self.settings.H // 3 or abs(character.rect.y - (self.settings.H // 2 - self.player.image.get_height() // 2)) > self.settings.H // 3:
                return False
        return True
    
    
    def moveObjects(self, x, y):
        ### Move everything except the player
        if self.enemies:
            for enemy in self.enemies:
                enemy.rect.x += x
                enemy.rect.y += y
        
        
    def createAllEnemies(self, numberOfEnemies):
        for enemy in range(numberOfEnemies):
            enemy = Enemy()
            enemy.add(self.waitingEnemies)
        
        
    def createEnemy(self) -> bool:
        for waitingEnemy in self.waitingEnemies:
            enemy = waitingEnemy
            break
        enemy.rect.x, enemy.rect.y = randint(1, self.settings.W), randint(1, self.settings.H)
        if not self.checkAnyCollision(enemy):
            enemy.add(self.enemies)
            enemy.remove(self.waitingEnemies)
        else:
            self.createEnemy()
        
    
    def randomCreateEnemy(self) -> None:
        ### Randomly spawn enemies
        if randint(1, self.settings.spawnRate) < 10:
            self.createEnemy()
        
    
    def blitPlayer(self) -> None:
        self.screen.blit(self.player.image, (self.player.x, self.player.y))
        
        
    def handlePlayerMovement(self) -> None:
        if self.up:
            self.moveObjects(0, 2)
        if self.down:
            self.moveObjects(0, -2)
        if self.right:
            self.moveObjects(-2, 0)
        if self.left:
            self.moveObjects(2, 0)
    
    
    def handleEnemyMovement(self) -> None:
        speed = self.settings.enemySpeed[self.settings.difficulty]
        width, height = self.settings.W, self.settings.H
        if self.enemies:
            for enemy in self.enemies:
                if width - enemy.rect.x < self.middleCoo[0]:
                    enemy.rect.x -= speed
                else:
                    enemy.rect.x += speed
                if height - enemy.rect.y < self.middleCoo[1]:
                    enemy.rect.y -= speed
                else:
                    enemy.rect.y += speed
    
    
    def updateEnemies(self) -> None:
        self.enemies.draw(self.screen)
        self.enemies.update()
        
        
    def events(self) -> None:
        for event in p.event.get():
            if event.type == p.QUIT:
                self.active = False
            elif event.type == p.KEYDOWN:
                if event.key == p.K_ESCAPE:
                    self.active = False
                elif event.key == p.K_w:
                    self.up = True
                elif event.key == p.K_s:
                    self.down = True
                elif event.key == p.K_a:
                    self.left = True
                elif event.key == p.K_d:
                    self.right = True
                    
            elif event.type == p.KEYUP:
                if event.key == p.K_w:
                    self.up = False
                elif event.key == p.K_s:
                    self.down = False
                elif event.key == p.K_a:
                    self.left = False
                elif event.key == p.K_d:
                    self.right = False
        
        
    def run(self) -> None:
        
        ### Background
        self.screen.fill(self.settings.bgColor)
        
        ### Blit the player
        self.blitPlayer()
        
        ### Creates enemy at given rate
        self.randomCreateEnemy()
        
        ### Handles player and enemy movement
        self.handlePlayerMovement()
        self.handleEnemyMovement()
        
        ### Update and draw sprite group
        self.updateEnemies() 
        
        ### create an enemy randomly
        self.clock.tick(self.settings.FPS)
        
        ### Update the screen
        p.display.flip()

        

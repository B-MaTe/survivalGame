import pygame as p
from settings import Settings
from player import Player
from enemies import Enemy
from random import randint, randrange
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
        
        ### Background
        self.backgroundCirclePositions = []
        self.createBackgroundCircles(self.settings.noise)
        
        ### Track movement for background drawing
        self.upBg = 0
        self.downBg = 0
        self.rightBg = 0
        self.leftBg = 0
        
        ### Movement
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        
        
        
        ### Pygame clock
        self.clock = Clock()
        
        ### Values for calculating stuff
        self.middleCoo = (self.settings.W // 2, self.settings.H // 2)
        self.healthBarStartPos = self.middleCoo[0] - self.player.image.get_width() // 2, self.middleCoo[1] + self.player.image.get_height() * 0.5
        self.healthBarEndPos = self.middleCoo[0] + self.player.image.get_width() // 2, self.middleCoo[1] + self.player.image.get_height() * 0.5
        self.playerHealth = self.healthBarEndPos[0] - self.healthBarStartPos[0] ### Calculating the health in px
        self.damage = 0
        
        
    
    def checkAnyCollision(self, character) -> bool:
        ### Checking if colliding with other enemies
        if not p.sprite.spritecollideany(character, self.enemies):
            ### Checking if spawning point is near the player
            if abs(character.rect.x - (self.settings.W // 2 - self.player.image.get_width() // 2)) > self.settings.H // 3 or abs(character.rect.y - (self.settings.H // 2 - self.player.image.get_height() // 2)) > self.settings.H // 3:
                return False
        return True
    
    
    def checkPlayerEnemyCollision(self) -> None:
        ### Check for player-enemy collision, if so the player takes damage and the enemy disappears
        if self.enemies:
            for enemy in self.enemies:
                if self.player.rect.colliderect(enemy.rect):
                    enemy.kill()
                    self.damage += self.settings.playerHealth[self.settings.difficulty] / self.playerHealth
                    if self.checkGameEnd():
                        p.quit()
     
     
    def moveObjects(self, x, y) -> None:
        ### Move everything except the player
        if self.enemies:
            for enemy in self.enemies:
                enemy.rect.x += x
                enemy.rect.y += y
                
        if self.backgroundCirclePositions:
            for index, pos in enumerate(self.backgroundCirclePositions):
                self.backgroundCirclePositions[index] = (pos[0] + x, pos[1] + y)
        
        
    def createAllEnemies(self, numberOfEnemies) -> None:
        for enemy in range(numberOfEnemies):
            enemy = Enemy()
            enemy.add(self.waitingEnemies)
        
        
    def createEnemy(self) -> None:
        if self.waitingEnemies:
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
        
        
    def handlePlayerMovement(self) -> None:
        speed = self.settings.playerSpeed
        if self.up:
            self.upBg += speed
            self.moveObjects(0, speed)
        if self.down:
            self.downBg += speed
            self.moveObjects(0, -speed)
        if self.right:
            self.rightBg += speed
            self.moveObjects(-speed, 0)
        if self.left:
            self.leftBg += speed
            self.moveObjects(speed, 0)
    
    
    def handleEnemyMovement(self) -> None:
        ### Calculate the movement of the two axis
        if self.enemies:
            speed = self.settings.enemySpeed[self.settings.difficulty]
            for enemy in self.enemies:
                x, y = self.middleCoo[0] - enemy.rect.x, self.middleCoo[1] - enemy.rect.y
                xNegative, yNegative = 1, 1
                if x < 0:
                    xNegative = -1
                if y < 0:
                    yNegative = -1
                absX, absY = abs(x), abs(y)
                if absX > absY:
                    enemy.rect.x += speed * xNegative
                    enemy.rect.y += speed * (absY / absX) * yNegative
                elif absY > absX:
                    enemy.rect.y += speed * yNegative
                    enemy.rect.x += speed * (absX / absY) * xNegative
                else:
                    enemy.rect.x += speed * xNegative
                    enemy.rect.y += speed * yNegative
                
    
    
    def updateEnemies(self) -> None:
        self.enemies.draw(self.screen)
        self.enemies.update()
        
    
    def blitPlayer(self) -> None:
        self.screen.blit(self.player.image, (self.player.x, self.player.y))
        
        
    def blitPlayerHealthBar(self) -> p.Rect:
        p.draw.line(self.screen, (255, 0, 0), self.healthBarStartPos, (self.healthBarEndPos[0] - self.damage, self.healthBarEndPos[1]), 2)
        
        
    def blitBackground(self) -> None:
        ### If bg is already created, this function draws them
        if self.backgroundCirclePositions:
            for pos in self.backgroundCirclePositions:
                p.draw.circle(self.screen, self.settings.BgCircleColor, (pos[0], pos[1]), randint(1, self.settings.circleSize))
            
            
    def createBackgroundCircles(self, noise) -> bool:
        ### Creates colorful circles as bg
        if not self.backgroundCirclePositions:
            for y in range(self.settings.H // noise):
                for x in range(self.settings.W // noise):
                    self.backgroundCirclePositions.append((randrange(0, self.settings.W), randrange(0, self.settings.H)))
            return False
        return True
            
        
    def changeBackgroundCirclesOutOfPos(self) -> None:
        w, h = self.settings.W, self.settings.H
        ### Checks for bg circles with pos out of the screen, put them in new pos
        if self.upBg > 30:
            for i, pos in enumerate(self.backgroundCirclePositions):
                if pos[1] - 35 > h:
                    self.backgroundCirclePositions[i] = (randint(5, w - 5), randint(-15, -1))
            self.upBg = 0
        if self.downBg > 30:
            for i, pos in enumerate(self.backgroundCirclePositions):
                if pos[1] + 35 < 0:
                    self.backgroundCirclePositions[i] = (randint(5, w - 5), randint(h+1, h+15))
            self.downBg = 0
        if self.leftBg > 30:
            for i, pos in enumerate(self.backgroundCirclePositions):
                if pos[0] - 35 > w:
                    self.backgroundCirclePositions[i] = (randint(-15,-1), randint(5, h - 5))
            self.leftBg = 0
        if self.rightBg > 30:
            for i, pos in enumerate(self.backgroundCirclePositions):
                if pos[0] + 35 < 0:
                    self.backgroundCirclePositions[i] = (randint(w+1, w+15), randint(5, h - 5))
            self.rightBg = 0
            
            
    def checkGameEnd(self) -> bool:
        if self.playerHealth <= self.damage:
            return True
        return False
            
            
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
        self.blitBackground()
        self.changeBackgroundCirclesOutOfPos()
        
        ### Blit the player and the health bar
        self.blitPlayer()
        self.blitPlayerHealthBar()
        
        ### Creates enemy at given rate
        self.randomCreateEnemy()
        
        ### Handles player and enemy movement
        self.handlePlayerMovement()
        self.handleEnemyMovement()
        
        ### Check for collisions
        self.checkPlayerEnemyCollision()
        
        ### Update and draw sprite group
        self.updateEnemies() 
        
        ### create an enemy randomly
        self.clock.tick(self.settings.FPS)
        
        ### Update the screen
        p.display.flip()

        

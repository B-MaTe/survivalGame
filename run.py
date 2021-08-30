from main import Main
from settings import Settings
import pygame as p
p.init()
class Run:
    def __init__(self) -> None:
        self.main = Main()
        self.settings = Settings()
        self.process()
        
    def isRunning(self) -> bool:
        return self.main.active
    
    def process(self) -> None:
        while self.isRunning():
            self.main.run()
            self.main.events()
            
            
            
           
            
            
if __name__=='__main__':
    Run()
    
    
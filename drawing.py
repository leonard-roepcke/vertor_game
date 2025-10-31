import pygame

class PygameApp:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((2800, 1600))
        pygame.display.set_caption("Vector game")
        self.running = True



    def loop(self):
        pygame.display.flip()
        self.screen.fill((0, 0, 0))
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
    
    def draw_cordinates(self):
        pygame.draw.line(self.screen,(255,255,255),(200,200),(300,300),5)
    
    def infput_thigi(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_1]:
            pass

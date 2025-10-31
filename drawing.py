import pygame

class PygameApp:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((2800, 1600))
        pygame.display.set_caption("Vector game")
        self.running = True



    def loop(self):
        self.screen.fill((0, 0, 0))
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
        #pygame.quit()
    
    def set_points(self, points):
        self.points = points

    def add_point(self, point):
        self.points.append(point)
    
    def update_pos(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_1]:
            pass

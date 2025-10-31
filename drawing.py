import pygame

class PygameApp:
    def __init__(self):
        pygame.init()
        info = pygame.display.Info()
        self.SCREEN_SIZE = [info.current_w, info.current_h]
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        pygame.display.set_caption("Vector game")
        self.running = True

    def r_to_w_pos(self, relative_pos):
        return (self.SCREEN_SIZE[0] / 2 + relative_pos[0],
                self.SCREEN_SIZE[1] / 2 + relative_pos[1])

    def loop(self):
        pygame.display.flip()
        self.screen.fill((0, 0, 0))
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        if self.escape(): return False
        return True
    
    def draw_coordinates(self):
        center = (self.SCREEN_SIZE[0] // 2, self.SCREEN_SIZE[1] // 2)
        grid_step = 100
        grid_count = 10     
        arrow_size = 30
        arrow_width = 20
        line_width = 4



        line_width *= 2

        # --- Gitterlinien ---
        # horizontale Linien
        for i in range(-grid_count, grid_count+1):
            y = center[1] + i * grid_step
            pygame.draw.line(self.screen, (50,50,50), (center[0]-grid_count*grid_step, y), (center[0]+grid_count*grid_step, y), line_width)

        # vertikale Linien
        for i in range(-grid_count, grid_count+1):
            x = center[0] + i * grid_step
            pygame.draw.line(self.screen, (50,50,50), (x, center[1]-grid_count*grid_step), (x, center[1]+grid_count*grid_step), line_width)

        # --- Achsen ---
        # X-Achse (rot)
        pygame.draw.line(self.screen, (255,0,0), (center[0]-grid_count*grid_step, center[1]), (center[0]+grid_count*grid_step, center[1]), line_width*2)
        # Pfeile X
        pygame.draw.line(self.screen, (255,0,0), (center[0]+grid_count*grid_step, center[1]), 
                        (center[0]+grid_count*grid_step-arrow_size, center[1]-arrow_width), line_width*2)
        pygame.draw.line(self.screen, (255,0,0), (center[0]+grid_count*grid_step, center[1]), 
                        (center[0]+grid_count*grid_step-arrow_size, center[1]+arrow_width), line_width*2)
        pygame.draw.line(self.screen, (255,0,0), (center[0]-grid_count*grid_step, center[1]), 
                        (center[0]-grid_count*grid_step+arrow_size, center[1]-arrow_width), line_width*2)
        pygame.draw.line(self.screen, (255,0,0), (center[0]-grid_count*grid_step, center[1]), 
                        (center[0]-grid_count*grid_step+arrow_size, center[1]+arrow_width), line_width*2)

        # Y-Achse (grün)
        pygame.draw.line(self.screen, (0,255,0), (center[0], center[1]-grid_count*grid_step), (center[0], center[1]+grid_count*grid_step), line_width*2)
        # Pfeile Y
        pygame.draw.line(self.screen, (0,255,0), (center[0], center[1]-grid_count*grid_step), 
                        (center[0]-arrow_width, center[1]-grid_count*grid_step+arrow_size), line_width*2)
        pygame.draw.line(self.screen, (0,255,0), (center[0], center[1]-grid_count*grid_step), 
                        (center[0]+arrow_width, center[1]-grid_count*grid_step+arrow_size), line_width*2)
        pygame.draw.line(self.screen, (0,255,0), (center[0], center[1]+grid_count*grid_step), 
                        (center[0]-arrow_width, center[1]+grid_count*grid_step-arrow_size), line_width*2)
        pygame.draw.line(self.screen, (0,255,0), (center[0], center[1]+grid_count*grid_step), 
                        (center[0]+arrow_width, center[1]+grid_count*grid_step-arrow_size), line_width*2)
        # --- Markierungen auf X-Achse ---
        for i in range(-grid_count+1, grid_count):
            x = center[0] + i * grid_step
            tick_height = int(grid_step/5)
            # Oberhalb/unterhalb der Achse
            pygame.draw.line(self.screen, (255,0,0), (x, center[1]-tick_height), (x, center[1]+tick_height), line_width)

        # --- Markierungen auf Y-Achse ---
        for i in range(-grid_count+1, grid_count):
            y = center[1] + i * grid_step
            tick_width = int(grid_step/5)
            # Links/rechts der Achse
            pygame.draw.line(self.screen, (0,255,0), (center[0]-tick_width, y), (center[0]+tick_width, y), line_width)


        
    def escape(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            return True

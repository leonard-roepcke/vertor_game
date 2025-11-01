import pygame

class PygameApp:
    def __init__(self):
        pygame.init()
        info = pygame.display.Info()
        self.SCREEN_SIZE = [info.current_w, info.current_h]
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        pygame.display.set_caption("Vector game")
        self.running = True
        self.clock = pygame.time.Clock()

        self.center = (self.SCREEN_SIZE[0] // 2, self.SCREEN_SIZE[1] // 2)
        self.grid_step = 100
        self.grid_count = 10     
        self.arrow_size = 30
        self.arrow_width = 20
        self.line_width = 8

    def r_to_w_pos(self, relative_pos):
        return (self.SCREEN_SIZE[0] / 2 + relative_pos[0],
                self.SCREEN_SIZE[1] / 2 + relative_pos[1])

    def loop(self):
        pygame.display.flip()
        self.dt = self.clock.tick(0)
        self.screen.fill((0, 0, 0))
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        if self.escape(): return False
        return True
    
    def draw_coordinates(self):
        center = self.center
        grid_step = self.grid_step
        grid_count = self.grid_count     
        arrow_size = self.arrow_size
        arrow_width = self.arrow_width
        line_width = self.line_width


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
            if i==0: continue 
            x = center[0] + i * grid_step
            tick_height = int(grid_step/5)
            # Oberhalb/unterhalb der Achse
            pygame.draw.line(self.screen, (255,0,0), (x, center[1]-tick_height), (x, center[1]+tick_height), line_width)

        # --- Markierungen auf Y-Achse ---
        for i in range(-grid_count+1, grid_count):
            if i==0: continue 
            y = center[1] + i * grid_step
            tick_width = int(grid_step/5)
            # Links/rechts der Achse
            pygame.draw.line(self.screen, (0,255,0), (center[0]-tick_width, y), (center[0]+tick_width, y), line_width)

    def draw_vector(self, pos):
        """
        pos: Tuple (x, y) in Einheiten, z.B. (1,2)
        Zeichnet einen Pfeil vom Ursprung zum Punkt pos
        """
        center = self.center
        grid_step = self.grid_step
        arrow_size = self.arrow_size
        arrow_width = self.arrow_width
        line_width = self.line_width

        # Zielpunkt in Pixel
        end_x = center[0] + pos[0] * grid_step
        end_y = center[1] - pos[1] * grid_step  # y nach oben, darum minus

        # Linie zeichnen
        pygame.draw.line(self.screen, (255,255,0), center, (end_x, end_y), line_width)

        # Pfeilspitze berechnen
        # Winkel des Vektors
        import math
        dx = end_x - center[0]
        dy = end_y - center[1]
        angle = math.atan2(dy, dx)

        # Linien für Pfeilspitze
        left_angle = angle + math.pi * 3/4  # 135 Grad
        right_angle = angle - math.pi * 3/4

        left_x = end_x + arrow_size * math.cos(left_angle)
        left_y = end_y + arrow_size * math.sin(left_angle)
        right_x = end_x + arrow_size * math.cos(right_angle)
        right_y = end_y + arrow_size * math.sin(right_angle)

        pygame.draw.line(self.screen, (255,255,0), (end_x, end_y), (left_x, left_y), line_width)
        pygame.draw.line(self.screen, (255,255,0), (end_x, end_y), (right_x, right_y), line_width)

    def escape(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            return True
    
    def draw_enemy(self, pos, size):
        pygame.draw.circle(self.screen,(255,255,255,0),pos,size)

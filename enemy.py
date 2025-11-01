import random
class EnemyHandler:
    def __init__(self, pygame_app):
        self.pygame_app = pygame_app
        self.enemys = []
        self.i = 0
        self.rate = 1
    
    def add_enemy(self, pos):
        self.enemys.append(Enemy(self,pos))


    def update_enemys(self):
        if self.i > 1000:
            self.i = 0 
            self.add_enemy(self.random_coord())
        self.i+=self.rate
        self.rate += 0.001

        dt = self.pygame_app.dt
        for enemy in self.enemys:
            enemy.update(dt)
            enemy.draw()

    def draw_enemy(self, pos, size):
        self.pygame_app.draw_enemy(self.get_real_pos(pos),size)
    
    def get_real_pos(self, pos):
        return self.pygame_app.r_to_w_pos((pos[0]*self.pygame_app.grid_step,-pos[1]*self.pygame_app.grid_step))

    

    def random_coord(self):
        pushed_axis = random.choice(["x", "y"])

        outer_values = [i for i in range(-9, 10) if abs(i) > 3]
        all_values = list(range(-9, 10))

        weights = [abs(i) for i in outer_values]

        if pushed_axis == "x":
            x = random.choices(outer_values, weights=weights, k=1)[0]
            y = random.choice(all_values)
        else:
            x = random.choice(all_values)
            y = random.choices(outer_values, weights=weights, k=1)[0]

        return (x, y)


class Enemy:
    def __init__(self,handler,pos):
        self.handler = handler
        self.pos = pos
        self.speed = 0.004
        self.live=0
        self.size=0
    
    def draw(self):
        self.handler.draw_enemy(self.pos, self.size)
    def update(self, dt):
        self.live+=dt
        if self.live<=5000:
            self.size += (20*dt)/5000
        else:
            self.move(dt)
        
    def move(self,dt):
        dx = -self.pos[0]*dt
        dy = -self.pos[1]*dt
        length = (dx**2 + dy**2) ** 0.5
        if length > 0:
            dx /= length
            dy /= length
        self.pos = (self.pos[0] + dx * self.speed, self.pos[1] + dy * self.speed)



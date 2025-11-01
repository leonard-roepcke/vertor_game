class VectorHandler:
    def __init__(self,pygame_app):
        self.pygame_app = pygame_app
        self.vectors = []
    
    def update_vectors(self, pos):
        for vector in self.vectors:
            vector.draw()
    
    def draw_vector(self, pos):
        self.pygame_app.draw_vector(pos)

class Vector:
    def __init__(self, handler, pos):
        self.handler = handler
        self.pos = pos

    def draw(self):
        self.handler.draw_vector(self.pos)
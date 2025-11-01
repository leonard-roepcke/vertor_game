import drawing
import enemy
import vector
app = drawing.PygameApp()
enemy_handler = enemy.EnemyHandler(app)
vector_handler = vector.VectorHandler(app)
while app.loop():
    app.draw_coordinates()
    app.draw_vector((1,2))
    enemy_handler.update_enemys()
    
    
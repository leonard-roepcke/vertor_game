import drawing
import enemy
app = drawing.PygameApp()
enemy_handler = enemy.EnemyHandler(app)

while app.loop():
    app.draw_coordinates()
    app.draw_vector((1,2))
    enemy_handler.update_enemys()
    
    
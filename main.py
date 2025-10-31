import drawing
app = drawing.PygameApp()
while app.loop():
    app.draw_coordinates()
    app.draw_vector((1,2))
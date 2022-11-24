import pygame as pg

pg.init()#modulos que vamos a usar

#creamos una pantalla
pantalla_principal = pg.display.set_mode((800,600))#ventana y su tamaño

pg.display.set_caption('Bolillas,Rebotando')#titulo de la ventana

game_over = False#variable para controlar el bucle
#contador = 0
x = 400
y = 300
vx = 1
vy = 1
while not game_over:#bucle para ejecutar los fotogramas para el repintado de la pantalla
    

    for eventos in pg.event.get():#capturar eventos de pygame en forma de lista
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = True
            
    pantalla_principal.fill((53, 153, 220))#asigna color a la pantalla
    x += vx
    y += vy
    
    if x >= 800 or x == 0:#llegue a los limites en x
        vx *= -1
    if y >= 600 or y == 0:#llegue a los limites en y
        vy *= -1
       
       
                
    pg.draw.rect(pantalla_principal, (128, 39, 45), (x, y, 20, 20))
    
    
    pg.display.flip()
   # contador += 1
    #print((f'pintando el fotograma nro: {contador}'))
pg.quit()
            
    
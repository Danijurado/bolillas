import pygame as pg

pg.init()#modulos que vamos a usar

#creamos una pantalla
pantalla_principal = pg.display.set_mode((800,600))#ventana y su tamaño

pg.display.set_caption('Bolillas,Rebotando')#titulo de la ventana

class Bolitas():
    def __init__(self, pantalla_principal, x, y):
        self.pantalla_principal = pantalla_principal
        self.x = x
        self.y = y
        self.vx = 1
        self.vy = 1
        
    def dibujar(self):
        pg.draw.rect(self.pantalla_principal, (128, 39, 45), (self.x, self.y, 20, 20))
        
    def mover(self):
        self.x += self.vx
        self.y += self.vy
        
def refrescar_pantalla(pantalla_principal):
    pantalla_principal.fill((53, 153, 220))
    bola.dibujar()
        
def funcion_principal():
    global bola
    pantalla_principal = pg.display.set_mode((800,600))
    pantalla_principal.fill((53, 153, 220))
    bola = Bolitas(pantalla_principal, 400, 300)
    bola.vx = 1
    bola.vy = 1
    game_over = True
       
    while  game_over:#bucle para ejecutar los fotogramas para el repintado de la pantalla
        for eventos in pg.event.get():#capturar eventos de pygame en forma de lista
            print(eventos)
            if eventos.type == pg.QUIT:
                game_over = False
        bola.mover()
        if bola.x >= 780:
            bola.vx *= -1
            bola.x = 780
        if bola.x <= 0:
            bola.vx *= -1
            bola.x = 0
        if bola.y >= 580:
            bola.vy *= -1
            bola.y = 580
        if bola.y <= 0:
            bola.vy *= -1
            bola.y = 0
                        
        refrescar_pantalla(pantalla_principal)
        pg.display.update()
            
    pg.display.flip()
        
pg.quit()
                    
                   
            
          
            
     
    
        

        
    
            
     
       
  
            
    
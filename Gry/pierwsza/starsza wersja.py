import pygame as pg
import sys,random

from pygame.math import Vector2

pg.init()
myfont=pg.font.SysFont("monospace",20)
circle_vect=pg.Vector2(1220,660)
#box=pg.Rect(10,10,50,50)
#box1=pg.Rect(1220,660,50,50)
circle1=[circle_vect.x,circle_vect.y]
circle2=[35,35]
ekran_x=1280
DW_HALF=ekran_x/2
ekran_y=720
DH_HALF=ekran_y/2
screen=pg.display.set_mode((ekran_x,ekran_y))
caler_a=5
caler_b=5
caler_c=5
caler_a1=150
caler_b1=0
caler_c1=255
clock=pg.time.Clock()
licznik=0
#import kota i jego wtśrodkowanie ora skalowanie
cat=pg.image.load('Catt.gif')
cat_img=pg.transform.scale(cat,(70,70))
cat_wsp=cat_img.get_rect()
mouse=pg.image.load('mouse.png')
mouse_scal=pg.transform.scale(mouse,(70,70))
mouse_wsp=mouse_scal.get_rect()
def zasady(circle2,circle_vect):
    global licznik
    odleglosc_x = abs(circle2[0] - circle_vect.x)
    odleglosc_y = abs(circle2[1]- circle_vect.y)
    if odleglosc_x<=50 and odleglosc_y<=50:
        licznik +=1
        circle2[1]=35
        circle2[0] = 35
        circle_vect.x = 1220
        circle_vect.y =660
    return licznik, circle2,circle_vect



    pass
while True:
    #evenyt
    for event in pg.event.get():
        if event.type==pg.QUIT:
            sys.exit(0)
        elif event.type==pg.KEYDOWN and event.key==pg.K_1:
            caler_b=random.randint(0,255)
            caler_c = random.randint(0, 255)
            caler_a = random.randint(0, 255)
        elif event.type==pg.KEYDOWN and event.key==pg.K_0:
            caler_b1=random.randint(0,255)
            caler_c1 = random.randint(0, 255)
            caler_a1 = random.randint(0, 255)
        elif event.type==pg.KEYDOWN and event.key==pg.K_2:      #ustawainie pozycji początkowej wersja kwardrat
            box.x=620
            box.y=350
        elif event.type == pg.KEYDOWN and event.key == pg.K_9:
            box1.x = 620
            box1.y = 350


    #imput check
    keys=pg.key.get_pressed()
    if circle2[1]<660 and circle2[1]>35:
        if keys[pg.K_w]:
            circle2[1]-=1
        if keys[pg.K_s]:
            circle2[1] -= -1
    if circle2[1] >= 660:
        if keys[pg.K_w]:
            circle2[1] -= 1
    if circle2[1] <=35:
        if keys[pg.K_s]:
            circle2[1]-= -1

    if circle2[0]<1220 and circle2[0]>35:
        if keys[pg.K_a]:
            circle2[0]-=1
        if keys[pg.K_d]:
            circle2[0]+=1
    if circle2[0] >= 1220 :
        if keys[pg.K_a]:
            circle2[0] -= 1
    if circle2[0] <=35:
        if keys[pg.K_d]:
            circle2[0] -= -1




    if circle_vect.y < 660 and circle_vect.y > 35:
        if keys[pg.K_UP]:
            circle_vect.y -= 1
        if keys[pg.K_DOWN]:
            circle_vect.y -= -1
    if circle_vect.y >= 660:
        if keys[pg.K_UP]:
            circle_vect.y -= 1
    if circle_vect.y <= 35:
        if keys[pg.K_DOWN]:
            circle_vect.y -= -1

    if circle_vect.x < 1220 and circle_vect.x > 35:
        if keys[pg.K_LEFT]:
            circle_vect.x -= 1
        if keys[pg.K_RIGHT]:
            circle_vect.x -= -1
    if circle_vect.x >= 1220:
        if keys[pg.K_LEFT]:
            circle_vect.x -= 1
    if circle_vect.x <= 35:
        if keys[pg.K_RIGHT]:
            circle_vect.x -= -1

    zasady(circle2,circle_vect)





    #Drowing
    screen.fill((0,0,0))
    pg.draw.circle(screen, (caler_a1, caler_b1, caler_c1), (int(circle_vect.x),int(circle_vect.y)), 25)
    pg.draw.circle(screen, (caler_a, caler_b, caler_c), circle2, 25)
    #screen.blit(cat_img,(DW_HALF-cat_wsp.center[0],DH_HALF-cat_wsp.center[1]))
    screen.blit(mouse_scal,(DW_HALF-mouse_wsp.center[0],DH_HALF-mouse_wsp.center[1]))

    text=myfont.render('kwadrat(x,y)=('+str(circle2[0])+","+str(circle2[1])+')' ,10,(255,255,255))
    text2=myfont.render( 'koło(x,y)'+str(circle_vect.x)+','+str(circle_vect.y)+')',10,(255,255,255))
    punktacja=myfont.render('punktacja gracz A: '+str(licznik)+' Gracz B: '+'punktyb',10,(255,250,240))
    screen.blit(punktacja,(400,10))
    screen.blit(text,(50,10))
    screen.blit(text2, (800, 690))

    #pg.draw.rect(screen,(caler_a,caler_b,caler_c),box)
    #pg.draw.rect(screen, (caler_a1, caler_b1, caler_c1), box1)

    pg.display.flip()
    clock.tick(250)
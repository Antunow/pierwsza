import pygame as pg
import sys,random

from pygame.math import Vector2

pg.init()
myfont=pg.font.SysFont("monospace",20)

ekran_x=1280
DW_HALF=ekran_x/2
ekran_y=720
DH_HALF=ekran_y/2
screen=pg.display.set_mode((ekran_x,ekran_y))
circle_vect=pg.Vector2(60,DH_HALF)
box=pg.Rect(35,DH_HALF,50,50)
caler_a=50
caler_b=150
caler_c=250
caler_a1=150
caler_b1=0
caler_c1=255
clock=pg.time.Clock()
licznik=0
licznik_m=0
delta=0.0
game_time=0
mouse_pos=pg.Vector2(1220,660)
cat_pos=pg.Vector2(1200,30)
poop_count=0


class Poop:
    def __init__(self,mouse_pos):
        self.poop_load = pg.image.load('poop.png')
        self.poop_scal=pg.transform.scale(self.poop_load,(40,40))
        self.pos_list=[mouse_pos.x,mouse_pos.y]
        self.pos_list_new=self.pos_list.copy()
        self.poop_posx=self.pos_list_new[0]
        self.poop_posy=self.pos_list_new[1]

    def poop_rules(self,cat_pos,mouse_pos):
        self.mous_dis_x=abs(mouse_pos.x-self.poop_posx)
        self.mous_dis_y = abs(mouse_pos.y - self.poop_posy)
        if self.mous_dis_x<=30 and self.mous_dis_y<=30:
            if self.poop_posx>mouse_pos.x :
                mouse_pos.x-=5

            else:
                mouse_pos.x += 5
            if self.poop_posy>mouse_pos.y:
                mouse_pos.y-=5

            else:
                mouse_pos.y += 5
        self.cat_dis_x = abs(cat_pos.x+5- self.poop_posx)
        self.cat_dis_y = abs(cat_pos.y+25 - self.poop_posy)
        if self.cat_dis_x <= 50 and self.cat_dis_y <= 50:
            if self.poop_posx > cat_pos.x:
                cat_pos.x -= 5

            else:
                cat_pos.x += 5
            if self.poop_posy > cat_pos.y:
                cat_pos.y -= 5

            else:
                cat_pos.y += 5



def zasady(mouse_pos,cat_pos):
    global licznik, circle_vect, licznik_m,poop_count
    odleglosc_x = abs(mouse_pos.x - cat_pos.x)
    odleglosc_y = abs(mouse_pos.y - cat_pos.y)
    hole_dis_x = abs(mouse_pos.x-circle_vect.x)
    hole_dis_y = abs(mouse_pos.y - circle_vect.y)
    if hole_dis_x<=30 and  hole_dis_y<=30:
        licznik_m += 1
        mouse_pos.x = 1220
        mouse_pos.y = 660
        cat_pos.x = 1200
        cat_pos.y = 30
        poop_count = 0
    if odleglosc_x<=50 and odleglosc_y<=50:
        licznik +=1
        mouse_pos.x=1220
        mouse_pos.y = 660
        cat_pos.x = 1200
        cat_pos.y =30
        poop_count=0

    return licznik, mouse_pos,cat_pos

def player_1(): #mysz
    global mouse_pos
    global mouse_scal
    global delta
    global mouse_wsp
    mouse = pg.image.load('mouse.png')
    mouse_scal = pg.transform.scale(mouse, (50, 50))
    mouse_wsp = mouse_scal.get_rect()

    dt = clock.tick()
    delta += dt / 1000.0
    while delta > 1 / 300:
        delta -= 1 / 300
        keys = pg.key.get_pressed()
        if mouse_pos.y < 660 and mouse_pos.y > 35:

                 if keys[pg.K_UP]:
                       mouse_pos.y -= 1
                 if keys[pg.K_DOWN]:
                       mouse_pos.y -= -1
        if mouse_pos.y >= 660:
            if keys[pg.K_UP]:
                mouse_pos.y -= 1
        if mouse_pos.y <= 35:
            if keys[pg.K_DOWN]:
                mouse_pos.y -= -1

        if mouse_pos.x < 1220 and mouse_pos.x > 35:
            if keys[pg.K_LEFT]:
                mouse_pos.x -= 1
            if keys[pg.K_RIGHT]:
                mouse_pos.x -= -1
        if mouse_pos.x >= 1220:
            if keys[pg.K_LEFT]:
                mouse_pos.x -= 1
        if mouse_pos.x <= 35:
            if keys[pg.K_RIGHT]:
                mouse_pos.x -= -1

def player_2():
    global cat_pos
    global cat_scal
    global cat_wsp
    global delta


    cat = pg.image.load('Catt.gif')
    cat_scal = pg.transform.scale(cat, (100, 100))
    cat_wsp = cat_scal.get_rect()

    dt = clock.tick()
    delta += dt / 9000.0
    keys = pg.key.get_pressed()
    while delta > 1 / 8500:
        delta -= 1 / 8500
        keys = pg.key.get_pressed()

        if cat_pos.y < 660 and cat_pos.y > 35:
            if keys[pg.K_w]:
                cat_pos.y -= 1
            if keys[pg.K_s]:
                cat_pos.y -= -1
        if cat_pos.y >= 660:
            if keys[pg.K_w]:
                cat_pos.y -= 1
        if cat_pos.y <= 35:
            if keys[pg.K_s]:
                cat_pos.y -= -1

        if cat_pos.x < 1220 and cat_pos.x > 35:
            if keys[pg.K_a]:
                cat_pos.x -= 1
            if keys[pg.K_d]:
                cat_pos.x -= -1
        if cat_pos.x >= 1220:
            if keys[pg.K_d]:
                cat_pos.x -= 1
        if cat_pos.x <= 35:
            if keys[pg.K_d]:
                cat_pos.x -= -1

def event():
    global poop_count
    global poop_1
    global poop_3
    global poop_2
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
        elif  event.type==pg.KEYDOWN and event.key==pg.K_KP3:
            poop_count+=1
            if poop_count==1:
                poop_1=Poop(mouse_pos)
                #poop_1.poop_pos=mouse_pos.copy()
            if poop_count==2:
                poop_2=Poop(mouse_pos)
            if poop_count==3:
                poop_3=Poop(mouse_pos)
            #poop_pos=mouse_pos



while True:


    event()
    player_2()
    player_1()
    zasady(mouse_pos,cat_pos)

    #Drowing
    screen.fill((0,0,0))
    pg.draw.circle(screen, (caler_a1, caler_b1, caler_c1), (int(circle_vect.x),int(circle_vect.y)), 25)
    pg.draw.rect(screen, (0, 0, 0), box)
    if poop_count >= 1:
        poop_1.poop_rules(cat_pos,mouse_pos)
        screen.blit(poop_1.poop_scal, (poop_1.poop_posx, poop_1.poop_posy))
    if poop_count >= 2:
        poop_2.poop_rules(cat_pos, mouse_pos)
        screen.blit(poop_2.poop_scal, (poop_2.poop_posx, poop_2.poop_posy))
    if poop_count >= 3:
        poop_3.poop_rules(cat_pos, mouse_pos)
        screen.blit(poop_3.poop_scal, (poop_3.poop_posx, poop_3.poop_posy))
    screen.blit(cat_scal,(cat_pos.x-30,cat_pos.y))
    screen.blit(mouse_scal,(mouse_pos.x,mouse_pos.y))


    text = myfont.render('kot(x,y)=('+str(cat_pos.x)+","+str(cat_pos.x)+')' ,10,(255,255,255))
    text2 = myfont.render( 'mysz(x,y)'+str(mouse_pos.x)+','+str(mouse_pos.y)+')',10,(255,255,255))
    punktacja = myfont.render('Punkty Kota: '+str(licznik),10,(255,250,240))
    punkty_myszy= myfont.render('Punkty myszy: '+str(licznik_m),10,(255,255,255))
    screen.blit(punktacja,(400,10))
    screen.blit(punkty_myszy,(1000,690))
    screen.blit(text,(50,10))
    screen.blit(text2, (500, 690))

    pg.display.flip()

    dt=clock.tick()
    delta+=dt/1000.0
    while delta>1/2000:
        delta-=1/2000


import pygame,sys
from pygame.locals import *
import time
#set pygame environment
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2,buffer=512)
pygame.init()
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("Desert Dinasour")
clock=pygame.time.Clock()
game_font=pygame.font.Font('Sprites/Transformers Movie.ttf',30)
#color
white=(255,255,255)
black=(0,0,0)
#create background
bg=pygame.image.load('Sprites/background.png').convert()
#create dinasour
dra1=pygame.image.load('Sprites/dra1.png').convert_alpha()
dra1=pygame.transform.scale(dra1,(30,30))
dra2=pygame.image.load('Sprites/dra2.png').convert_alpha()
dra2=pygame.transform.scale(dra2,(30,30))
dra3=pygame.image.load('Sprites/dra3.png').convert_alpha()
dra3=pygame.transform.scale(dra3,(30,30))
dra4=pygame.image.load('Sprites/dra4.png').convert_alpha()
dra4=pygame.transform.scale(dra4,(30,30))
dra5=pygame.image.load('Sprites/dra5.png').convert_alpha()
dra5=pygame.transform.scale(dra5,(30,30))
dra6=pygame.image.load('Sprites/dra6.png').convert_alpha()
dra6=pygame.transform.scale(dra6,(30,30))
dra_walk=[dra1,dra1,dra2,dra2,dra2,dra3,dra3,dra3,dra4,dra4,dra4]
#create tree
tree0=pygame.image.load('Sprites/tree.png').convert()
tree0=pygame.transform.scale(tree0,(60,50))
tree1=pygame.image.load('Sprites/tree1.png').convert_alpha()
tree1=pygame.transform.scale(tree1,(100,60))
tree2=pygame.image.load('Sprites/tree2.png').convert_alpha()
tree2=pygame.transform.scale(tree2,(90,60))
tree3=pygame.image.load('Sprites/tree3.png').convert_alpha()
tree3=pygame.transform.scale(tree3,(50,50))
tree4=pygame.image.load('Sprites/tree4.png').convert_alpha()
tree4=pygame.transform.scale(tree4,(50,50))
tree5=pygame.image.load('Sprites/tree5.png').convert_alpha()
tree5=pygame.transform.scale(tree5,(35,50))
#create sound:
hit_sound=pygame.mixer.Sound('Sprites/sfx_hit.wav')
jumb_sound=pygame.mixer.Sound('Sprites/sfx_wing.wav')
point_sound=pygame.mixer.Sound('Sprites/sfx_point.wav')
#loop game
def gameloop():
    score=0
    highscore=0
    game_active=False
    bgvelo=0
    bgx=0
    bgy=0
    tree_x=400
    tree_y=281
    dra_x=50
    dra_y=293
    walkpoint=0
    jumb=False
    gravity=3
    game_over=False
    while True:
        events=pygame.event.get()
        for event in events:
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_UP:
                    if dra_y==293:
                        game_active=True
                        bgvelo=5
                        jumb=True
            if event.type==KEYDOWN:
                if event.key==K_SPACE:
                    gameloop()
        #create infinite background
        if bgx<=-600:
            bgx=0
        #create infinite background
        if tree_x<=-2700:
            tree_x=600
        #jumb
        if 294>dra_y>196:
            if jumb==True:
                dra_y-=6
                jumb_sound.play()
        else :
            jumb=False
        if dra_y<293:
            if jumb==False:
                dra_y+=gravity
        #collision
        #tree1
        if tree_x<dra_x+34<tree_x+100 and tree_y<dra_y<tree_y+60:
            hit_sound.play()
            gravity=0
            bgvelo=0
            walkpoint=0
            game_active=False
            game_over=True

        #tree2   
        if tree_x+400<dra_x+34<tree_x+100+400 and tree_y<dra_y+34<tree_y+60:
            hit_sound.play()
            gravity=0
            bgvelo=0
            walkpoint=0
            game_active=False
            game_over=True

        #tree3
        if tree_x+400+500<dra_x+34<tree_x+40+400+500 and tree_y<dra_y+25<tree_y+62:
            hit_sound.play()
            gravity=0
            bgvelo=0
            walkpoint=0
            game_active=False
            game_over=True

        #tree4
        if tree_x+400+500+500<dra_x+32<tree_x+50+400+500+500 and tree_y<dra_y+20<tree_y+50:
            hit_sound.play()
            gravity=0
            bgvelo=0
            game_active=False
            walkpoint=0
            game_over=True
        #tree5   
        if tree_x+400+500+500+500<dra_x+30<tree_x+50+400+500+500+500+35 and tree_y<dra_y+20<tree_y+55:
            gravity=0
            bgvelo=0
            walkpoint=0
            game_active=False
        #tree0
        if tree_x+400+500+500+500+600<dra_x+30<tree_x+50+400+500+500+500+600+60 and tree_y<dra_y+25<tree_y+65:
            hit_sound.play()
            gravity=0
            bgvelo=0
            walkpoint=0
            game_active=False
            game_over=True
        bgx-=bgvelo
        tree_x-=bgvelo
        text=game_font.render("SCORE "+str(score),True,black)
        text1=game_font.render("HIGH SCORE "+str(highscore),True,black)
        text2=game_font.render("GAME OVER!Press space to play again",True,black)
        if game_active==True:
            score+=1
            if score%100==0:
                point_sound.play()
        screen.fill(white)
        screen.blit(bg,(bgx,bgy))
        screen.blit(bg,(bgx+600,bgy))
        screen.blit(text,(400,10))
        screen.blit(text1,(100,10))
        if game_over==True:
            screen.blit(text2,(20,160))
            if score>highscore:
                highscore=score
            
        screen.blit(dra_walk[walkpoint],(dra_x,dra_y))
        if game_active==True:
            walkpoint+=1
            if walkpoint>10:
                walkpoint=0
        screen.blit(tree1,(tree_x,tree_y))
        screen.blit(tree2,(tree_x+400,tree_y-7))
        screen.blit(tree3,(tree_x+900,tree_y+1))
        screen.blit(tree4,(tree_x+1400,tree_y+7))
        screen.blit(tree5,(tree_x+1900,tree_y+4))
        screen.blit(tree0,(tree_x+2500,tree_y+2))
        pygame.display.update()
        clock.tick(65)
gameloop()
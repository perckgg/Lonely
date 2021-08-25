import pygame,sys,random

from pygame.locals import *
#create function
def draw_floor():
    screen.blit(floor,(floor_x_pos,650))
    screen.blit(floor,(floor_x_pos+432,650))
def create_pipe():
    random_pipe_pos=random.choice(pipe_height)
    bottom_pipe=pipe_surface.get_rect(midtop=(400,random_pipe_pos))
    top_pipe=pipe_surface.get_rect(midtop=(400,random_pipe_pos-700))
    return bottom_pipe,top_pipe 
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx-=3
    return pipes
def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom>=700:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe=pygame.transform.flip(pipe_surface,False,True)#dk dau laf truc x, dk sau la truc y
            screen.blit(flip_pipe,pipe)
def check(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            hit_sound.play()
            return False
        if bird_rect.top<=-75 or bird_rect.bottom>=768:
            hit_sound.play()
            return False
    return True
def rotate_bird(bird_up):
    new_bird=pygame.transform.rotozoom(bird_up,-movement*3,1)#rotozoom tao hieu ung xoay cho chim
    return new_bird
def bird_animation():
    new_bird=bird_list[bird_index]
    new_bird_rect=new_bird.get_rect(center=(100,bird_rect.centery))
    return new_bird,new_bird_rect
def score_display(game_state):
    if game_state=='main game':    
        score_surface=game_font.render(str(int(score)),True,(255,255,255))
        score_rect=score_surface.get_rect(center = (350,80))
        screen.blit(score_surface,score_rect)
    if game_state=='game_over':
        score_surface=game_font.render(f'Score: {int(score)}',True,(255,255,255))
        score_rect=score_surface.get_rect(center = (220,80))
        screen.blit(score_surface,score_rect)
        #highscore
        high_score_surface=game_font.render(f'High score: {int(high_score)}',True,(255,255,255))
        high_score_rect=score_surface.get_rect(center = (170,600))
        screen.blit(high_score_surface,high_score_rect)
def update_score(score,high_score):
    if score >= high_score:
        high_score=score
    return high_score 
#create Variables
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2,buffer=512)
pygame.init()
screen=pygame.display.set_mode((432,768))
clock=pygame.time.Clock()
gravity=0.18
movement=0
game_active=True
game_font=pygame.font.Font('04B_19.ttf',40)
score=0
high_score=0
#chen background
bg=pygame.image.load('assets/background.png').convert()
bg=pygame.transform.scale2x(bg)
#chen floor
floor=pygame.image.load('assets/floor.png').convert()
floor=pygame.transform.scale2x(floor)
floor_x_pos=0
#create bird
bird_len=pygame.transform.scale2x(pygame.image.load('assets/yellowbird-upflap.png').convert_alpha())
bird_ngang=pygame.transform.scale2x(pygame.image.load('assets/yellowbird-midflap.png').convert_alpha())
bird_xuong=pygame.transform.scale2x(pygame.image.load('assets/yellowbird-downflap.png').convert_alpha())
bird_list=[bird_xuong,bird_ngang,bird_len]
bird_index=2
bird=bird_list[bird_index]
#create timer for bird
bird_flap=pygame.USEREVENT+1
pygame.time.set_timer(bird_flap,290)

#bird=pygame.image.load('assets/yellowbird-midflap.png').convert_alpha()
#bird=pygame.transform.scale2x(bird)
bird_rect=bird.get_rect(center=(100,300))

#create obstacle
pipe_surface=pygame.image.load('assets/pipe-green.png').convert()
pipe_surface=pygame.transform.scale2x(pipe_surface)
pipe_list=[]
#create game over
game_over_surface=pygame.transform.scale2x(pygame.image.load('assets/message.png').convert_alpha())
game_over_rect=game_over_surface.get_rect(center=(216,350))
#create timer
spawnpipe=pygame.USEREVENT
pygame.time.set_timer(spawnpipe,1400)
pipe_height=[350,300,400,280]
#create sound
flap_sound=pygame.mixer.Sound('sound/sfx_wing.wav')
hit_sound=pygame.mixer.Sound('sound/sfx_hit.wav')
point_sound=pygame.mixer.Sound('sound/sfx_point.wav')
point_sound_countdown=100
#loop game
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and game_active==True:
                movement=0
                movement-=6.3
                flap_sound.play()
            if event.key==pygame.K_SPACE and game_active==False:
                game_active=True
                pipe_list.clear()
                bird_rect.center=(100,200)
                movement=0
                score=0
        if event.type==spawnpipe:
            pipe_list.extend(create_pipe())
        if event.type==bird_flap:
            if bird_index < 2 :
                bird_index+=1
            else :
                bird_index=0
            bird,bird_rect=bird_animation()
    #Background
    screen.blit(bg,(0,0))
    if game_active:
    #bird
        movement+=gravity
        rotated_bird=rotate_bird(bird)
        bird_rect.centery +=movement
        screen.blit(rotated_bird,bird_rect)
        game_active=check(pipe_list)
        #Pipe
        pipe_list=move_pipe(pipe_list)
        draw_pipe(pipe_list)
        score+=0.01
        score_display('main game')
        point_sound_countdown-=1
        if point_sound_countdown<=0:
            point_sound.play()
            point_sound_countdown=100
    else:
        screen.blit(game_over_surface,game_over_rect)
        high_score=update_score(score,high_score)
        score_display('game_over')
        

        #Floor
    floor_x_pos-=1
    draw_floor()
    if floor_x_pos<=-432:
        floor_x_pos=0
    pygame.display.update()
    clock.tick(120)

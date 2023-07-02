import pygame
import random
from pygame import mixer
from pygame import freetype
import os

os.chdir(r"G:\Pallav\Coding\Python Projects\Python Games\car game")
window_x, window_y = 960, 660

pygame.init()
mixer.init()
pygame.display.set_caption('Pallav Game')
gamefont = freetype.SysFont("comicsansms", 20)
screen = pygame.display.set_mode((window_x, window_y))

car_yellow = pygame.image.load("car_yellow.jpg")
car_red = pygame.image.load("car_red.jpg")
car_list = [car_yellow, car_red]
trophy = pygame.image.load("trophy.jpg")
man = pygame.image.load("man.jpg")
hit_sound = mixer.Sound("dmg_sound.mp3")

"--------------------------------------------------------------------------------------------------" # CONSTANTS

lane1, lane2, lane3, lane4, lane5, lane6, lane7, lane8, lane9 = [], [], [], [], [], [], [], [], []
lane_list = [lane1, lane2, lane3, lane4, lane5, lane6, lane7, lane8, lane9]
target_lane = 0

home_up = (480, 10)
home_down = (480, 610)

death = 0
score = 0

run = True

player_x,player_y = 480, 610
powerup_x, powerup_y = None, None

white = [255,255,255]
black = [0, 0, 0]

disp = 0

"--------------------------------------------------------------------------------------------------"# GAME VARS (MODIFY)

lives = 20
reset = -4
speed = 3
gap = 300
deviation = 35
powerups = ["lives", "slow time"]

"--------------------------------------------------------------------------------------------------"# FUNCTIONS AND MAINLOOP


def check():
    global player_x,player_y,lane_list
    for i in lane_list:
        for j in i:
            if (player_x-5) > j[0] and (player_x+5) < j[0] + 120:
                if player_y > j[1] and player_y < j[1] + 50:
                    return True
    
    if player_x > 940 or player_x < 0 or player_y > 660 or player_y < 0:
        return True    
    
def add_block():
    global lane1, lane2, lane3, lane4, lane5, lane6, lane7, lane8, lane9
    
    lane1.append([960 + deviation*random.randint(0, 4), 545])
    lane3.append([960 + deviation*random.randint(0, 4), 425])
    lane5.append([960 + deviation*random.randint(0, 4), 305])
    lane7.append([960 + deviation*random.randint(0, 4), 185])
    lane9.append([960 + deviation*random.randint(0, 4), 65 ])
    
    lane2.append([-120 - deviation*random.randint(0, 4), 485])
    lane4.append([-120 - deviation*random.randint(0, 4), 365])
    lane6.append([-120 - deviation*random.randint(0, 4), 245])
    lane8.append([-120 - deviation*random.randint(0, 4), 125])

def powerup():
    p = random.choice(powerups)
    
    
    
    pass

def draw_lines():
    for i in range(8):
        depth = 540 - 60*(i+1)
        pygame.draw.line(screen, black, (0,depth),(960,depth), 1)


while run:
       
    flip = -0.1
    
    draw_lines()
    
    pygame.draw.line(screen, black, (0, 540), (960,540),1)
    pygame.draw.line(screen, black, (0, 600), (960,600),1)
    
    
    text_surface, rect = gamefont.render("LIVES - " + str(lives), (0, 0, 0))
    screen.blit(text_surface, (20, 20))

    text_surface2, rect2 = gamefont.render("TROPHIES - " + str(score), (0, 0, 0))
    screen.blit(text_surface2, (180, 20))
    
    
    
    if check():
        death += 1
        lives -= 1
        hit_sound.play()
        if target_lane == 0:
            player_x,player_y = home_down
        else:
            player_x, player_y = home_up
        
        
    
    screen.blit(man, [player_x, player_y])
    for i in [lane1, lane2, lane3, lane4, lane5, lane6, lane7, lane8, lane9]:
        if flip == 0.1:
            car = 1
        else:
            car = 0
        for j in i:
            
            screen.blit(car_list[car], j)
            j[0] += flip*speed
        flip *= -1        
    
    disp += 0.1*speed

    if disp > gap + 5*random.randint(-3,3):
        disp = 0
        add_block()
        reset += 1

        
    if reset == 9:
        reset=0
        for i in [lane1, lane2, lane3, lane4, lane5, lane6, lane7, lane8, lane9]:
            del i[0:9]
    
    if target_lane == 0:
        screen.blit(trophy, home_up)
    else:
        screen.blit(trophy, home_down)
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= 30
            if event.key == pygame.K_RIGHT:
                player_x += 30
            if event.key == pygame.K_DOWN:
                player_y += 60
            if event.key == pygame.K_UP:
                player_y -= 60
            if event.key == pygame.K_l:
                score += 2
                speed += 1.2
    
    current_lane = (player_y-10)/60
    
    if current_lane == target_lane:
        score+=1
        speed += 0.6
        
        if target_lane == 10:
            target_lane = 0
        else:
            target_lane = 10
        
   
    pygame.display.flip()
    screen.fill(white) 
    
    if lives == 0:
        break
    
    

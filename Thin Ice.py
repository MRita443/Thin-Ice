# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 18:28:37 2021

@author: rital
"""

import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

def spaces_number():
    spaces = 0
    for row in range(0, len(levels[current_level])):
        for element in levels[current_level][row]:
            if element == "-" or element == "L" or element == "K" or element == "F" or element == "D" or element == "S":
                spaces += 1
    return spaces

def update_frames(animation_list):
    
    global time_since_last_frame
    global animation_frame_num
    global dt
    
    delay, keyword = animation_list[0]

    if time_since_last_frame > delay:
        animation_frame_num[keyword] += 1
        if animation_frame_num[keyword] > len(animation_list) - 1:
            animation_frame_num[keyword] = 1
        time_since_last_frame = 0
    else:
        time_since_last_frame += dt


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT, ))
pygame.display.set_caption("Thin Ice")



'''
Legend 
    0: Empty space
    1: External barrier
    -: Walkable space
    S: Starting block of the level
    F: Final block of the level
    D: Double block, can be stepped on twice before sinking
    K: Key block
    L: Locked block, requires a key to go through
'''
   
levels = [
    ["0000000000000000000000000",
    "0000000000000000000000000",
    "0000000000000000000000000",
    "0000000000000000000000000",
    "0000000000000000000000000",
    "0000000000000000000000000",
    "0000000000000000000000000",
    "0000000000000000000000000",
    "1111111111111111111111111",
    "1S---------------------F1",
    "1111111111111111111111111",
    "0000000000000000000000000",
    "0000000000000000000000000",
    "0000000000000000000000000",
    "0000000000000000000000000",
    "0000000000000000000000000",
    "0000000000000000000000000",
    "0000000000000000000000000"],
    
    ["0000000000000000000000000",
    "0000000000000000000000000",
    "0000000000000000000000000",
    "0000000000000000000000000",
    "0000000000000000000000000",
    "0000000000000000000000000",
    "0000000000000000000000000",
    "0000001111000000000000000",
    "1111111--1111111111111111",
    "1S--------------------F11",
    "1111----------------11111",
    "000111111111----111-10000",
    "00000000000111--11--10000",
    "00000000000001--11-110000",
    "000000000000011----100000",
    "0000000000000011111100000",
    "0000000000000000000000000",
    "0000000000000000000000000"],

    ["0000000000000000000000000",
    "0000000000000000000000000",
    "0000000000000000000000000",
    "0000000000000000000000000",
    "0000001111111110000000000",
    "0000001------K10000000000",
    "0000001-------10000000000",
    "0000001--1111110000000000",
    "1111111--1111111000000000",
    "1S-------------1000000000",
    "1111-----------1000000000",
    "0001111--1111111111111100",
    "0000001----------L----100",
    "00000011--------11111-100",
    "000000011111111110001F100",
    "0000000000000000000011100",
    "0000000000000000000000000",
    "0000000000000000000000000"],
    
    ["0000000000000000000000000",
    "0000000000000000000000000",
    "0000000000000000000000000",
    "0000000000000000000000000",
    "1111111111111111111111000",
    "1--------------------1000",
    "1-111111111111111111-1111",
    "1-111F--------------D---1",
    "1-111111111111111111-11-1",
    "1-111111111111111111S11-1",
    "1-111111111111111111111-1",
    "1-11----11111111--11111-1",
    "1-----------------------1",
    "111111111----------111111",
    "0000000011111111111110000",
    "0000000000000000000000000",
    "0000000000000000000000000",
    "0000000000000000000000000"],
    
    ["0000000000000000000000000",
    "0000000000000000000000000",
    "1111111111111111111111111",
    "1K----------------------1",
    "1---DDDDDDDDDDDDDD----D-1",
    "1---------------------D-1",
    "1----111-----111111---D-1",
    "1---11-------11S11DD--D-1",
    "1--11--------11-11------1",
    "1-----------------------1",
    "1-----------------------1",
    "1--11--------111----111-1",
    "1--111----------DDDDL-1-1",
    "1-111--111---111----1F1-1",
    "1-11-DD-------------111-1",
    "1-----------------------1",
    "1111111111111111111111111",
    "0000000000000000000000000"],
    
    ["0000000000000000000000000",
    "0000000000000000000000000",
    "0000000000000000000000000",
    "0000111110001111100000000",
    "00001---11111--K100000000",
    "00001-1-11S11-1-100000000",
    "00001--D--D--D--111100000",
    "0000111-11-11-1111F100000",
    "0000011-11-11-1111L100000",
    "000001----D--D--1--110000",
    "000001---1-11-1-1---10000",
    "000001-----11---11--10000",
    "000001-11111111111--10000",
    "000001--------------10000",
    "0000011111111111111110000",
    "0000000000000000000000000",
    "0000000000000000000000000",
    "0000000000000000000000000"]
]

#Sprites
puffle_img_1 = pygame.image.load('Puff1.png')
puffle_img_2 = pygame.image.load('Puff2.png')
puffle_img_3 = pygame.image.load('Puff3.png')
puffle_img_4 = pygame.image.load('Puff4.png')
puffle_img_5 = pygame.image.load('Puff5.png')

puffle_img = [(150, "Puffle"), puffle_img_1, puffle_img_2, puffle_img_3, puffle_img_4, puffle_img_5]

puffle_death_img_1 = pygame.image.load('PuffDeath1.png')
puffle_death_img_2 = pygame.image.load('PuffDeath2.png')
puffle_death_img_3 = pygame.image.load('PuffDeath3.png')
puffle_death_img_4 = pygame.image.load('PuffDeath4.png')
puffle_death_img_5 = pygame.image.load('PuffDeath5.png')
puffle_death_img_6 = pygame.image.load('PuffDeath6.png')
puffle_death_img_7 = pygame.image.load('PuffDeath7.png')
puffle_death_img_8 = pygame.image.load('PuffDeath8.png')
puffle_death_img_9 = pygame.image.load('PuffDeath9.png')
puffle_death_img_10 = pygame.image.load('PuffDeath10.png')
puffle_death_img_11 = pygame.image.load('PuffDeath11.png')
puffle_death_img_12 = pygame.image.load('PuffDeath12.png')

puffle_death_img = [(80, "Death"), puffle_death_img_1, puffle_death_img_2, puffle_death_img_3, puffle_death_img_4, puffle_death_img_5, puffle_death_img_6, puffle_death_img_7, puffle_death_img_8, puffle_death_img_9, puffle_death_img_10, puffle_death_img_11, puffle_death_img_12]

block_img = pygame.image.load('Bloco.png')
finalblock_img = pygame.image.load('Bloco final.png')
lockblock_img = pygame.image.load('Bloco unlockable.png')
doubleblock_img = pygame.image.load('Bloco duplo.png')

key_img_1 = pygame.image.load('Key.png')
key_img_2 = pygame.image.load('Key_2.png')
key_img_3 = pygame.image.load('Key_3.png')
key_img_4 = pygame.image.load('Key_4.png')
key_img_5 = pygame.image.load('Key_5.png')

key_img = [(150, "Key"), key_img_1, key_img_2, key_img_3, key_img_4, key_img_5]

victory_zoom_1 = pygame.image.load('Final zoom.png')

animation_frame_num = {'Puffle': 1, 'Death': 1, 'Key': 1}

#Sounds
pygame.mixer.music.load('Club Penguin OST - Thin Ice Theme.mp3')

victory = pygame.mixer.Sound('Victory.mp3')
bonk = pygame.mixer.Sound('Bonk.mp3')
game_over_sound = pygame.mixer.Sound('Game Over.wav')
diving = pygame.mixer.Sound('Diving.mp3')

pygame.mixer.music.set_volume(0.1)
victory.set_volume(0.1)
bonk.set_volume(0.1)
game_over_sound.set_volume(0.1)
diving.set_volume(0.1)

#Fonts
game_over_font = pygame.font.Font("AlegreyaSans-Black.ttf", 72, bold=True, italic=False)
game_over_text_font = pygame.font.Font("AlegreyaSans-Black.ttf", 32, bold=False, italic=False)
main_menu_font = pygame.font.Font("AlegreyaSans-Black.ttf", 28, bold=True, italic=False)

#General

clock = pygame.time.Clock()


current_level = 0
solved = 0
total_points = 0
starting_points = 0
starting_positions = []
spaces_num = spaces_number()
key_block = ()
final_block = ()
locked_block = ()
double_blocks = set()
barriers = set()
used = set()
key = False
first_pass = {}
left_key = False
right_key = False
up_key = False
down_key = False
start_pos = False
animation_done = False
music_done = False



puffle_x = 0     
puffle_y = 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            

block_size = 32

left_key = right_key = up_key = down_key = False
death_animation = game_over_screen = game_over_check = False
time_since_last_movement = 0
time_since_last_frame = 0
running = True

pygame.mixer.music.play()

while running:
    
    dt = clock.tick(120)
    previous_position = (puffle_x, puffle_y, )
    
    #Drawing

    ##Screen
    screen.fill((155, 205, 255))
    
    ##Menu
    game_over = game_over_font.render('Game Over', True, (255, 255, 255))
    game_over_text = game_over_text_font.render('Your puffle drowned. Press SPACE to replay this level!', True, (155, 205, 255))
    level_num = main_menu_font.render('LEVEL ' + str(current_level + 1), True, (0, 79, 156))
    square_count = main_menu_font.render(str(len(used)) + "/" + str(spaces_num), True, (0, 79, 156))
    solved_count = main_menu_font.render("SOLVED " + str(solved), True, (0, 79, 156))
    points_count = main_menu_font.render("POINTS " + str(total_points), True, (0, 79, 156))

    pygame.draw.rect(screen, (215, 240, 255), (0, 0, SCREEN_WIDTH, 48))
    pygame.draw.rect(screen, (215, 240, 255), (0, 552, SCREEN_WIDTH, 48))
    screen.blit(level_num, (40, 10))
    screen.blit(square_count, (375, 10))
    screen.blit(solved_count, (640, 10))
    screen.blit(points_count, (640, 560))

    ##Level
    for row in range(0, len(levels[current_level])):
        for col in range(0, len(levels[current_level][0])):
            
            if (col*block_size, row*block_size, ) in used and (col*block_size, row*block_size, ) != (puffle_x, puffle_y, ):
                #Mark the block where the puffle is as dark blue
                pygame.draw.rect(screen, (0, 70, 204), (col*block_size, row*block_size, block_size, block_size)) 
                
            elif levels[current_level][row][col] == '1':
                screen.blit(block_img, (col*block_size, row*block_size, block_size, block_size) )
                barriers.add((col*block_size, row*block_size,))
                
            elif levels[current_level][row][col] == '-':
                pygame.draw.rect(screen, (217, 241, 255), (col*block_size, row*block_size, block_size, block_size)) 
                
            elif levels[current_level][row][col] == 'S':
                pygame.draw.rect(screen, (217, 241, 255), (col*block_size, row*block_size, block_size, block_size)) 
                if not start_pos:
                    (puffle_x, puffle_y, ) = (col*block_size, row*block_size, )
                    starting_positions.append((col*block_size, row*block_size, ))
                    start_pos = True
                
            elif levels[current_level][row][col] == 'F':
                screen.blit(finalblock_img, (col*block_size, row*block_size, block_size, block_size) )
                final_block = (col*block_size, row*block_size, )
                
            elif levels[current_level][row][col] == 'K':
                pygame.draw.rect(screen, (217, 241, 255), (col*block_size, row*block_size, block_size, block_size))
                if not animation_done:
                    if key:
                        update_frames(key_img)
                        screen.blit(key_img[animation_frame_num["Key"]], (col*block_size, row*block_size, block_size, block_size))
                        if animation_frame_num["Key"] == len(key_img) - 1:
                            animation_done = True
                    else:
                        screen.blit(key_img[1], (col*block_size, row*block_size, block_size, block_size) )
                key_block = (col*block_size, row*block_size, )
                
            elif levels[current_level][row][col] == 'L':
                screen.blit(lockblock_img, (col*block_size, row*block_size, block_size, block_size) )
                locked_block = (col*block_size, row*block_size, )
                
            elif levels[current_level][row][col] == 'D':
                if not first_pass.get((col*block_size, row*block_size, ), False):
                    screen.blit(doubleblock_img, (col*block_size, row*block_size, block_size, block_size) )
                    double_blocks.add((col*block_size, row*block_size, ))
                    first_pass[(col*block_size, row*block_size, )] = False
                else: 
                    pygame.draw.rect(screen, (217, 241, 255), (col*block_size, row*block_size, block_size, block_size))
        
                    
                
    #Keyboard events
    
    for event in pygame.event.get():           
        if event.type == QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_ESCAPE:
                running = False
                
            elif event.key == pygame.K_LEFT:
                left_key = True
                
            elif event.key == pygame.K_RIGHT:
                right_key = True
             
            elif event.key == pygame.K_UP:
                up_key = True
          
            elif event.key == pygame.K_DOWN:
                down_key = True

            elif event.key == pygame.K_SPACE:
                game_over_screen = False
                total_points = starting_points
                pygame.mixer.music.play()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_key = False
                
            elif event.key == pygame.K_RIGHT:
                right_key = False
                
            elif event.key == pygame.K_UP:
                up_key = False
                
            elif event.key == pygame.K_DOWN:
                down_key = False
        
    
                
    #Game mechanics
    
    ##Move the puffle, Count points
    temp_puffle_x, temp_puffle_y = (puffle_x, puffle_y,)
    
    if time_since_last_movement > 100:
        if left_key:
            temp_puffle_x -= 32
            
        if right_key:
            temp_puffle_x += 32
            
        if up_key:
           temp_puffle_y -= 32
            
        if down_key:
            temp_puffle_y += 32
            
        time_since_last_movement = 0
    else:
        time_since_last_movement += dt
    
    if (temp_puffle_x, temp_puffle_y, ) not in barriers and (temp_puffle_x, temp_puffle_y, ) not in used and (abs(temp_puffle_x - puffle_x), abs(temp_puffle_y - puffle_y)) != (32, 32):
    #Disallow movements to a barrier, a used block, or diagonal movements
        if ((temp_puffle_x, temp_puffle_y, ) == locked_block and key) or (temp_puffle_x, temp_puffle_y, ) != locked_block:
        #Only allow movement to a locked block if a key had been obtained
            puffle_x, puffle_y = (temp_puffle_x, temp_puffle_y,)
            
            if (puffle_x, puffle_y, ) not in double_blocks and (puffle_x, puffle_y) != previous_position:
                total_points += 1 
                
    elif (temp_puffle_x, temp_puffle_y, ) != previous_position and (temp_puffle_x, temp_puffle_y, ) in used:
        bonk.play()

    ##Game Over
    
    ###Check for Game Over
    adjacent_blocks = [(puffle_x + block_size, puffle_y, ), (puffle_x - block_size, puffle_y, ), (puffle_x, puffle_y + block_size, ), (puffle_x, puffle_y - block_size, )]
    
    if not game_over_screen and not death_animation:
        if list(filter(lambda x: x in used or x in barriers or (x == locked_block and not key), adjacent_blocks)) == adjacent_blocks:
            if (puffle_x, puffle_y) != final_block:
                game_over_check = True

    ###Game Over screen
    if game_over_check:
        pygame.event.clear()
        pygame.mixer.music.fadeout(1000)
        # pygame.time.wait(500)
        game_over_sound.play()
        diving.play()
        game_over_check = False
        death_animation = True
        
    if death_animation:

        pygame.draw.rect(screen, (0, 70, 204), ((puffle_x, puffle_y, block_size, block_size))) 
        update_frames(puffle_death_img)
        screen.blit(puffle_death_img[animation_frame_num["Death"]], (puffle_x, puffle_y))
        pygame.display.update()
        
        if animation_frame_num["Death"] == len(puffle_death_img) - 1:
            death_animation = False
            game_over_screen = True
            
        continue
            
    if game_over_screen:
        screen.fill((0, 70, 204))
        screen.blit(game_over, (237, 200))
        screen.blit(game_over_text, (47, 300))
        
        pygame.display.update()
        
        puffle_x = starting_positions[current_level][0]      
        puffle_y = starting_positions[current_level][1] 
        used = set()
        key = False
        animation_done = False
        first_pass = {}
        
        continue
        
        
    ##Mark the blocks where the puffle has already been
    if (puffle_x, puffle_y, ) not in double_blocks:
        used.add((puffle_x, puffle_y, ))

    ##Deal with different block types
    
    ###Final block
    if (puffle_x, puffle_y,) == final_block:
        
        #Check if the level was solved (100% blocks)
        if len(used) == spaces_number():
            solved += 1
        
        #Last level, end the game
        if current_level +1 > len(levels) - 1:

            screen.blit(puffle_img[animation_frame_num["Puffle"]], (puffle_x, puffle_y) )
                                   
            pygame.mixer.music.fadeout(800) 
            for i in range (100):    
                victory_zoom_1.set_alpha(i)
                screen.blit(victory_zoom_1,(0,0))
                pygame.display.update()
                pygame.time.wait(20)
                if i == 30:
                    victory.play()

            running = False
        
        #Advance to the next level
        else:
            current_level += 1
            (puffle_x, puffle_y) = (0, 0)
            starting_points = total_points
            barriers = set()
            used = set()
            final_block = ()
            double_blocks = set()
            spaces_num = spaces_number()
            key = False
            first_pass = {}
            animation_done = False
            start_pos = False


    ###Key block
    if (puffle_x, puffle_y,) == key_block:
        key = True
        
    ###Double block
    if (puffle_x, puffle_y) != previous_position and (puffle_x, puffle_y, ) in double_blocks:
        total_points += 1
        if not first_pass[(puffle_x, puffle_y, )]:
            first_pass[(puffle_x, puffle_y, )] = True
        else:
            used.add((puffle_x, puffle_y, ))
            double_blocks.remove((puffle_x, puffle_y, ))
            
    #Draw the puffle at final position, update screen
    update_frames(puffle_img)
    screen.blit(puffle_img[animation_frame_num["Puffle"]], (puffle_x, puffle_y) )
    pygame.display.update()

    
pygame.quit()
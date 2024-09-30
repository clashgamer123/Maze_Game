import pygame,sys
from Classes.button import button
from Classes.Player import Player
from highscore_func import read_high_scores,update_high_scores
from game_screen_maker import game_screen

#colors to use.        
black=(0,0,0)
silver=(192,192,192,255)
gold=(184, 134, 11, 255)
crimson=(220, 20, 60, 255)
orangered= (238, 64, 0, 255)
aquamarine=(69, 139, 116, 255)
brown=(205, 51, 51, 255)
aqua=(0, 255, 255, 255)
purple= (160, 32, 240, 255)
orange= (255, 165, 0, 255)
################################
        

#initializing pygame    
pygame.init()

############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
#                                             MAIN SCREEN

#Lets design the main_screen function now

main_screen_size=(main_screen_width,main_screen_height) = (960,540)

#Creating all the image surfaces for blitting on main screen

button_image_og=pygame.image.load("images/button_template.png")
button_image=pygame.transform.scale(button_image_og,(200,100))
button_image_score=pygame.transform.scale(button_image_og,(500,100))

background_image_og=pygame.image.load("images/background_mainscreen.jpg")
background_image=pygame.transform.scale(background_image_og,main_screen_size)

def main_screen():
    main_screen=pygame.display.set_mode(main_screen_size)
    pygame.display.set_caption("Home screen")
    
    #define the 4 buttons on main screen
    
    play_button=button(100,75,200,100,button_image,"Play",38,"Fonts/VeniteAdoremus.ttf",silver)
    quit_button=button(600,75,200,100,button_image,"Quit",38,"Fonts/VeniteAdoremus.ttf",silver)
    help_button=button(350,75,200,100,button_image,"Help",38,"Fonts/VeniteAdoremus.ttf",silver)
    highscores_button=button(250,400,500,100,button_image_score,"HighScores",34,"Fonts/VeniteAdoremus.ttf",silver)
    
    #Game loop for main screen
    
    run=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                if play_button.mouse_clicked(mouse_pos):
                    action="level_screen"
                    run=False
                
                elif quit_button.mouse_clicked(mouse_pos):
                    pygame.quit()
                    sys.exit()
                
                elif help_button.mouse_clicked(mouse_pos):
                    action="help_screen"
                    run=False
                
                elif highscores_button.mouse_clicked(mouse_pos):
                    action="highscores_screen"
                    run=False
                    
            else:
                pass
        
        # Mouse Hovering checks
        
        mouse_pos=pygame.mouse.get_pos()
        
        play_button.mouse_hovered(mouse_pos,gold,42)
        play_button.mouse_not_hovered(mouse_pos,silver,38)
        
        quit_button.mouse_hovered(mouse_pos,gold,42)
        quit_button.mouse_not_hovered(mouse_pos,silver,38)
        
        help_button.mouse_hovered(mouse_pos,gold,42)
        help_button.mouse_not_hovered(mouse_pos,silver,38)
        
        highscores_button.mouse_hovered(mouse_pos,gold,38)
        highscores_button.mouse_not_hovered(mouse_pos,silver,34)
            
        main_screen.blit(background_image,(0,0))
        play_button.draw(main_screen)
        quit_button.draw(main_screen)
        help_button.draw(main_screen)
        highscores_button.draw(main_screen)
        
        # Update the display screen
        
        pygame.display.flip()
    return action

##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
#                                                   LEVEL SCREEN

# Lets design lev_screen now...
level_screen_size=level_screen_width,level_screen_height=960,540

#images required are of level button and back button

back_button_image_og=pygame.image.load("images/back_button.png")
back_button_image=pygame.transform.scale(back_button_image_og,(200,75))

level_button_image_og=pygame.image.load("images/level_button.png")
level_button_image=pygame.transform.scale(level_button_image_og,(250,100))

level_screen_backg_og=pygame.image.load("images/background_level_screen.jpg")
level_screen_backg=pygame.transform.scale(level_screen_backg_og,level_screen_size)
       
def level_screen():
    level_screen=pygame.display.set_mode(level_screen_size)
    
    level_1_button=button(350, 50,250,100,level_button_image,"Level 1",36,"Fonts/DragonHunter.otf",gold)
    level_2_button=button(350,200,250,100,level_button_image,"Level 2",36,"Fonts/DragonHunter.otf",gold)
    level_3_button=button(350,350,250,100,level_button_image,"Level 3",36,"Fonts/DragonHunter.otf",gold)
    
    back_button=button(0,0,200,75,back_button_image,"Back",34,"Fonts/DragonHunter.otf",gold)
    
    run=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                
                if back_button.mouse_clicked(mouse_pos):
                    action="back"
                    run=False
                
                elif level_1_button.mouse_clicked(mouse_pos):
                    action="level_1_screen"
                    run=False
                
                elif level_2_button.mouse_clicked(mouse_pos):
                    action="level_2_screen"
                    run=False
                
                elif level_3_button.mouse_clicked(mouse_pos):
                    action="level_3_screen"
                    run=False
                
                else : pass
            else : pass
        
        mouse_pos=pygame.mouse.get_pos()
        
        back_button.mouse_hovered(mouse_pos,orangered,38)
        back_button.mouse_not_hovered(mouse_pos,gold,34)
        
        level_1_button.mouse_hovered(mouse_pos,orangered,40)
        level_1_button.mouse_not_hovered(mouse_pos,gold,36)
        
        level_2_button.mouse_hovered(mouse_pos,orangered,40)
        level_2_button.mouse_not_hovered(mouse_pos,gold,36)
        
        level_3_button.mouse_hovered(mouse_pos,orangered,40)
        level_3_button.mouse_not_hovered(mouse_pos,gold,36)
        
        level_screen.blit(level_screen_backg,(0,0))
        
        back_button.draw(level_screen)
        level_1_button.draw(level_screen)
        level_2_button.draw(level_screen)
        level_3_button.draw(level_screen)
        
        pygame.display.flip()
        
    return action

wall_img = pygame.image.load('images/maze_wall.png')
cell_img = pygame.image.load('images/maze_cell.png')
key_img = pygame.image.load('images/key.png')
gem_img = pygame.image.load('images/gem.png')

##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
#                                                LEVEL 1 SCREEN

#Lets design the level_1 of our maze using prims algorithm.24x15 being the dimension

level_1_screen_size = level_1_screen_width,level_1_screen_height = 960,650

# Wall size = 40x40 and so is a cell size. player size=25x25
# maze colors
cell_color_1 = aquamarine
wall_color_1 = brown

# images for buttons

time_temp_og_1 = pygame.image.load("images/button_template.png")
time_temp_1 = pygame.transform.scale(time_temp_og_1,(200,50))

back_button_image_og_1=pygame.image.load("images/back_button.png")
back_button_image_1=pygame.transform.scale(back_button_image_og_1,(150,50)) 

score_image_og_1=pygame.image.load("images/score_button.png")
score_image_1 = pygame.transform.scale(score_image_og_1,(300,50))

key_temp_og_1 = pygame.image.load("images/button_template.png")
key_temp_1 = pygame.transform.scale(key_temp_og_1,(250,50))

# ninja sprites loading

idle_og = pygame.image.load("Ninja_sprites/Idle.png")
run_0_og = pygame.image.load("Ninja_sprites/Run_0.png")
run_1_og = pygame.image.load("Ninja_sprites/Run_1.png")
run_2_og = pygame.image.load("Ninja_sprites/Run_2.png")
run_3_og = pygame.image.load("Ninja_sprites/Run_3.png")
run_4_og = pygame.image.load("Ninja_sprites/Run_4.png")
run_5_og = pygame.image.load("Ninja_sprites/Run_5.png")

idle_1 = pygame.transform.scale(idle_og,(25,25))
run_0_1 = pygame.transform.scale(run_0_og,(25,25))
run_1_1 = pygame.transform.scale(run_1_og,(25,25))
run_2_1 = pygame.transform.scale(run_2_og,(25,25))
run_3_1 = pygame.transform.scale(run_3_og,(25,25))
run_4_1 = pygame.transform.scale(run_4_og,(25,25))
run_5_1 = pygame.transform.scale(run_5_og,(25,25))

forward_ninja_images_1 = [idle_1,run_0_1,run_1_1,run_2_1,run_3_1,run_4_1,run_5_1]
no_keys_1 = 3
no_gems_1 = 5
time_limit_1 = 75

def level_1_screen():
    return game_screen([480,300],[960,600],2,24,15,50,1,1,40,cell_img,wall_img,25,forward_ninja_images_1,back_button_image_1,score_image_1,time_temp_1,key_img,key_temp_1,no_keys_1,gem_img,no_gems_1,time_limit_1)

    
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
#                                                LEVEL 2 SCREEN

# Lets design level 2 now
        
level_2_screen_size = level_2_screen_width,level_2_screen_height = 960,650 
#32 x 20 maze 

cell_color_2 = aquamarine
wall_color_2 = brown

# images for buttons

time_temp_og_2 = pygame.image.load("images/button_template.png")
time_temp_2 = pygame.transform.scale(time_temp_og_2,(200,50))

back_button_image_og_2=pygame.image.load("images/back_button.png")
back_button_image_2=pygame.transform.scale(back_button_image_og_2,(150,50)) 

score_image_og_2=pygame.image.load("images/score_button.png")
score_image_2 = pygame.transform.scale(score_image_og_2,(300,50))

key_temp_og_2 = pygame.image.load("images/button_template.png")
key_temp_2 = pygame.transform.scale(key_temp_og_2,(250,50))

idle_2 = pygame.transform.scale(idle_og,(20,20))
run_0_2 = pygame.transform.scale(run_0_og,(20,20))
run_1_2 = pygame.transform.scale(run_1_og,(20,20))
run_2_2 = pygame.transform.scale(run_2_og,(20,20))
run_3_2 = pygame.transform.scale(run_3_og,(20,20))
run_4_2 = pygame.transform.scale(run_4_og,(20,20))
run_5_2 = pygame.transform.scale(run_5_og,(20,20))

forward_ninja_images_2 = [idle_2,run_0_2,run_1_2,run_2_2,run_3_2,run_4_2,run_5_2]
no_keys_2 = 5
time_limit_2 = 135
no_gems_2 = 7

def level_2_screen():
    return game_screen([480,300],[960,600],2,32,20,50,2,0.9,30,cell_img,wall_img,20,forward_ninja_images_2,back_button_image_2,score_image_2,time_temp_2,key_img,key_temp_2,no_keys_2,gem_img,no_gems_2,time_limit_2)


#########################################################################################################################################
#########################################################################################################################################
#########################################################################################################################################
#                                                LEVEL 3 SCREEN

cell_color_3 = aquamarine
wall_color_3 = brown

# Let's design level 3 of the maze now
time_temp_og_3 = pygame.image.load("images/button_template.png")
time_temp_3 = pygame.transform.scale(time_temp_og_3,(200,50))

back_button_image_og_3=pygame.image.load("images/back_button.png")
back_button_image_3=pygame.transform.scale(back_button_image_og_3,(150,50)) 

score_image_og_3=pygame.image.load("images/score_button.png")
score_image_3 = pygame.transform.scale(score_image_og_3,(300,50))

key_temp_og_3 = pygame.image.load("images/button_template.png")
key_temp_3 = pygame.transform.scale(key_temp_og_3,(250,50))

level_3_screen_size = level_3_screen_width,level_3_screen_height = 960,650

#48x30     
idle_3 = pygame.transform.scale(idle_og,(15,15))
run_0_3 = pygame.transform.scale(run_0_og,(15,15))
run_1_3 = pygame.transform.scale(run_1_og,(15,15))
run_2_3 = pygame.transform.scale(run_2_og,(15,15))
run_3_3 = pygame.transform.scale(run_3_og,(15,15))
run_4_3 = pygame.transform.scale(run_4_og,(15,15))
run_5_3 = pygame.transform.scale(run_5_og,(15,15))

forward_ninja_images_3= [idle_3,run_0_3,run_1_3,run_2_3,run_3_3,run_4_3,run_5_3]
no_keys_3 = 7
time_limit_3 = 210
no_gems_3 = 10

def level_3_screen():
    return game_screen([320,200],[960,600],3,48,30,50,3,0.75,20,cell_img,wall_img,15,forward_ninja_images_3,back_button_image_3,score_image_3,time_temp_3,key_img,key_temp_3,no_keys_3,gem_img,no_gems_3,time_limit_3)

##############################################################################################################################################
##############################################################################################################################################
##############################################################################################################################################
#                                 HELP SCREEN
## Lets design the help screen now.

help_screen_size=help_screen_width,help_screen_height=960,540

#images required for help screen.

#back_button_image_og=pygame.image.load("images/back_button.png")
#back_button_image=pygame.transform.scale(back_button_image_og,(200,75)) >> Already defined for level screen.Use them as it is

help_img_og = pygame.image.load('images/help_text.png')
help_img = pygame.transform.scale(help_img_og,(640,360))

def help_screen():
    help_screen=pygame.display.set_mode(help_screen_size)
    back_button=button(0,0,200,75,back_button_image,"Back",34,"Fonts/DragonHunter.otf",gold)
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                if back_button.mouse_clicked(mouse_pos):
                    action="back"
                    run=False
                else: pass
            
            else: pass
            
        help_screen.fill(gold)
        help_screen.blit(help_img,(160,90))
        mouse_pos=pygame.mouse.get_pos()
        back_button.mouse_hovered(mouse_pos,orangered,38)
        back_button.mouse_not_hovered(mouse_pos,gold,34)
        back_button.draw(help_screen)
        
        
        pygame.display.flip()
        
    return action

# Lets design the highscores screen now

#Size will be 600 x 600
#Background image will be 

highscores_screen_bg_og = pygame.image.load("images/game_over_bg.png")
highscores_screen_bg = pygame.transform.scale(highscores_screen_bg_og,(1000,1000))

#Back button image ( it will take us to level screen )
back_button_score_og=pygame.image.load("images/back_button.png")
back_button_score=pygame.transform.scale(back_button_score_og,(200,100)) 


highscores_screen_size=highscores_screen_width,highscores_screen_height=700,700

def highscores_screen():
    highscores_screen=pygame.display.set_mode(highscores_screen_size)
    back_button = button(0,0,150,50,back_button_score,"Back",26,"Fonts/DragonHunter.otf",gold)
    
    #fonts
    head_font_1 = pygame.font.Font("Fonts/DragonHunter.otf",60)
    head = head_font_1.render("HIGH SCORES",True,gold)
    head_rect = head.get_rect(topleft=(170,140))
    
    head_font_2 = pygame.font.Font("Fonts/DragonHunter.otf",30)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if back_button.mouse_clicked(mouse_pos):
                    action = "back"
                    run = False
            
            else: pass
        
        highscores_screen.blit(highscores_screen_bg,(-150,-150))
        highscores_screen.blit(head,head_rect)
        
        mouse_pos = pygame.mouse.get_pos()
        back_button.mouse_hovered(mouse_pos,orangered,30)
        back_button.mouse_not_hovered(mouse_pos,gold,26)
        back_button.draw(highscores_screen)
        
        for i in range(1,4):
            level_head = head_font_2.render(f"Level{i}",True,silver)
            level_rect = level_head.get_rect(topleft=(30+140*i,230))
            highscores_screen.blit(level_head,level_rect)
            
            with open(f'highscores/highscore{i}.txt') as score_file:
                j = 1
                for line in score_file:
                    score_surface = head_font_2.render(str(j)+".  "+line, True, silver)
                    score_rect = score_surface.get_rect(topleft=(30+140*i,280+(j-1)*40))
                    highscores_screen.blit(score_surface,score_rect)
                    j+=1
    
        pygame.display.flip()
    return action
    
################################################################################################################

#Lets design the game_over screen

#Size will be 600 x 600
#Background image will be 

game_over_bg_og = pygame.image.load("images/game_over_bg.png")
game_over_bg = pygame.transform.scale(game_over_bg_og,(800,800))

#Back button image ( it will take us to level screen )
back_button_score_og=pygame.image.load("images/back_button.png")
back_button_score=pygame.transform.scale(back_button_score_og,(150,50)) 

game_over_screen_size = game_over_screen_width,game_over_screen_height = 600,600

def game_over_screen(status,level,score):
    game_over_screen = pygame.display.set_mode(game_over_screen_size)
    back_button = button(0,0,150,50,back_button_score,"Back",26,"Fonts/DragonHunter.otf",gold)
    
    run = True
    frame_counter = 1
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if back_button.mouse_clicked(mouse_pos):
                    action = "back"
                    run = False
            
            else : pass
                    
        game_over_screen.blit(game_over_bg,(-120,-120))
        
        mouse_pos = pygame.mouse.get_pos()
        back_button.mouse_hovered(mouse_pos,orangered,30)
        back_button.mouse_not_hovered(mouse_pos,gold,26)
        back_button.draw(game_over_screen)
        
        msg_font = pygame.font.Font("Fonts/DragonHunter.otf",70)
        if status == "win":
            msg_font_surface = msg_font.render("VICTORY",True,gold)
        else :
            msg_font_surface = msg_font.render("DEFEAT",True,gold)
        msg_rect = msg_font_surface.get_rect(topleft=(160,130))  
        game_over_screen.blit(msg_font_surface,msg_rect)
    
        if status == "win":
            if (frame_counter == 1) :
                update_high_scores(score,level)
                frame_counter+=1
    
            high_scores = read_high_scores(level)
            score_font = pygame.font.Font("Fonts/DragonHunter.otf",40)
            font = pygame.font.Font("Fonts/DragonHunter.otf",35)
            
            if len(high_scores) < 5 or score > min(high_scores) :
                score_font_surface = score_font.render(f"{score} (HIGH SCORE)",True,gold)
                score_rect = score_font_surface.get_rect(topleft=(120,210))
                head_font_surface = score_font.render("HIGH SCORES",True,silver)
                head_rect = score_font_surface.get_rect(topleft=(160,260))
                game_over_screen.blit(score_font_surface,score_rect)
                game_over_screen.blit(head_font_surface,head_rect)
                
            else:
                score_font_surface = score_font.render(f"{score}",True,silver)
                score_rect = score_font_surface.get_rect(topleft=(170,210))
                head_font_surface = score_font.render("HIGH SCORES",True,silver)
                head_rect = score_font_surface.get_rect(topleft=(160,260))
                game_over_screen.blit(score_font_surface,score_rect)
                game_over_screen.blit(head_font_surface,head_rect)
                
            with open(f'highscores/highscore{level}.txt') as score_file:
                i = 1
                for line in score_file:
                    text_surface = font.render(str(i)+".   "+line, True, silver)
                    text_rect = text_surface.get_rect(topleft=(170,300+(i-1)*40))
                    game_over_screen.blit(text_surface,text_rect)
                    i+=1
    
        pygame.display.flip()
        
    return action
        
#######################################################################################################################################
########################################################################################################################################
########################################################################################################################################
#                                              RUN CODE
# the followinng code defines the run function that defines the flow of the code.
#It enables smooth switching of screens by using path variable and the return values of various screens
    
def run_game():
    path=["main_screen"]
    
    while path==["main_screen"]:
        
        act=main_screen()
        path.append(act)
        
        while path==["main_screen","level_screen"]:
            act=level_screen()
            
            if act=="back":
                path=path[0:1]
                break
            
            path.append(act)
            
            while path==["main_screen","level_screen","level_1_screen"]:
                act=level_1_screen()
                
                if act[0]=="back":
                    path=path[0:2]
                    break
                
                path.append(act[0])
                
                while path == ["main_screen","level_screen","level_1_screen","game_over_screen"]:
                    act=game_over_screen(act[1],act[2],act[3])
                    
                    if act == "back":
                        path = path[0:2]
                        break
                
                if path == ["main_screen","level_screen"] : break
            
            while path==["main_screen","level_screen","level_2_screen"]:
                act=level_2_screen()
                
                if act[0]=="back":
                    path=path[0:2]
                    break
                
                path.append(act[0])
                
                while path == ["main_screen","level_screen","level_2_screen","game_over_screen"]:
                    act=game_over_screen(act[1],act[2],act[3])
                    
                    if act == "back":
                        path = path[0:2]
                        break
                
                if path == ["main_screen","level_screen"] : break
            
            
            while path==["main_screen","level_screen","level_3_screen"]:
                act=level_3_screen()
                
                if act[0]=="back":
                    path = path[0:2]
                    break
                
                path.append(act[0])
                
                while path == ["main_screen","level_screen","level_3_screen","game_over_screen"]:
                    act=game_over_screen(act[1],act[2],act[3])
                    
                    if act == "back":
                        path = path[0:2]
                        break
                
                if path == ["main_screen","level_screen"] : break
            
            if path==["main_screen","level_screen"] : continue
                
        while path==["main_screen","help_screen"]:
            act=help_screen()
            
            if act=="back":
                path=path[0:1]
                break
                
        while path==["main_screen","highscores_screen"]:
            act=highscores_screen()
            
            if act=="back":
                path=path[0:1]
                break
            
        if path==["main_screen"] : continue
        
run_game()
            
        
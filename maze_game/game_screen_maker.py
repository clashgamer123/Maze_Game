import pygame,sys,random
from Classes.Player import Player
from Classes.button import button
from prims_maze_algo import generate_maze
from maze_solver import generate_pathfile

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

##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
#                                                GAME SCREEN

#Lets design the general game screen of our maze using prims algorithm.

#All the arguments are passed on to game_screen function

def game_screen(game_screen_size,maze_size,scale,maze_no_cols,maze_no_rows,bar_width,level,speed,cell_dim,cell_img,wall_img,player_dim,forward_ninja_images,back_button_image,score_image,time_temp,key_img,key_temp,no_keys,gem_img,no_gems,time_limit):
    
    # start the bgm
    pygame.mixer.music.load('bgm.mp3')
    pygame.mixer.music.play(-1)
    
    # maze size is the size of the maze that is the complete maze not the one visible.
    # game_screen_size is the size of the rectangle we cut from this maze and make it visible
    # scale is the amount by which we increase the size of this cut part before blitting on the final game_screen
    #bar_width represents the width of the bar in the final game_screen that has various stats like time,score etc
    game_x = game_screen_size[0]
    game_y = game_screen_size[1] 
    
    #note the start time
    start_time = pygame.time.get_ticks()
    
    backward_ninja_images = [pygame.transform.flip(img,True,False) for img in forward_ninja_images]
    clock = pygame.time.Clock()
    
    # Generate the screen
    game_screen = pygame.display.set_mode((game_x*scale,game_y*scale + bar_width))
    maze_screen = pygame.Surface((maze_size[0],maze_size[1]+bar_width))
    
    # Create the back_button object
    back_button=button(0,0,150,50,back_button_image,"Back",26,"Fonts/DragonHunter.otf",gold)
    
    # generate the prims maze and update the solution path
    maze=generate_maze(maze_no_cols,maze_no_rows)
    generate_pathfile(maze,level)
    
    #generate random keys
    cells =[]
    for r in range(maze_no_rows):
        for c in range(maze_no_cols):
            if maze[r][c] == 'c' : cells.append((c*cell_dim,r*cell_dim))
    key_arr = random.sample(cells,no_keys)
    
    #generate random gems
    cells_without_keys = []
    for tuple in cells:
        if tuple not in key_arr:
            cells_without_keys.append(tuple)
    gem_arr = random.sample(cells_without_keys,no_gems)
    
    #Create the player object with initial position x,y=,0
    player = Player(0,0,player_dim,player_dim,forward_ninja_images,backward_ninja_images,speed,maze,0,cell_dim,cell_dim,key_arr,gem_arr)
    
    for i in range(maze_no_cols):
        if maze[0][i] == 'c':
            player.x,player.y=i*cell_dim,0
        if maze[maze_no_rows-1][i] == 'c':
            end_rect = pygame.Rect(i*cell_dim,cell_dim*(maze_no_rows-1),cell_dim,cell_dim)
    
    #initiate some keyboard variables
    key_pressed_down,key_pressed_left,key_pressed_right,key_pressed_up=False,False,False,False
    
    # start the game loop
    run=True
    
    while run:
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if back_button.mouse_clicked(mouse_pos):
                    act = ["back"]
                    run = False
            
            elif event.type == pygame.KEYDOWN:   
            # Set the appropriate flag when a key is pressed
                if event.key == pygame.K_UP:
                    key_pressed_up = True
                elif event.key == pygame.K_DOWN:
                    key_pressed_down = True
                elif event.key == pygame.K_LEFT:
                    key_pressed_left = True
                elif event.key == pygame.K_RIGHT:
                    key_pressed_right = True
                    
            # Reset the flag when a key is released
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    key_pressed_up = False
                elif event.key == pygame.K_DOWN:
                    key_pressed_down = False
                elif event.key == pygame.K_LEFT:
                    key_pressed_left = False
                elif event.key == pygame.K_RIGHT:
                    key_pressed_right = False
                    
            else: pass
         
        # update the player position    
        player.image_update(key_pressed_up,key_pressed_down,key_pressed_left,key_pressed_right)
        
        #update key status
        player.key_checker_update()
        player.gem_checker_update()
        
        # back button mouse hovering check
        mouse_pos = pygame.mouse.get_pos()
        back_button.mouse_hovered(mouse_pos,orangered,30)
        back_button.mouse_not_hovered(mouse_pos,gold,26)
        back_button.draw(game_screen)
        
        #create the maze on the maze screen surface
        maze_screen.fill(black)
          
        # crete the camera_rect ie the rectangle we are going to crop  
        if player.y<=game_y/2 :
            row_up = 0 
            row_down = game_y 
        elif player.y >maze_size[1]-game_y/2 :
            row_up = maze_size[1]-game_y 
            row_down = maze_size[1] 
        elif player.y >game_y/2 and player.y<maze_size[1]-game_y/2 :
            row_up = player.y - game_y/2 
            row_down = player.y + game_y/2
        else : pass
        
        if player.x<=game_x/2 :
            col_up = 0
            col_down = game_x
        elif player.x >=maze_size[0]-game_x/2:
            col_up = maze_size[0]-game_x
            col_down = maze_size[0]
        elif player.x >game_x/2 and player.x<maze_size[0]-game_x/2:
            col_up = player.x - game_x/2
            col_down = player.x + game_x/2
        else : pass
        
        camera_rect = pygame.Rect(col_up,row_up,game_x,game_y)
        
        # Create images of walls,cells of suitable sizes depending on cell_dimension
        cell_img_f = pygame.transform.scale(cell_img,(cell_dim,cell_dim))
        wall_img_f = pygame.transform.scale(wall_img,(cell_dim,cell_dim))
        key_img_f = pygame.transform.scale(key_img,(cell_dim,cell_dim))
        gem_img_f = pygame.transform.scale(gem_img,(cell_dim,cell_dim))
        
        #draw the walls and cells in the maze_screen
        for h in range(0,maze_no_rows):
            for r in range(0,maze_no_cols):
                if maze[h][r] == 'w':
                    maze_screen.blit(wall_img_f,(cell_dim*r,cell_dim*h))
                else:
                    if h == maze_no_rows-1 or h==0 :
                        pygame.draw.rect(maze_screen,gold,(cell_dim*r,cell_dim*h,cell_dim,cell_dim))
                    elif ((r*cell_dim,h*cell_dim) in key_arr  and player.key_checker[(r*cell_dim,h*cell_dim)] == False):
                        maze_screen.blit(cell_img_f,(cell_dim*r,cell_dim*h))
                        maze_screen.blit(key_img_f,(cell_dim*r,cell_dim*h))
                    elif ((r*cell_dim,h*cell_dim) in gem_arr  and player.gem_checker[(r*cell_dim,h*cell_dim)] == False): 
                        maze_screen.blit(cell_img_f,(cell_dim*r,cell_dim*h))
                        maze_screen.blit(gem_img_f,(cell_dim*r,cell_dim*h))
                    else:                
                        maze_screen.blit(cell_img_f,(cell_dim*r,cell_dim*h))
        
        ## Blitting some stats on the bar in game_screen
        
        #Keys status
        game_screen.blit(key_temp,(475,0))
        keys_collected = player.keys_collected()
        keys_font = pygame.font.Font("Fonts/VeniteAdoremus.ttf",26)
        if keys_collected == no_keys:
            # Gold color if all keys collected
            key_surface = keys_font.render(f'Keys {keys_collected}',True,gold)
        else:
            key_surface = keys_font.render(f'Keys {keys_collected}',True,silver)
        key_rect = key_surface.get_rect(center = (600,25))
        game_screen.blit(key_surface,key_rect)
        
        # Time status    
        game_screen.blit(time_temp,(750,0))
        time = (current_time - start_time)//1000
        time_rem = time_limit - time
        time_rem_min = time_rem//60
        time_rem_sec = time_rem%60
        time_font = pygame.font.Font("Fonts/VeniteAdoremus.ttf",26)
        time_surface = time_font.render(f'{time_rem_min}:{time_rem_sec}',True,silver)
        time_rect = time_surface.get_rect(center = (850,25))
        game_screen.blit(time_surface,time_rect)
        
        # Score status
        game_screen.blit(score_image,(150,0))
        score = 10*time_rem + 100*player.gems_collected()
        score_font=pygame.font.Font("Fonts/VeniteAdoremus.ttf",26)
        score_surface=score_font.render(f"Score:{score}",True,orange)
        score_rect=score_surface.get_rect(center=(300,25))
        game_screen.blit(score_surface,score_rect)
        
        player.draw_player(maze_screen)
        
        # Enabling Restricted View
        cut_part = maze_screen.subsurface(camera_rect)
        scaled_cut_part = pygame.transform.scale(cut_part,(game_x*scale,game_y*scale))
        game_screen.blit(scaled_cut_part,(0,bar_width))
        
        if time_rem<=0:
            run = False
            act = ["game_over_screen","lose",level,-1]
        
        if end_rect.colliderect(player.rect) and player.keys_collected() == no_keys :
            act = ["game_over_screen","win",level,score]
            run = False
        pygame.display.flip()
    
    #end the bgm
    pygame.mixer.music.stop()
    
    return act        

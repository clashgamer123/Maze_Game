import pygame

class Player:
    def __init__(self,x,y,width,height,images_r,images_l,speed,maze,bar_width,cell_width,cell_height,key_arr,gem_arr,image_counter = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.images_r = images_r
        self.images_l = images_l
        self.total_images = len(images_r)
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.image_counter = image_counter
        self.dir = 'f'
        self.maze=maze
        self.bar_width=bar_width
        self.cell_width=cell_width
        self.cell_height=cell_height
        self.key_arr = key_arr
        self.key_checker = {key : False for key in key_arr}
        self.gem_arr = gem_arr
        self.gem_checker = {gem : False for gem in gem_arr}
        self.imgfrm=0
    
    ## Collision detection with the walls as well as the boundaries of the maze.
    def collision_checker(self):
        rows = len(self.maze)
        cols = len(self.maze[0]) 
        maze_height = rows*self.cell_height
        maze_width = cols*self.cell_width
        
        collide = False
        
        self.rect.x = self.x
        self.rect.y = self.y
        
        if self.x<0 or self.x>(maze_width-self.width) or self.y<self.bar_width or self.y>(maze_height+self.bar_width-self.height):
            collide = True
            
        
        for r in range(rows):
            for c in range(cols):
                if self.maze[r][c] == 'w':
                    wall_rect = pygame.Rect(c*self.cell_width,r*self.cell_height+self.bar_width,self.cell_width,self.cell_height)
                    if wall_rect.colliderect(self.rect) : collide = True
        
        return collide
    
    ## Update image based on the keyboard keys status in that frame. 
    ## Implemented dual key pressing as well as the feauture that if diagonal movement is not possible the possible movement is taken till the diagonal movement becomes possible
    
    def image_update(self,up,down,left,right):
        
        if (not(left) and not(right)) or (left and right):
            self.image_counter = 0
            self.imgfrm = 0
            self.dir = 'r'
            if up and not down : 
                self.y = self.y - self.speed
                if self.collision_checker() : self.y += self.speed
            elif down and not up :
                self.y = self.y + self.speed
                if self.collision_checker() : self.y -=self.speed
            else : pass 
        
        elif left and not(right):
            self.dir = 'l' 
            self.imgfrm+=0.2
            if int(self.imgfrm%7)==0 : self.imgfrm+=1
            self.image_counter = (int(self.imgfrm)) % (self.total_images)
            
            if (not(up) and not(down)) or (up and down) :
                self.x = self.x - self.speed
                if self.collision_checker() : self.x += self.speed      
            elif up and not down:
                self.x -= self.speed
                self.y -= self.speed
                if self.collision_checker() :
                    self.x+=self.speed
                    if self.collision_checker(): 
                        self.x-=self.speed
                        self.y+=self.speed
                    if self.collision_checker(): self.x+=self.speed
            elif down and not(up):
                self.x -= self.speed
                self.y += self.speed
                if self.collision_checker() :
                    self.x+=self.speed
                    if self.collision_checker(): 
                        self.x-=self.speed
                        self.y-=self.speed
                    if self.collision_checker(): self.x+=self.speed
        
        elif right and not(left):
            self.dir = 'r'
            self.imgfrm+=0.2
            if int(self.imgfrm)%7==0 : self.imgfrm+=1
            self.image_counter = (int(self.imgfrm)) % self.total_images
            if (not(up) and not(down)) or (up and down) :
                self.x = self.x + self.speed
                if self.collision_checker() : self.x -= self.speed      
            elif up and not down:
                self.x += self.speed
                self.y -= self.speed
                if self.collision_checker() :
                    self.x-=self.speed
                    if self.collision_checker(): 
                        self.x+=self.speed
                        self.y+=self.speed
                    if self.collision_checker() : self.x-=self.speed
            elif down and not(up):
                self.x += self.speed
                self.y += self.speed
                if self.collision_checker() :
                    self.x-=self.speed
                    if self.collision_checker(): 
                        self.x+=self.speed
                        self.y-=self.speed
                    if self.collision_checker(): self.x-=self.speed
        
                
    def draw_player(self,screen):
        if self.dir == 'r':
            screen.blit(self.images_r[self.image_counter],(self.x,self.y))
        elif self.dir == 'l':
            screen.blit(self.images_l[self.image_counter],(self.x,self.y))
    
    ## Checks and updates if the key is taken by using the colliderect method for rect objects
    def key_checker_update(self):
        for key in self.key_arr:
            key_rect = pygame.Rect(key[0],key[1],self.cell_width,self.cell_height)
            if self.rect.colliderect(key_rect):
      
                self.key_checker[key] = True
                
    ## Returns number of keys collected till that frame
    def keys_collected(self):
        n = 0
        for key in self.key_arr:
            if self.key_checker[key] == True : n+=1
        return n
    
    ## Checks and updates if the gem is taken by using the colliderect method for rect objects
    def gem_checker_update(self):
        for gem in self.gem_arr:
            gem_rect = pygame.Rect(gem[0],gem[1],self.cell_width,self.cell_height)
            if self.rect.colliderect(gem_rect):
                self.gem_checker[gem] = True
    
    ## Returns number of gems collected till that frame
    def gems_collected(self):
        n = 0
        for gem in self.gem_arr:
            if self.gem_checker[gem] == True : n+=1
        return n
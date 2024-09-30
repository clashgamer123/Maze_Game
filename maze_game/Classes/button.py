import pygame

## Button class for more efficient and fast button making wherever required
## Implement mouse click and mouse hovering detection
## Implement the draw function to directly draw the button on the screen

class button:
    def __init__(self,x,y,width,height,image,text,font_size=36,font_style="None",font_color=(0,0,0)):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.image=image
        self.text=text
        self.font_style=font_style
        self.font_size=font_size
        self.font_color=font_color
    
    def draw(self,screen):
        if self.font_style=="None":
            text_font=pygame.font.Font(None,self.font_size)
        else:
            text_font=pygame.font.Font(self.font_style,self.font_size)
        text_surface=text_font.render(self.text,True,self.font_color)
        text_rect = text_surface.get_rect(center=(self.x+(self.width/2),self.y+(self.height/2)))
        screen.blit(self.image,(self.x,self.y))
        screen.blit(text_surface,text_rect)
    
    def mouse_clicked(self,mouse_pos):
        if mouse_pos[0]>=self.x and mouse_pos[0]<=self.x+self.width and mouse_pos[1]>=self.y and mouse_pos[1]<=self.y+self.height:
            return True
    
    def mouse_hovered(self,mouse_pos,color_update,font_update):
        if mouse_pos[0]>=self.x and mouse_pos[0]<=self.x+self.width and mouse_pos[1]>=self.y and mouse_pos[1]<=self.y+self.height:
            self.font_color=color_update
            self.font_size=font_update
    
    def mouse_not_hovered(self,mouse_pos,color_reset,font_reset):
        if not(mouse_pos[0]>=self.x and mouse_pos[0]<=self.x+self.width and mouse_pos[1]>=self.y and mouse_pos[1]<=self.y+self.height):
            self.font_color=color_reset
            self.font_size=font_reset
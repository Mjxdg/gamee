import pygame
pygame.init()
window=pygame.display.set_mode((1320, 700))
background=pygame.image.load("autumn-landscape-background_1012-302.jpg")
clock=pygame.time.Clock()
class GamesSprite():
    def __init__(self,x=0,y=0,height=0,width=0,step=0,image_sprite=""):
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.step=step
        self.image=pygame.image.load(image_sprite)
        self.image=pygame.transform.scale(self.image,(self.width,self.height))
        self.image.set_colorkey((255, 255, 255))
    def draw(self,x,y):
        window.blit(self.image,(self.x,self.y))
    def update(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x-=self.step
        if keys[pygame.K_RIGHT]:
            self.x+=self.step
        if keys[pygame.K_UP]:
            self.y-=self.step
        if keys[pygame.K_DOWN]:
            self.y+=self.step
        if self.x<0:
            self.x=0
        if self.x>1320-self.width:
            self.x=1320-self.width
        if self.y<0:
            self.y=0
        if self.y>700-self.height:
            self.y=700-self.height
        if event.key==pygame.K.w:
            self.y-=self.step
        if event.key==pygame.K.s:
            self.y+=self.step
        if event.key==pygame.K.a:
            self.x-=self.step
        if event.key==pygame.K.d:
            self.x+=self.step
player=GamesSprite(100,450,100,100,10,"png-transparent-clash-royale-king-clash-royale-clash-of-clans-king-game-prince-game-king-video-game-thumbnail.png")
game=True
while game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
    window.blit(background, (0, 0))
    player.draw(50,50)
    clock.tick(40)
    pygame.display.update()
pygame.quit()

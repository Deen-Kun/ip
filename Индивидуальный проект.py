from pygame import *
from random import randint
okkno = display.set_mode((700, 500))
display.set_caption("mona")

fon1 = transform.scale(image.load('63.jpg'), (700,500))
fon2 = transform.scale(image.load('3.jpg'), (700,500))
dio = transform.scale(image.load('93.png'), (700,500))
curfon = fon1
class boop(sprite.Sprite):
    def __init__(self, img, x,y):
        super().__init__()
        self.image = transform.scale(image.load(img), (90,80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
    def pain(self):
        okkno.blit(self.image, (self.rect.x, self.rect.y))
txt="наруто учил не сдаваться вот я и лежу"
txt2=" нажми w затем s"

font.init()
shrift=font.Font(None,30)

n=1
game = True
while game:
    okkno.blit(curfon, (0,0))
    okkno.blit(dio, (1,100))
    t1 = shrift.render(txt, True, (255,225,225))
    okkno.blit(t1, (120,370))
    t2 = shrift.render(txt2, True, (255,225,225))
    okkno.blit(t2, (120,400))
    for i in event.get():
        if i.type == QUIT:  
            game = False
        if i.type==KEYUP:
            if i.key==K_w and n==1:
                txt="*Яростно проснулся*"
            if i.key==K_s and n==1:
                txt="*Яростно лежит*"
                n=2
                txt2=" нажми a затем q"
            if i.key==K_a  and n==2:
                txt="Больше не ложусь"
            if i.key==K_q  and n==2:
                txt="Уже встал"
                n=3
                curfon=fon2
                txt2=" нажми w затем s"
            if i.key==K_w and n==3:
                txt="*Агресивно сел на кровать*"
            if i.key==K_s and n==3:
                txt="*Протёр глаза руками*"
                n == 4
                txt2=" нажми a затем q"
            if i.key==K_a  and n==2:
                txt="Больше не ложусь"
            if i.key==K_q  and n==2:
                txt="Уже встал"
                n=3
                txt2=" нажми w затем s"
            
                
            
    display.update()
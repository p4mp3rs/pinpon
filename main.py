from pygame import *

window = display.set_mode((600,500))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] == True:
            self.rect.y = self.rect.y - self.speed

        if keys[K_DOWN] == True:
            self.rect.y = self.rect.y + self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] == True:
            self.rect.y = self.rect.y - self.speed

        if keys[K_s] == True:
            self.rect.y = self.rect.y + self.speed

window.fill((255,255,255))

game = True
finish = False

clock = time.Clock()
FPS = 60

player1 = Player('stick.png',30,100,30,500,5)
player2 = Player('stick.png',550,100,30,500,5)
ball = GameSprite('ball.png',300,250,25,25,3)
speed_x = 2
speed_y = 2

while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill((255,255,255))
        player1.update_l()
        player2.update_r()

        ball.rect.x += speed_x 
        ball.rect.y += speed_y 

        if ball.rect.y < 0 or ball.rect.y > 490:
            speed_y = speed_y *-1
        
        if sprite.collide_rect(player1,ball):
            speed_y = speed_y *-1
            speed_x = speed_x *-1
        if sprite.collide_rect(player2,ball):
            speed_y = speed_y *-1
            speed_x = speed_x *-1


        ball.reset()
        player1.reset()
        player2.reset()



    display.update()
    clock.tick(FPS)

    

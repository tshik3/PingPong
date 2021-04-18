from pygame import *

a = 0

class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed, height, width):
        super().__init__()
 
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
 
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def updateL(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
    def updateR(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        global a
        a += 1

Rocket1 = Player("PongRock.png", 30, 250, 10, 100, 20)
Rocket2 = Player("PongRock.png", 650, 250, 10, 100, 20)
Ball = Ball("PongBall.png", 340, 240, 10, 20, 20)

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("PingPong")
background = transform.scale(image.load("PongBack.png"), (win_width, win_height))

game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background,(0,0))
#updates
        Rocket1.updateL()
        Rocket2.updateR()
        Ball.update()
#resets
        Rocket1.reset()
        Rocket2.reset()
        Ball.reset()

        display.update()
        clock.tick(FPS)
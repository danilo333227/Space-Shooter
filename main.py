import pygame

pygame.init()

WIDTH = 700
HEIGHT = 500

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.mixer.init()
pygame.mixer.music.load("space.ogg")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self,image,x,y,width,height,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(image), (width,height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x >0:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.x <= 620:
            self.rect.x += self.speed

background = pygame.transform.scale(pygame.image.load("galaxy.jpg"),(WIDTH,HEIGHT))
player = Player("rocket.png",WIDTH/2 -55,HEIGHT - 100,80,100,10)
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    window.blit(background,(0,0))
    player.reset()
    player.update()
    pygame.display.update()
    clock.tick(60)
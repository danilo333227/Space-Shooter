import random

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
pygame.font.init()
font = pygame.font.Font(None,36)
score = 0
lost = 0

class GameSprite(pygame.sprite.Sprite):
    def __init__(self,image,x,y,width,height,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(image), (width,height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.x <= 620:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet("bullet.png", self.rect.centerx, self.rect.top, 10, 15, 15)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed

        if self.rect.y >= 500:
            self.speed = random.randint(1, 5)
            self.rect.x = random.randint(20, 460)
            self.rect.y = -40
            lost += 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

background = pygame.transform.scale(pygame.image.load('galaxy.jpg'), (WIDTH, HEIGHT))
player = Player('rocket.png', WIDTH / 2 - 80, HEIGHT - 100, 80, 100, 10)

background = pygame.transform.scale(pygame.image.load('galaxy.jpg'), (WIDTH, HEIGHT))
player = Player('rocket.png', WIDTH / 2 - 80, HEIGHT - 100, 80, 100, 10)

monsters = pygame.sprite.Group()
for i in range(1, 10):
    monster = Enemy('ufo.png', random.randint(20, 460), -40, 80, 50, random.randint(1, 3))
    monsters.add(monster)

bullets = pygame.sprite.Group()

game = True
finish = False
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.fire()


    window.blit(background, (0, 0))
    player.reset()
    player.update()
    if not finish:
        window.blit(background, (0, 0))

        text_score = font.render(f'Рахунок: {score}', True, (250, 250, 250))
        window.blit(text_score, (10, 20))

        text_score = font.render(f'Пропущені: {lost}', True, (250, 250, 250))
        window.blit(text_score, (10, 50))

        player.reset()
        player.update()
        monsters.update()
        bullets.update()
        monsters.draw(window)
        bullets.draw(window)

    if lost > 5:
        window.blit(background, (0, 0))
        text_lose = font.render('Ти програв!!!', True, (250, 0, 0))
        window.blit(text_lose, (WIDTH/2-100, HEIGHT/2))
        finish = True

    pygame.display.update()
    clock.tick(60)
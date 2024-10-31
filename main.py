import pygame
import random

class Game:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Galaxy Defender")    # Game title <<<<
        self.clock = pygame.time.Clock()
        self.running = True
        self.spaceship = Spaceship(self, 370, 515)

        self.enemies = []
        for i in range(12):
            self.enemies.append(Enemy(self, random.randint(0, 736), random.randint(30, 130)))

        self.background_img = pygame.image.load("img/background.png")    # Background image src <<<<

        while self.running:
            self.clock.tick(60)     # FPS <<<<
            
            self.screen.blit(self.background_img, (0,0))    # Background image <<<<
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                    # Movement Spaceship 
                if event.type == pygame.KEYDOWN:         
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.spaceship.move(-15)
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.spaceship.move(15)
                    if event.key == pygame.K_SPACE:
                        self.spaceship.fire_bullet()       # Spaceship Fire <<<<

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                     self.spaceship.move(15)
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.spaceship.move(-15)


            self.spaceship.update()
            if len(self.spaceship.bullets) > 0:
                for bullet in self.spaceship.bullets:
                    if bullet.is_fired == True:
                        bullet.update()
                    else:
                        self.spaceship.bullets.remove(bullet)


            for enemy in self.enemies:
                enemy.update()

            
            pygame.display.update()



class Spaceship:
    def __init__(self,game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.change_x = 0
        self.spaceship_img = pygame.image.load("img/spaceship.png")    # Spaceship image src <<<<
        self.bullets = []
    

    def fire_bullet(self):                        #  Bullet method <<<<
        self.bullets.append(Bullet(self.game, self.x, self.y))
        self.bullets[len(self.bullets) - 1].fire()


    def move(self, speed):
        self.change_x += speed

    def update(self):
        self.x += self.change_x
        if self.x < 0:                      #  Level-Area Ending Left  <<<<
            self.x = 0
        elif self.x > 736:
            self.x = 736                    #  Level-Area Ending Right  <<<<

        self.game.screen.blit(self.spaceship_img, (self.x, self.y))    # Spaceship image <<<<


class Bullet:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game
        self.bullet_img = pygame.image.load("img/bullet.png")    # Bullet image src <<<<
        self.speed = 10
    
    def fire(self):                  #  Bullet Fire method <<<<
        self.is_fired = True

    def update(self):
        self.y -= self.speed
        if self.y < 0:
            self.is_fired = False
        self.game.screen.blit(self.bullet_img, (self.x, self.y))


class Enemy:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.change_x = 5
        self.change_y = 60
        self.enemy_img = pygame.image.load("img/enemy.png")    # Enemy image src <<<<

    def update(self):
        self.x += self.change_x                         # dynamic movement aliens <<<<  
        if self.x > 736:                                
            self.y += self.change_y                       
            self.change_x = -5
        elif self.x <= 0:  
            self.y += self.change_y
            self.change_x = 5                        
        self.game.screen.blit(self.enemy_img, (self.x, self.y))


if __name__ == "__main__":
    game = Game(800, 600)
    print(__file__)
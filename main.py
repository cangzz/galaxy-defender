import pygame

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

        self.background_img = pygame.image.load("img/background.png")    # Background image src <<<<

        while self.running:
            self.clock.tick(60)     # FPS <<<<
            
            self.screen.blit(self.background_img, (0,0))    # Background image <<<<
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                    # Movement Spaceship 
                if event.type == pygame.KEYDOWN:         
                    if event.key == pygame.K_LEFT:
                        self.spaceship.move(-15)
                    if event.key == pygame.K_RIGHT:
                        self.spaceship.move(15)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                     self.spaceship.move(15)
                    if event.key == pygame.K_RIGHT:
                        self.spaceship.move(-15)

            self.spaceship.update()
            pygame.display.update()



class Spaceship:
    def __init__(self,game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.change_x = 0
        self.spaceship_img = pygame.image.load("img/spaceship.png")    # Spaceship image src <<<<


    def move(self, speed):
        self.change_x += speed

    def update(self):
        self.x += self.change_x
        if self.x < 0:                      #  Level-Area Ending Left<<<<
            self.x = 0
        elif self.x > 736:
            self.x = 736                    #  Level-Area Ending Right<<<<

        self.game.screen.blit(self.spaceship_img, (self.x, self.y))    # Spaceship image <<<<

if __name__ == "__main__":
    game = Game(800, 600)
    print(__file__)
import pygame
import time
from paddle import*
from ball import*

class Game():

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800,600))
        self.bg = pygame.image.load("images/bg.webp")
        self.bg = pygame.transform.scale(self.bg, (800, 600))

        self.paddle = pygame.image.load("images/paddle.jpg")
        self.paddle = pygame.transform.scale(self.paddle, (50, 50))

        self.player = Paddle(self.window, 350, 450, self.paddle)

        self.ball_img = pygame.image.load("images/ball.png")
        self.ball_img = pygame.transform.scale(self.ball_img,(32,32))
        self.ball = Ball(self.window, self.ball_img,350,350)
        self.clock = pygame.time.Clock()

    def run(self):

        running = True
        while (running):
            delta_time = self.clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.window.blit(self.bg, (0,0))
            self.player.draw()
            self.player.move(delta_time)
            self.ball.draw()
            self.ball.move(delta_time)
        

            pygame.display.update()

game = Game()
game.run()
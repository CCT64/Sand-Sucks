import pygame

class Ball():
    def __init__(self,window,image,x,y):
        self.window = window
        self.image = image
        self.ball_rect = self.image.get_rect(x = x, y = y)

        self.velocity_x = 150
        self.velocity_y = 150

    def draw(self):
        self.window.blit(self.image, (self.ball_rect_x, self.ball_rect.y))

    def move(self,delta_time):
        self.ball_rect.x += self.velocity_x * delta_time
        self.ball_rect.y += self.velocity_y * delta_time
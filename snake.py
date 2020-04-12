# pylint: disable=no-member

import pygame
import sys
import time
import random
import sys

pygame.init()
d_width = 640 
d_height = 376 

screen = pygame.display.set_mode((d_width,d_height))
pygame.display.set_caption('Snake and stars')


backgroundImage = pygame.image.load('1.png')


class Food:

    def __init__(self):

        self.x = random.randint(70, 570)

        self.y = random.randint(70, 306)

        self.image = pygame.image.load("star3.png")



    def draw(self):

        screen.blit(self.image, (self.x, self.y))

    

    def eat(self):

        if (self.x in range(snake.elements[0][0] - self.image.get_size()[0], snake.elements[0][0])) and (self.y  in range(snake.elements[0][1] - self.image.get_size()[1], snake.elements[0][1])):

            snake.is_add = True

point = pygame.font.Font(None, 30)

class Snake:
    def __init__(self):

        self.size = 1

        self.elements = [[100, 100]]

        self.radius = 10

        self.dx = 5  # right

        self.dy = 0

        self.is_add = False



    def draw(self):

        for element in self.elements:

            pygame.draw.circle(screen, (0, 255, 0), element, self.radius)



    def add_to_snake(self):

        self.size += 1

        self.elements.append([0, 0])

        food.x = random.randint(60, 580)

        food.y = random.randint(60, 316 )

        self.is_add = False

        

    def move(self):

        if self.is_add:

            self.add_to_snake()



        for i in range(self.size - 1, 0, -1):

            self.elements[i][0] = self.elements[i - 1][0]

            self.elements[i][1] = self.elements[i - 1][1]



        self.elements[0][0] += self.dx

        self.elements[0][1] += self.dy

foodImage = pygame.image.load("star3.png")
pointplus = 0

def scores (x,y, score):

    sc = point.render('Points: ' + str(pointplus), True, (0, 0, 0))

    screen.blit(sc, (x, y))



def end():

    if (snake.elements[0][0] > 640 - 30 or snake.elements[0][0] < 30) or (snake.elements[0][1] >376 - 30 or snake.elements[0][1] < 30):

        return False



snake = Snake()

food = Food()



running = True



gg = 3



FPS = 60



clock = pygame.time.Clock()



while running:

    mill = clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                running = False

            if event.key == pygame.K_RIGHT:

                snake.dx = gg

                snake.dy = 0

            if event.key == pygame.K_LEFT:

                snake.dx = -gg

                snake.dy = 0

            if event.key == pygame.K_UP:

                snake.dx = 0

                snake.dy = -gg

            if event.key == pygame.K_DOWN:

                snake.dx = 0

                snake.dy = gg

    

    for i in range(1, len(snake.elements)):

        if (snake.elements[0][0] == snake.elements[i][0] and snake.elements[0][1] == snake.elements[i][1]):

            running = False

    

    if end() == False:

        running = False



    if snake.is_add == True:

        pointplus += 1

    

    screen.blit(backgroundImage, (0, 0))

    end()

    snake.move()

    food.eat()

    snake.draw()

    food.draw()

    scores(0, 0, pointplus)

    pygame.display.flip()



pygame.quit()
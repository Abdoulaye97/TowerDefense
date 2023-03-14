import pygame


class Monstre:
    def __init__(self, positionX, positionY):
        self.image_monstre = pygame.image.load("alien.png")
        self.image_monstre = pygame.transform.scale(self.image_monstre, (30, 30))
        self.positionX=positionX
        self.positionY=positionY
        self.vitesse = 6
        self.direction_x = 0
        self.direction_y = 0

    def move(self):

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.direction_y = -1
                    self.positionY +=self.direction_y * self.vitesse
                elif event.key == pygame.K_DOWN:
                    self.direction_y = 1
                    self.positionY +=self.direction_y * self.vitesse
                elif event.key == pygame.K_LEFT:
                    self.direction_x = -1
                    self.positionX+=self.direction_x * self.vitesse
                elif event.key == pygame.K_RIGHT:
                    self.direction_x = 1
                    self.positionX +=self.direction_x * self.vitesse


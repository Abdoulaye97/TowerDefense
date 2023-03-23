import pygame



class Monstre(pygame.sprite.Sprite):
    def __init__(self, positionX, positionY):
        super().__init__()
        self.image_monstre = pygame.image.load("alien.png")
        self.image_monstre = pygame.transform.scale(
            self.image_monstre, (30, 30))
        self.positionX = positionX
        self.positionY = positionY
        self.vitesse = 3
        self.direction_x = 0
        self.direction_y = 0
        self.attente = 10

    def update(self):
        self.positionY = self.direction_y
        self.positionY = self.positionX

    def position_depart(self):
        self.positionX = 84
        self.positionY = 480

    def move(self):

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.direction_y = -1
                    self.positionY += self.direction_y * self.vitesse
                elif event.key == pygame.K_DOWN:
                    self.direction_y = 1
                    self.positionY += self.direction_y * self.vitesse
                elif event.key == pygame.K_LEFT:
                    self.direction_x = -1
                    self.positionX += self.direction_x * self.vitesse
                elif event.key == pygame.K_RIGHT:
                    self.direction_x = 1
                    self.positionX += self.direction_x * self.vitesse

        print("{0},{1}".format(self.positionX, self.positionY))

    def draw_monstre(self, screen, pixels):

        clock = pygame.time.Clock()
        if self.positionY != 324 and self.positionX == 84:
            self.positionY -= self.vitesse
            screen.blit(self.image_monstre, (
                self.positionX + pixels, self.positionY + pixels))
            pygame.display.update()
            pygame.time.delay(self.attente)
        elif self.positionX != 564 and self.positionY == 324:
            self.positionX += self.vitesse
            screen.blit(self.image_monstre, (
                self.positionX + pixels, self.positionY + pixels))
            pygame.display.update()
            pygame.time.delay(self.attente)
        elif self.positionY != 42 and self.positionX == 564:
            self.positionY -= self.vitesse
            screen.blit(self.image_monstre, (
                self.positionX + pixels, self.positionY + pixels))
            pygame.display.update()
            pygame.time.delay(self.attente)
        elif self.positionX != 165 and self.positionY == 42:
            self.positionX -= self.vitesse
            screen.blit(self.image_monstre, (
                self.positionX + pixels, self.positionY + pixels))
            pygame.display.update()
            pygame.time.delay(self.attente)
        elif self.positionX == 165 and self.positionY != -72:
            self.positionY -= self.vitesse
            screen.blit(self.image_monstre, (
                self.positionX + pixels, self.positionY + pixels))
            pygame.display.update()
            pygame.time.delay(self.attente)
            if self.positionX == 165 and self.positionY == -72:
                self.position_depart()

import pygame

from word import *

class Monstre(pygame.sprite.Sprite):
    def __init__(self, positionX, positionY):
        super().__init__()
        self.image_monstre = pygame.image.load("Assets/alien.png").convert_alpha()
        self.image_monstre = pygame.transform.scale(self.image_monstre, (30, 30))
        self.positionX = positionX
        self.positionY = positionY
        self.vitesse = 3
        self.health = 2
        self.direction_x = 0
        self.direction_y = 0
        self.nbr_vie = 50
        self.nbr_vie_max = 50
        self.degat = 25
        self.positions_visitees = []
        self.position_monstre = [11, 3]

    # def position_depart(self):
    #     self.positionX = 84
    #     self.positionY = 480

    def update_bar_de_vie(self, surface):
        # j'ai defini un code couleurs rouge qui va etre au dessus du monstre qui etre son niveau de vie
        bar_color = (231, 52, 14)
        # la position va permetrre le niveaux de vie se deplace avec le monstre
        position = [self.positionX + 30, self.positionY + 36, self.nbr_vie, 3]
        # couleur de l'arriere plan qui va permettre devoir si le monstre a subit un degat
        couleur_arriere_plan = (60, 63, 60)
        # la position de l'arriere plan
        position_arriere_plan = [self.positionX + 30, self.positionY + 36, self.nbr_vie_max, 3]
        pygame.draw.rect(surface, couleur_arriere_plan, position_arriere_plan)
        pygame.draw.rect(surface, bar_color, position)

    def move(self):

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.direction_y = -1
                    self.positionY += self.direction_y * 3
                elif event.key == pygame.K_DOWN:
                    self.direction_y = 1
                    self.positionY += self.direction_y * 3
                elif event.key == pygame.K_LEFT:
                    self.direction_x = -1
                    self.positionX += self.direction_x * 5
                elif event.key == pygame.K_RIGHT:
                    self.direction_x = 1
                    self.positionX += self.direction_x * 3

        print("{0},{1}".format(self.positionX, self.positionY))

    # def est_position_valide(position):
    #     positionX, positionY = position
    #     return 0 <= positionX < len(word) and 0 <= positionY < len(word[0]) and word[positionX][positionY] == 0

    def draw_monstre_map_1(self, screen, pixels):
        screen.blit(self.image_monstre, (self.positionX + pixels, self.positionY + pixels))
        if self.positionX - 1 >= 0:# and self.est_position_valide([self.positionX - 1, self.positionY]) and [self.positionX - 1, self.positionY] not in self.positions_visitees:
            self.positionX -= self.vitesse  # Déplacer vers le haut
        elif self.positionX + 1 < len(word):# and self.est_position_valide([self.positionX + 1, self.positionY]) and [self.positionX + 1, self.positionY] not in self.positions_visitees:
            self.positionX += self.vitesse  # Déplacer vers le bas
        elif self.positionY + 1 < len(word[0]):# and self.est_position_valide([self.positionX, self.positionY + 1]) and [self.positionX, self.positionY + 1] not in self.positions_visitees:
            self.positionY += self.vitesse  # Déplacer vers la droite
        elif self.positionY - 1 >= 0:# and self.est_position_valide([self.positionX, self.positionY - 1]) and [self.positionX, self.positionY - 1] not in self.positions_visitees:
            self.positionY -= self.vitesse  # Déplacer vers la gauche

    def draw_monstre_map_2(self, screen, pixels):
        screen.blit(self.image_monstre, (self.positionX + pixels, self.positionY + pixels))
        # Dans ces conditions on verifies la position initiale du joueur lors du creation de l'objet si cette position respecte les conditions le monstre pourra se deplacer
        if self.positionY != 327 and self.positionX == 84:
            self.positionY -= self.vitesse
        elif self.positionX != 123 and self.positionY == 327:
            self.positionX += self.vitesse
        elif self.positionY != 288 and self.positionX == 123:
            self.positionY -= self.vitesse
        elif self.positionX != 168 and self.positionY == 288:
            self.positionX += self.vitesse
        elif self.positionY != 165 and self.positionX == 168:
            self.positionY -= self.vitesse
        elif self.positionX != 489 and self.positionY == 165:
            self.positionX += self.vitesse
        elif self.positionY != 84 and self.positionX == 489:
            self.positionY -= self.vitesse
        elif self.positionX != 444 and self.positionY == 84:
            self.positionX -= self.vitesse

        elif self.positionX == 444 and self.positionY != -78:
            self.positionY -= self.vitesse

            if self.positionX == 444 and self.positionY == -75:
             pass

    def draw_monstre_map_3(self, screen, pixels):
        screen.blit(self.image_monstre, (self.positionX + pixels, self.positionY + pixels))
        if self.positionY != 327 and self.positionX == 84:
            self.positionY -= self.vitesse
        elif self.positionX != 123 and self.positionY == 327:
            self.positionX += self.vitesse
        elif self.positionY != 288 and self.positionX == 123:
            self.positionY -= self.vitesse
        elif self.positionX != 489 and self.positionY == 288:
            self.positionX += self.vitesse
        elif self.positionY != 168 and self.positionX==489:
            self.positionY -=self.vitesse
        elif self.positionX !=165 and self.positionY==168:
            self.positionX -=self.vitesse

        elif self.positionX == 165 and self.positionY != -78:
            self.positionY -= self.vitesse

            if self.positionX == 165 and self.positionY == -75:
               pass

    def update_monstre(self, screen, pixels):
        screen.blit(self.image_monstre, (self.positionX + pixels, self.positionY + pixels))

    def getPositionY(self):
        print("Position X et Y: {0},{1}".format(self.positionX, self.positionY))
        # print("Taille {0}".format(self.image_monstre.get_size()))

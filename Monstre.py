from collections import deque
from datetime import time
from random import random

import pygame


class Monstre(pygame.sprite.Sprite):
    def __init__(self, positionX, positionY):
        super().__init__()
        self.image_monstre = pygame.image.load("Assets/alien.png")
        self.image_monstre = pygame.transform.scale(
           self.image_monstre, (35, 30))
        self.positionX = positionX
        self.positionY = positionY
        self.rect = self.image_monstre.get_rect()
        self.rect.x = self.positionX
        self.rect.y = self.positionY

        self.rect.width = self.image_monstre.get_width()-10
        self.rect.center = (self.positionX, self.positionY)

        self.rect.height = self.image_monstre.get_height()-2
        self.vitesse = 3
        self.health = 2
        self.direction_x = 0
        self.direction_y = 0
        self.nbr_vie = 50
        self.nbr_vie_max = 50
        self.degat = 25
        self.positions_visitees = set()
        self.position_monstre = [self.positionX, self.positionY]

    @classmethod
    def detecter_collision_monstres(cls, monstres, projectiles):

        for monstre in monstres:
            for projectile in projectiles:
                if monstre.rect.colliderect(projectile.rect):
                    # Collision détectée entre le monstre et le projectile
                    monstre.nbr_vie -= 5
                    projectiles.remove(projectile)  # Supprimer le projectile lorsqu'il touche le monstre
                    print("Monstre touché !")

                    if monstre.nbr_vie <= 0:
                        monstres.remove(monstre)


    def position_depart(self):
        self.positionX = 84
        self.positionY = 480

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

    def show_message(self, screen, message):
        font = pygame.font.Font(None, 24)  # Définir la police et la taille du texte
        text = font.render(message, True,
                           (255, 255, 255))  # Créer une surface de texte avec le message et la couleur blanche
        text_rect = text.get_rect(center=self.rect.center)  # Obtenir le rectangle du texte centré sur le monstre
        screen.blit(text, text_rect)  # Afficher le texte à l'écran

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

    def draw_monstre_map_1(self, screen, pixels):
        if self.image_monstre is not None:
            screen.blit(self.image_monstre, (self.positionX+pixels, self.positionY+pixels))
            pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

            if self.positionY != 324 and self.positionX == 84:
                self.positionY -= self.vitesse

            elif self.positionX != 564 and self.positionY == 324:
                self.positionX += self.vitesse

            elif self.positionY != 42 and self.positionX == 564:
                self.positionY -= self.vitesse

            elif self.positionX != 165 and self.positionY == 42:
                self.positionX -= self.vitesse

            elif self.positionX == 165 and self.positionY != -78:
                self.positionY -= self.vitesse

                if self.positionX == 165 and self.positionY == -75:
                    # self.position_depart()
                    pass

    def draw_monstre_map_2(self, screen, pixels):
        if self.image_monstre is not None:
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
        elif self.positionY != 168 and self.positionX == 489:
            self.positionY -= self.vitesse
        elif self.positionX != 165 and self.positionY == 168:
            self.positionX -= self.vitesse

        elif self.positionX == 165 and self.positionY != -78:
            self.positionY -= self.vitesse

            if self.positionX == 165 and self.positionY == -75:
                # self.position_depart()
                pass

    def update_monstre(self, screen, pixels):
        screen.blit(self.image_monstre, (self.positionX + pixels, self.positionY + pixels))

    def getPositionY(self):
        print("Position X et Y: {0},{1}".format(self.positionX, self.positionY))
        # print("Taille {0}".format(self.image_monstre.get_size()))

    def detecter_collision_projectilea(self, projectiles):
        for projectile in projectiles:
            if self.rect.colliderect(projectile.rect):
                self.nbr_vie -= 5
                print("touche")

    def detecter_collision_projectileee(self, projectiles):
        for projectile in projectiles:
            if self.rect.collidepoint(projectile.rect.center):
                self.nbr_vie -= 5
                projectiles.remove(projectile)  # Supprimer le projectile lorsqu'il touche le monstre
                print("touché")

                if self.nbr_vie <= 0:
                    # Le monstre est mort, ajoutez ici le code correspondant
                    self.remove()

    def detecter_collision_projectile(self, projectiles):
        monstre_touche = False  # Variable pour indiquer si le monstre a été touché

        for projectile in projectiles:
            if self.rect.colliderect(projectile.rect):
                self.nbr_vie -= 5
                projectiles.remove(projectile)  # Supprimer le projectile lorsqu'il touche le monstre
                print("touché")

                if self.nbr_vie <= 0:
                    monstre_touche = True  # Le monstre a été touché

        if monstre_touche:
            # Code pour supprimer le monstre et les projectiles associés
            self.remove()  # Supprimer le monstre

            # Supprimer les projectiles restants qui sont associés à ce monstre
            for projectile in projectiles.copy():
                if projectile.monstre == self:
                    projectiles.remove(projectile)

    def update_projectille(self, projectiles):
        self.detecter_collision_projectile(projectiles)

    def remove(self):
        # Ajoutez ici la logique pour faire disparaître le monstre
        # Par exemple, vous pouvez le rendre invisible en définissant son attribut image à None :
        print(self.rect)

    def update_velocite_rect(self):
        self.rect.x = self.positionX+45
        self.rect.y = self.positionY+42




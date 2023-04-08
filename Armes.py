import pygame
import math


class Arme:

    def __init__(self, position_x, position_y, image, type):
        self.type = type
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (60, 50)).convert()
        self.position_x = position_x
        self.position_y = position_y
        self.rect = self.image.get_rect(center=(position_x, position_y))
        self.ArmeCopiee = None
        self.position = (position_x, position_y)
        self.selectionne = False  # Ajout de l'attribut selectionne

    def type_arme(self, screen, pixels):
        if self.type == "arme_1":
            screen.blit(self.image, (self.position_x + pixels, self.position_y + pixels))

    def placer_armes(self, screen, word, pixels):
        matrix_width = len(word[0])
        matrix_height = len(word)
        if self.type == "arme_1":
            for i in range(matrix_height):
                # Boucler sur chaque colonne de la matric
                for j in range(matrix_width):
                    # Déterminer la position de la cellule dans la grille
                    x = j * pixels
                    y = i * pixels
                    # on récupère chaque valeur de la matrice
                    cellule = word[i][j]
                    if cellule == 3:
                        # On redimensionne l'image pour qu'il prenne la taille de la cellule
                        image = pygame.image.load("Assets/Armes/wals.png")
                        image = pygame.transform.scale(image, (pixels, 40))
                        # on recupere un rectangle de l'image
                        rect = image.get_rect(
                            center=(x + pixels / 2, y + pixels / 2))
                        screen.blit(image, rect)

                        self.image = pygame.transform.scale(self.image, (pixels, 40))
                        rect = image.get_rect(
                            center=(x + pixels / 2, y + pixels / 2))
                        screen.blit(self.image, rect)

    def tirer(self, position_monstre, screen):
        dx = position_monstre[0] - self.position_x
        dy = position_monstre[1] - self.position_y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance < 100:  # check if the monster is within range
            angle = math.atan2(dy, dx)  # calculate the angle towards the monster
            rotated_image = pygame.transform.rotate(self.image, math.degrees(-angle))
            new_rect = rotated_image.get_rect(center=self.rect.center)
            screen.blit(self.image, new_rect)

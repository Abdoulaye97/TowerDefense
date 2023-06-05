import math

import pygame
from pygame.sprite import Sprite


class Projectile(Sprite):

     def __init__(self, start_position_x, start_position_y, target_position, image):
        super().__init__()
        self.start_position_x = start_position_x
        self.start_position_y = start_position_y
        self.target_position = target_position
        self.image = image
        # self.image = pygame.image.load("Assets/image/Bullet1.png")
        self.image = pygame.transform.scale(self.image, (10, 10)).convert_alpha()
        self.rect = self.image.get_rect(center=(start_position_x, start_position_y))
        dx = target_position[0] - start_position_x
        dy = target_position[1] - start_position_y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        # Normaliser le vecteur de direction
        if distance != 0:
            direction_x = dx / distance
            direction_y = dy / distance
        else:
            direction_x = 0
            direction_y = 0

        # Définir la vitesse du projectile
        speed = 4  # Vitesse de déplacement du projectile

        # Définir les valeurs de vitesse en fonction du vecteur de direction
        self.velocity_x = direction_x * speed
        self.velocity_y = direction_y * speed
        # ... Autres attributs du projectile ...

     def updates(self, monster_position):
        # Calculer la direction entre le projectile et le monstre
        dx = monster_position[0] - self.start_position_x
        dy = monster_position[1] - self.start_position_y
        # Normaliser la direction pour obtenir un vecteur unitaire
        direction_length = math.sqrt(dx ** 2 + dy ** 2)
        if direction_length != 0:
            direction_x = dx / direction_length
            direction_y = dy / direction_length
            # Mettre à jour la position du projectile en fonction de la direction
            speed = 5  # Vitesse du projectile (à ajuster selon vos besoins)
            self.start_position_x += direction_x * speed
            self.start_position_y += direction_y * speed

     def update(self):
        self.start_position_x += self.velocity_x
        self.start_position_y += self.velocity_y
        self.rect.center = (self.start_position_x, self.start_position_y)

     def draw(self, screen):
        # Dessiner le projectile à l'écran
         screen.blit(self.image, self.rect)




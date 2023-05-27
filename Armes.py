import pygame
import math
from Projectille import Projectile


class Arme:

    def __init__(self, position_x, position_y, image, types):
        self.type = types
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (80, 70)).convert()
        self.position_x = position_x
        self.position_y = position_y
        self.rect = self.image.get_rect(center=(position_x, position_y))
        self.position = (position_x, position_y)
        self.start = False
        self.is_placed = False
        self.angle = 0  # Angle de rotation initial
        self.rotated_image = self.image  # Image tournée
        self.all_projectilles = pygame.sprite.Group()
        self.cadenas_image = pygame.image.load("Assets/Armes/lock_ability.jpg")
        self.cadenas_visible = True
        self.cout_arme = 50
        self.deverrouille = False
        self.check_arme = True

    def draw_armes(self, window):

        window.blit(self.image, (self.position_x, self.position_y))
        if self.cadenas_visible:
            window.blit(self.cadenas_image, (self.position_x, self.position_y))

    def acheter(self, joueur):
        if joueur.argent >= self.cout_arme:
            joueur.argent -= self.cout_arme
            self.cadenas_visible = False

    def cliquer(self, joueur):
        if self.cadenas_visible and joueur.argent >= self.cout_arme:
            joueur.argent -= self.cout_arme
            self.cadenas_visible = False

    def is_clicked_armes(self, mouse_pos):
        rect = self.image.get_rect().move(self.position_x, self.position_y)
        return rect.collidepoint(mouse_pos)

    def resize_image(self, size):
        self.image = pygame.transform.scale(self.image, size)

    def update_position(self, x, y):

        self.position_x = x
        self.position_y = y

    def type_arme(self
                  , screen, pixels):
        if self.type == "arme_1":
            screen.blit(self.image, (self.position_x + pixels, self.position_y + pixels))

    @classmethod
    def detecter_montres(cls, armes, monster_position):
        distance_min = 200
        for arme in armes:
            distance = math.sqrt(
                (arme.position_x - monster_position[0]) ** 2 + (arme.position_y - monster_position[1]) ** 2)
            if distance <= distance_min:
                pass
                # print("tirer")

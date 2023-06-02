import time

import pygame
import math
from Projectille import Projectile


class Arme:
    all_projectiles = pygame.sprite.Group()
    last_shot_time = 0
    shot_delay = 0.1  # Délai en secondes entre chaque lancement de projectile
    arme_en_tir = True
    projectile_delay = 0.3

    def __init__(self, position_x, position_y, image, types):

        # self.rotated_rect = self.image
        # self.position_tir_x = None
        # self.position_tir_y = None
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
        self.is_selected = False
        self.selected = False
        self.direction = (0, 0)

    def draw_armes(self, window):

        window.blit(self.image, (self.position_x, self.position_y))
        if self.cadenas_visible:
            window.blit(self.cadenas_image, (self.position_x, self.position_y))

    def draw_armess(self, is_placed, window):
        if is_placed:  # Vérifier si l'arme est placée
            rotated_image = pygame.transform.rotate(self.image, self.angle)
            rotated_rect = rotated_image.get_rect(center=(self.position_x, self.position_y))
            window.blit(rotated_image, rotated_rect)
        else:
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
        self.image.set_colorkey((0, 0, 0))

    def update_position(self, x, y):

        self.position_x = x
        self.position_y = y

    def type_arme(self
                  , screen, pixels):
        if self.type == "arme_1":
            screen.blit(self.image, (self.position_x + pixels, self.position_y + pixels))

    @classmethod
    def detecter_monstres(cls, armes, monster_position, champ_vision):
        distance_min = 200
        for arme in armes:
            distance = math.sqrt(
                (arme.position_x - monster_position[0]) ** 2 + (arme.position_y - monster_position[1]) ** 2)

            if distance <= distance_min and distance <= champ_vision:
                cls.lancer_projectiles(arme.position_x, arme.position_y, monster_position)

    @classmethod
    def lancer_projectiles(cls, position_x, position_y, target_position):
        current_time = time.time()
        if current_time - cls.last_shot_time >= cls.projectile_delay:
            projectile_image = pygame.image.load("Assets/Armes/Bullet1.png").convert_alpha()
            projectile = Projectile(position_x + 25, position_y - 3, target_position, projectile_image)
            cls.all_projectiles.add(projectile)
            cls.last_shot_time = current_time

    @classmethod
    def lancer_projectiless(cls, position_x, position_y, target_position):
        projectile = Projectile(position_x + 25, position_y - 3, target_position)
        cls.all_projectiles.add(projectile)

    @classmethod
    def detecter_collision_projectile_monstre(cls, projectile, monstre):
        print("Vérification de collision entre projectile et monstre")
        if projectile.rect.colliderect(monstre.rect):
            print("Le projectile a touché le monstre!")

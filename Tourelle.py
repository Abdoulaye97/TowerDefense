import pygame

class Tourelle:
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Assets/Armes/arme.png")
        self.rect = self.image.get_rect()
        self.degats = 10

    def draw(self, screen):
        screen.blit(self.image, (40,520))

    def attaquer(self, monstre):
        monstre.health -= self.degats

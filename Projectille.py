import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self, arme):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load("Assets/projectile.png")
        self.image = pygame.transform.scale(self.image,(50, 50))
        self.rect = self.image.get_rect
        #self.rect.x=arme.position_x
       # self.rect.y = arme.position_y

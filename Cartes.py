import pygame


class Carte:
    # le constrcteur pour creer un bouton Menu
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (250, 200)).convert()
        self.rect = self.image.get_rect(center=(x, y))

    # cet fonction permet de verifier si notre button est cliquer
    def is_clicked_map(self, position):
        # verifie si le bouton et le souris sont au meme coordonnes au clik
        if self.rect.collidepoint(position):
            self.start = True
            return True
        else:
            return False

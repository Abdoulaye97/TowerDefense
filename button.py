import pygame


class Button:
    # le constrcteur pour creer un bouton Menu
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path)
        self.image=pygame.transform.scale(self.image, (150, 100)).convert()
        self.rect = self.image.get_rect(center=(x, y))
        self.start = False

    # cet fonction permet de verifier si notre button est cliquer
    def is_clicked(self, mouse_pos):
        # verifie si le bouton et le souris sont au meme coordonnes au clik
        if self.rect.collidepoint(mouse_pos):
            self.start = True
            return True
        else:
            return False

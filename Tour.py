import pygame
import os

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Tower Defense")

# Paramètres du jeu
FPS = 60

# Couleurs
WHITE = (255, 255, 255)

# Images
BACKGROUND_IMG = pygame.image.load("Assets/Background.png")
TOWER_IMG = pygame.image.load("Assets/alien.png")

# Classe pour les tours
class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = TOWER_IMG

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

# Fonction principale du jeu
def main():
    clock = pygame.time.Clock()
    run = True
    towers = []
    placing_tower = False

    while run:
        clock.tick(FPS)
        WINDOW.fill(WHITE)
        WINDOW.blit(BACKGROUND_IMG, (0, 0))

        # Afficher l'image de la tour
        WINDOW.blit(TOWER_IMG, (0, 0))

        # Dessiner les tours
        for tower in towers:
           tower.draw(WINDOW)

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if placing_tower:
                    towers.append(Tower(x, y))
                    placing_tower = False
                else:
                    if 0 < x < 100 and 0 < y < 100:
                        placing_tower = True

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()

import pygame

# Paramètres de la fenêtre
SCREEN_WIDTH =1800
SCREEN_HEIGHT = 1600
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


# Classe pour les armes
class Weapon:
    def __init__(self, image, position):
        self.image = image
        self.position = position

    def draw(self, window):
        window.blit(self.image, self.position)


# Classe pour le jeu
class Game:
    def __init__(self):
        self.run = True
        self.towers = []
        self.placing_tower = False

        # Liste des armes disponibles
        self.available_weapons = [
            Weapon(TOWER_IMG, (100, 100)),
            Weapon(TOWER_IMG, (200, 200)),
            # Ajoutez plus d'armes disponibles avec leurs positions
        ]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if self.placing_tower:
                    self.towers.append(Weapon(TOWER_IMG, (x, y)))
                    self.placing_tower = False
                else:
                    # Vérifier si l'utilisateur a cliqué sur une arme disponible
                    for weapon in self.available_weapons:
                        weapon_pos = weapon.position
                        if x > weapon_pos[0] and x < weapon_pos[0] + TOWER_IMG.get_width() and \
                                y > weapon_pos[1] and y < weapon_pos[1] + TOWER_IMG.get_height():
                            self.placing_tower = True
                            break

    def draw(self):
        # Afficher les armes disponibles
        for weapon in self.available_weapons:
            weapon.draw(WINDOW)

        # Dessiner les tours placées
        for tower in self.towers:
            tower.draw(WINDOW)

        pygame.display.update()

    def run_game(self):
        clock = pygame.time.Clock()

        while self.run:
            clock.tick(FPS)
            self.handle_events()
            self.draw()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run_game()

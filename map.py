import pygame


class Map:
    def __init__(self):
        # Pour lancer notre application en boucle
        self.running = True
        self.rect = ""
        # titre de notre jeu
        pygame.display.set_caption("Tower Defense")
        # on recuperer notre matrix que l'on stocke sur un variable
        self.word = self.matrix()

        # Définir la taille de la matrice et des carrés

        self.matrix_width = len(self.word[0])
        self.matrix_height = len(self.word)
        # la taille de chaque cellule dans le fenetre en pixels

        self.square_size = 40

        # Définir la taille de la fenêtre en fonction de notre matrice

        self.window_width = self.matrix_width * self.square_size
        self.window_height = self.matrix_height * self.square_size
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        # charger un image de fond
        self.background = pygame.image.load("sable.jpg")
        self.background = pygame.transform.scale(self.background, (self.window_width, self.window_height))
        self.screen.blit(self.background, (0, 0))

    def dessiner(self):
        for i in range(self.matrix_height):
            # Boucler sur chaque colonne de la matric
            for j in range(self.matrix_width):
                # Déterminer la position de la cellule dans la grille
                x = j * self.square_size
                y = i * self.square_size
                # on recupere chaque valeur du matrice
                cell_value = self.word[i][j]
                if cell_value == 1:
                    # on charge notre image
                    image = pygame.image.load("Assets/Tiles/tileWood_bridge.png")
                    # redimensionner l'image pour qu'il prend la taille du cellule
                    image = pygame.transform.scale(image, (self.square_size, 40))
                    # on recupere un rectangle de l'image
                    rect = image.get_rect(center=(x + self.square_size / 2, y + self.square_size / 2))
                    self.screen.blit(image, rect)
                elif cell_value == 0:
                    # on charge notre image
                    image = pygame.image.load("Assets/Tiles/tileWood_bridge.png")
                    # redimensionner l'image pour qu'il prend la taille du cellule
                    image = pygame.transform.scale(image, (self.square_size, 40))
                    # on recupere un rectangle de l'image
                    rect = image.get_rect(center=(x + self.square_size / 2, y + self.square_size / 2))
                    self.screen.blit(image, rect)
                else:
                    # on charge notre image
                    image = pygame.image.load("Assets/Tiles/hillSand.png")
                    # redimensionner l'image pour qu'il prend la taille du cellule
                    image = pygame.transform.scale(image, (self.square_size, 110))
                    # on recupere un rectangle de l'image
                    rect = image.get_rect(center=(x + self.square_size / 2, y + self.square_size / 2))
                    self.background.blit(image, rect)

    def run(self):

        while self.running:
            self.dessiner()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()

        pygame.quit()

    def matrix(self):

        word = [
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        return word

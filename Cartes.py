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

    @classmethod
    def afficher_decor(cls, chemin, pixels, x, y, screen):
        image = pygame.image.load(chemin)
        # On redimensionne l'image pour qu'il prenne la taille de la cellule
        image = pygame.transform.scale(image, (pixels, 40))
        # on recupere un rectangle de l'image
        rect = image.get_rect(
            center=(x + pixels / 2, y + pixels / 2))
        screen.blit(image, rect)

    @classmethod
    def afficher_message_vague(cls, vague_actuelle, window_width, window_height, screen):
        font = pygame.font.SysFont(None, 48)
        message = f"Vague {vague_actuelle + 1} !"
        texte = font.render(message, True, (255, 255, 255))
        position = texte.get_rect(center=(window_width // 2, window_height // 2))
        screen.blit(texte, position)
        pygame.display.update()
        pygame.time.delay(3000)

    @classmethod
    def draw_map(cls, matrix_height, matrix_width, pixels, world, screen):

        for i in range(matrix_height):
            # Boucler sur chaque colonne de la matric
            for j in range(matrix_width):
                # Déterminer la position de la cellule dans la grille
                x = j * pixels
                y = i * pixels
                # on récupère chaque valeur de la matrice

                cellule = world[i][j]

                if cellule == 1:
                    Carte.afficher_decor("Assets/Armes/wals.png", pixels, x, y, screen)
                elif cellule == 0:

                    Carte.afficher_decor("Assets/sable.jpg", pixels, x, y, screen)

                elif cellule == 2:
                    # pygame.draw.rect(self.screen, (171, 178, 185), pygame.Rect(x, y, self.pixels, 40))
                    image = pygame.image.load("Assets/Armes/Image 89 at frame 1copy .jpg")
                    screen.blit(image, (681, 0))

import pygame
import math

from Sound import Sound
from button import Button


def matrix():
    word = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    return word


class Map:
    def __init__(self):
        # Pour lancer notre application en boucle
        self.running = True
        # titre de notre jeu
        pygame.display.set_caption("Tower Defense")
        # on recuperer notre matrix que l'on stocke sur un variable
        self.word = matrix()

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
        self.background = pygame.image.load("Assets/sable.jpg")
        self.background = pygame.transform.scale(self.background, (self.window_width, self.window_height))
        # definir l'image de font de notre Menu
        self.Fond_Menu = pygame.image.load("Assets/Background.png")
        # instanciation de mon menu
        self.mes_button = {
            "button_Menu": Button(420, 100, "Assets/Menu Buttons/Large Buttons/Colored Large Buttons/Menu  col_Button.png"),
            "button_NewGame": Button(420, 220, "Assets/Menu Buttons/Large Buttons/Colored Large Buttons/New Game  col_Button.png"),
            "button_Options": Button(420, 340, "Assets/Menu Buttons/Large Buttons/Colored Large Buttons/Options  col_Button.png"),
            "button_Quitt": Button(420, 460, "Assets/Menu Buttons/Large Buttons/Colored Large Buttons/Quit  col_Button.png")

        }
        # instancier musique
        self.sound = Sound("Musique/1.mp3")

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
                    image = pygame.image.load("Assets/gazon.jpg")
                    # redimensionner l'image pour qu'il prend la taille du cellule
                    image = pygame.transform.scale(image, (self.square_size, 40))
                    # on recupere un rectangle de l'image
                    rect = image.get_rect(center=(x + self.square_size / 2, y + self.square_size / 2))
                    self.screen.blit(image, rect)

    def run(self):
        while self.running:
            # On affiche notre Menu et on attend l'action de l'utilisateur pour faire des actions

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            if not self.mes_button["button_NewGame"].start:
                # on charge la musique
                self.sound.play_sound()
                # on charge notre menu
                self.screen.blit(self.Fond_Menu, (0, 0))
                # on charge le Menu
                self.screen.blit(self.mes_button["button_Menu"].image, self.mes_button["button_Menu"].rect)
                self.screen.blit(self.mes_button["button_NewGame"].image, self.mes_button["button_NewGame"].rect)
                self.screen.blit(self.mes_button["button_Options"].image, self.mes_button["button_Options"].rect)
                self.screen.blit(self.mes_button["button_Quitt"].image, self.mes_button["button_Quitt"].rect)

                for events in pygame.event.get():
                    if events.type == pygame.MOUSEBUTTONDOWN:
                        # on verifie si notre button est clique
                        if self.mes_button["button_NewGame"].is_clicked(pygame.mouse.get_pos()):
                            # on charge notre fond de jeux
                            self.screen.blit(self.background, (0, 0))
                            # on demare le jeux
                            self.dessiner()

                pygame.display.flip()

        pygame.quit()

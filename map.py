import pygame
import time

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

            "button_Menu": Button(420, 100,
                                  "Assets/Menu Buttons/Large Buttons/Colored Large Buttons/Menu  col_Button.png"),
            "button_NewGame": Button(420, 220,
                                     "Assets/Menu Buttons/Large Buttons/Colored Large Buttons/New Game  col_Button.png"),
            "button_Options": Button(420, 340,
                                     "Assets/Menu Buttons/Large Buttons/Colored Large Buttons/Options  col_Button.png"),
            "button_Quitt": Button(420, 460,
                                   "Assets/Menu Buttons/Large Buttons/Colored Large Buttons/Quit  col_Button.png"),
            "button_SousMenuMusique": Button(300, 100,
                                             "Assets/Menu Buttons/Square Buttons/Colored Square Buttons/Music col_Square Button.png"),
            "button_SousMenuStopMusique": Button(520, 100,
                                                 "Assets/Menu Buttons/Square Buttons/Colored Square Buttons/X col_Square Button.png"),
            "button_SousMenuAudio": Button(300, 250,
                                           "Assets/Menu Buttons/Square Buttons/Colored Square Buttons/Audio col_Square Button.png"),
            "button_SousMenuStopAudio": Button(520, 250,
                                               "Assets/Menu Buttons/Square Buttons/Colored Square Buttons/X col_Square Button.png"),
            "button_Retour": Button(420, 420,
                                    "Assets/Menu Buttons/Square Buttons/Colored Square Buttons/Back col_Square Button.png")

        }
        # instancier musique
        self.sound = Sound("Musique/1.mp3")
        self.img = pygame.image.load("Assets/gazon.jpg")
        self.etat = "menu"

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
            # Mais le jeu est demarer avec l'isntance Menu et le changements des etats va permettre d'afficher les autre fenetre
            if self.etat == "menu":
                # on charge notre menu
                self.screen.blit(self.Fond_Menu, (0, 0))
                # on charge le Menu
                self.screen.blit(self.mes_button["button_Menu"].image, self.mes_button["button_Menu"].rect)
                self.screen.blit(self.mes_button["button_NewGame"].image, self.mes_button["button_NewGame"].rect)
                self.screen.blit(self.mes_button["button_Options"].image, self.mes_button["button_Options"].rect)
                self.screen.blit(self.mes_button["button_Quitt"].image, self.mes_button["button_Quitt"].rect)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    # On ecoute les evenement du Menu
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.mes_button["button_NewGame"].is_clicked(pygame.mouse.get_pos()):
                            # si c'est le bouton New Game est clique on change l'etat du jeu pour quitter fenetre menu pour aller fenetre dujeux
                            self.etat = "jeu"
                        elif self.mes_button["button_Options"].is_clicked(pygame.mouse.get_pos()):
                            # si c'est le bouton options est clique on change l'etat du jeu pour quitter fenetre menu pour aller fenetre du options
                            self.etat = "options"
                        elif self.mes_button["button_Quitt"].is_clicked(pygame.mouse.get_pos()):
                            self.running = False
                pygame.display.flip()

            elif self.etat == "options":
                # On affiche le sous menu de Options
                self.screen.blit(self.Fond_Menu, (0, 0))
                self.screen.blit(self.mes_button["button_SousMenuMusique"].image,
                                 self.mes_button["button_SousMenuMusique"].rect)
                self.screen.blit(self.mes_button["button_SousMenuStopMusique"].image,
                                 self.mes_button["button_SousMenuStopMusique"].rect)
                self.screen.blit(self.mes_button["button_SousMenuAudio"].image,
                                 self.mes_button["button_SousMenuAudio"].rect)
                self.screen.blit(self.mes_button["button_SousMenuStopAudio"].image,
                                 self.mes_button["button_SousMenuStopAudio"].rect)
                self.screen.blit(self.mes_button["button_Retour"].image, self.mes_button["button_Retour"].rect)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.mes_button["button_Retour"].is_clicked(pygame.mouse.get_pos()):
                            self.etat = "menu"
                pygame.display.flip()

            elif self.etat == "jeu":
                # on charge la musique
                # self.sound.play_sound()
                # on charge notre fond de jeux
                self.screen.blit(self.background, (0, 0))
                # on demare le jeux
                self.dessiner()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                pygame.display.flip()

        pygame.quit()

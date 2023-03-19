import pygame
import time

from Sound import Sound
from button import Button
from Monstre import Monstre


def matrix():
    word = [

        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],

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

        self.pixels = 40

        # Définir la taille de la fenêtre en fonction de notre matrice

        self.window_width = self.matrix_width * self.pixels
        self.window_height = self.matrix_height * self.pixels
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
        self.etat_button_options = "normal"
        # instancier musique
        self.sound = Sound("Musique/1.mp3")
        self.etat = "menu"
        self.monstre = Monstre(84, -72)

    def dessiner_map_1(self):
        for i in range(self.matrix_height):
            # Boucler sur chaque colonne de la matric
            for j in range(self.matrix_width):
                # Déterminer la position de la cellule dans la grille
                x = j * self.pixels
                y = i * self.pixels
                # on recupere chaque valeur du matrice
                cellule = self.word[i][j]

                if cellule == 1:
                    # on charge  image
                    image = pygame.image.load("Assets/gazon.jpg")
                    #On redimensionner l'image pour qu'il prend la taille du cellule
                    image = pygame.transform.scale(image, (self.pixels, 40))
                    # on recupere un rectangle de l'image
                    rect = image.get_rect(center=(x + self.pixels / 2, y + self.pixels / 2))
                    self.screen.blit(image, rect)

                elif cellule == 0:
                    # on charge notre image
                    image = pygame.image.load("Assets/sable.jpg")
                    #On redimensionner l'image pour qu'il prend la taille du cellule
                    image = pygame.transform.scale(image, (self.pixels, 40))
                    # on recupere un rectangle de l'image
                    rect = image.get_rect(center=(x + self.pixels / 2, y + self.pixels / 2))
                    self.screen.blit(image, rect)
                    self.screen.blit(self.monstre.image_monstre, (
                        self.monstre.positionX + self.pixels, self.monstre.positionY + self.pixels))
                   

            pygame.display.flip()

    def MenuPrincipal(self):
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

    def option_play_Musique(self):
        # On remplace le bouton par un nouveau
        new_button = Button(520, 100,
                            "Assets/Menu Buttons/Square Buttons/Colored Square Buttons/Play col_Square Button.png")
        self.mes_button["button_SousMenuStopMusique"] = new_button
        self.screen.blit(self.mes_button["button_SousMenuStopMusique"].image,
                         self.mes_button["button_SousMenuStopMusique"].rect)
        self.sound.play_sound()

    def option_stop_Musique(self):
        # On remet le boutton initial
        new_button = Button(520, 100,
                            "Assets/Menu Buttons/Square Buttons/Colored Square Buttons/Pause col_Square Button.png")
        self.mes_button["button_SousMenuStopMusique"] = new_button
        self.screen.blit(self.mes_button["button_SousMenuStopMusique"].image,
                         self.mes_button["button_SousMenuStopMusique"].rect)
        self.sound.stop_sound()

    def option_play_audio(self):
        # On remplace le bouton par un nouveau
        new_button = Button(520, 250,
                            "Assets/Menu Buttons/Square Buttons/Colored Square Buttons/Play col_Square Button.png")
        self.mes_button["button_SousMenuStopAudio"] = new_button
        self.screen.blit(self.mes_button["button_SousMenuStopAudio"].image,
                         self.mes_button["button_SousMenuStopAudio"].rect)

    def option_stop_audio(self):
        # On remet le boutton initial
        new_button = Button(520, 250,
                            "Assets/Menu Buttons/Square Buttons/Colored Square Buttons/Pause col_Square Button.png")
        self.mes_button["button_SousMenuStopAudio"] = new_button
        self.screen.blit(self.mes_button["button_SousMenuStopAudio"].image,
                         self.mes_button["button_SousMenuStopAudio"].rect)
        self.sound.stop_sound()

    def draw_monstre(self):
        while self.monstre.positionY != 126:
            clock = pygame.time.Clock()
            self.monstre.positionY += self.monstre.vitesse
            self.screen.blit(self.monstre.image_monstre, (
                self.monstre.positionX + self.pixels, self.monstre.positionY + self.pixels))
            pygame.display.update()
            pygame.time.delay(self.monstre.attente)
            clock.tick(60) 

        self.screen.blit(self.monstre.image_monstre, (
            self.monstre.positionX + self.pixels, self.monstre.positionY + self.pixels))



    def MenuOptions(self):
        #   On affiche les Boutons du Sous Menu Options
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
        # On ecoute les evenements sur les Bouttons qu'on attribuer des etats et chaque etats correspond a un un fenetre ou un action
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.mes_button["button_Retour"].is_clicked(pygame.mouse.get_pos()):
                    self.etat = "menu"

                elif self.mes_button["button_SousMenuMusique"].is_clicked(pygame.mouse.get_pos()):
                    # On definie aussi des etats au niveaux des bouttons du Sous Menu Option
                    self.etat_button_options = "musique"

                    if self.etat_button_options == "musique":
                        self.option_play_Musique()

                elif self.mes_button["button_SousMenuStopMusique"].is_clicked(pygame.mouse.get_pos()):

                    if self.etat_button_options == "musique":
                        self.etat_button_options = "stop_musique"

                    if self.etat_button_options == "stop_musique":
                        self.option_stop_Musique()

                elif self.mes_button["button_SousMenuAudio"].is_clicked(pygame.mouse.get_pos()):
                    self.etat_button_options = "audio"

                    if self.etat_button_options == "audio":
                        self.option_play_audio()

                elif self.mes_button["button_SousMenuStopAudio"].is_clicked(pygame.mouse.get_pos()):
                    if self.etat_button_options == "audio":
                        self.etat_button_options = "stop_audio"

                    if self.etat_button_options == "stop_audio":
                        self.option_stop_audio()

        pygame.display.flip()

    def run(self):
        while self.running:
            # On affiche notre Menu et on attend l'action de l'utilisateur pour faire des actions
            # Mais le jeu est demarer avec l'isntance Menu et le changements des etats va permettre d'afficher les autre fenetre
            if self.etat == "menu":
                # on charge notre menu
                self.MenuPrincipal()

            elif self.etat == "options":
                # On affiche le sous menu de Options
                self.MenuOptions()

            elif self.etat == "jeu":
                # on lance notre jeux
                # self.monstre.move()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False

                self.dessiner_map_1()
                self.draw_monstre()

        pygame.quit()

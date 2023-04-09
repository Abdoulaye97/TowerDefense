import pygame
import time

from Sound import Sound
from button import Button
from Monstre import Monstre
from Vie import Vie
from Armes import Arme
from Cartes import Carte
from AfficheurTexte import AfficheurTexte

# def matrix():
word = [

    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],

]

word_2 = [

    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],

]

word_3 = [

    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],

]


class Map:
    def __init__(self):
        # Pour lancer notre application en boucle
        self.running = True
        # titre de notre jeu
        pygame.display.set_caption("Tower Defense")
        # on récupère notre matrix que l'on stocke sur un variable
        self.word = word

        # Définir la taille de la matrice et des carrés
        self.matrix_width = len(self.word[0])
        self.matrix_height = len(self.word)
        # la taille de chaque cellule dans le fenetre qu'on met  en pixels

        self.pixels = 40

        # Définir la taille de la fenêtre en fonction de notre matrice

        self.window_width = self.matrix_width * self.pixels
        self.window_height = self.matrix_height * self.pixels
        self.screen = pygame.display.set_mode(
            (self.window_width, self.window_height))
        # charger un image de fond
        self.background = pygame.image.load("Assets/sable.jpg")
        self.background = pygame.transform.scale(
            self.background, (self.window_width, self.window_height))
        # definir l'image de faire de notre Menu
        self.Fond_Menu = pygame.image.load("Assets/Background.png")
        self.Fond_Map = pygame.image.load("map_1.png")
        # instanciation de mon menu
        self.mes_button = {

            "button_Menu": Button(500, 100,

                                  "Assets/Menu Buttons/Large Buttons/Colored Large Buttons/Menu  col_Button.png"),
            "button_NewGame": Button(500, 220,
                                     "Assets/Menu Buttons/Large Buttons/Colored Large Buttons/New Game  col_Button.png"),
            "button_Options": Button(500, 340,
                                     "Assets/Menu Buttons/Large Buttons/Colored Large Buttons/Options  col_Button.png"),
            "button_Quitt": Button(500, 460,
                                   "Assets/Menu Buttons/Large Buttons/Colored Large Buttons/Quit  col_Button.png"),
            "button_SousMenuMusique": Button(400, 100,
                                             "Assets/Menu Buttons/Square Buttons/Colored Square Buttons/Music col_Square Button.png"),
            "button_SousMenuStopMusique": Button(620, 100,
                                                 "Assets/Menu Buttons/Square Buttons/Colored Square Buttons/X col_Square Button.png"),
            "button_SousMenuAudio": Button(400, 250,
                                           "Assets/Menu Buttons/Square Buttons/Colored Square Buttons/Audio col_Square Button.png"),
            "button_SousMenuStopAudio": Button(620, 250,
                                               "Assets/Menu Buttons/Square Buttons/Colored Square Buttons/X col_Square Button.png"),
            "button_Retour": Button(520, 420,
                                    "Assets/Menu Buttons/Square Buttons/Colored Square Buttons/Back col_Square Button.png")
        }
        self.cartes = {
            "carte_1": Carte(170, 250, "map_1.png"),
            "carte_2": Carte(480, 250, "map_2.png"),
            "carte_3": Carte(790, 250, "map_1.png")
        }
        self.text = {
            "text_easy": AfficheurTexte("Aesy", 150, 360, (128, 128, 128)),
            "text_medium": AfficheurTexte("Medium", 430, 360, (128, 128, 128)),
            "text.difficile": AfficheurTexte("Hight", 750, 360, (128, 128, 128)),
            "game_over": AfficheurTexte("Game Over", 400, 400, (199, 0, 57))
        }
        self.etat_button_options = "normal"
        self.etat = "menu"
        # instancier musique
        self.sound = Sound("Musique/1.mp3")
        self.vie_joueur = Vie()
        self.armes = {
            "arme_1": Arme(655, -10, "Assets/Armes/armes.png", "arme_1")
        }
        self.vagues_de_monstres = [
            [Monstre(84, 480), Monstre(84, 552)],
            [Monstre(84, 480), Monstre(84, 552)],
            [Monstre(84, 480), Monstre(84, 552)]
        ]
        self.monstre = Monstre(84, 480)
        self.monstres_vague_actuelle = 0
        self.vague_actuelle = 0
        self.position_prochaine_vague = 165
        self.vague_affichee = False
        # self.monstres.append(Monstre(84, 480))
        # self.monstres.append(Monstre(84, 552))

    def dessiner_map_1(self):

        for i in range(self.matrix_height):
            # Boucler sur chaque colonne de la matric
            for j in range(self.matrix_width):
                # Déterminer la position de la cellule dans la grille
                x = j * self.pixels
                y = i * self.pixels
                # on récupère chaque valeur de la matrice
                cellule = self.word[i][j]

                if cellule == 1:
                    # on charge  image
                    image = pygame.image.load("Assets/Armes/wals.png")
                    # On redimensionne l'image pour qu'il prenne la taille de la cellule
                    image = pygame.transform.scale(image, (self.pixels, 40))
                    # on recupere un rectangle de l'image
                    rect = image.get_rect(
                        center=(x + self.pixels / 2, y + self.pixels / 2))
                    self.screen.blit(image, rect)

                elif cellule == 0:
                    # on charge notre image
                    image = pygame.image.load("Assets/sable.jpg")
                    # On redimensionne l'image pour qu'il prenne la taille de la cellule
                    image = pygame.transform.scale(image, (self.pixels, 40))
                    # on recupere un rectangle de l'image
                    rect = image.get_rect(
                        center=(x + self.pixels / 2, y + self.pixels / 2))
                    self.screen.blit(image, rect)

                elif cellule == 2:
                    pygame.draw.rect(self.screen, (171, 178, 185), pygame.Rect(x, y, self.pixels, 40))
                # image = pygame.transform.scale(image,(self.pixels, 40))
                # rect = image.get_rect(
                #   center=(x + self.pixels / 2, y + self.pixels / 2))
                # self.screen.blit(image, rect)

        pygame.display.flip()

    def dessiner_map_2(self):

        for i in range(self.matrix_height):
            # Boucler sur chaque colonne de la matric
            for j in range(self.matrix_width):
                # Déterminer la position de la cellule dans la grille
                x = j * self.pixels
                y = i * self.pixels
                # on récupère chaque valeur de la matrice
                cellule = word_2[i][j]

                if cellule == 1:
                    # on charge  image
                    image = pygame.image.load("Assets/Armes/wals.png")
                    # On redimensionne l'image pour qu'il prenne la taille de la cellule
                    image = pygame.transform.scale(image, (self.pixels, 40))
                    # on recupere un rectangle de l'image
                    rect = image.get_rect(
                        center=(x + self.pixels / 2, y + self.pixels / 2))
                    self.screen.blit(image, rect)

                elif cellule == 0:
                    # on charge notre image
                    image = pygame.image.load("Assets/sable.jpg")
                    # On redimensionne l'image pour qu'il prenne la taille de la cellule
                    image = pygame.transform.scale(image, (self.pixels, 40))
                    # on recupere un rectangle de l'image
                    rect = image.get_rect(
                        center=(x + self.pixels / 2, y + self.pixels / 2))
                    self.screen.blit(image, rect)

                elif cellule == 2:
                    pygame.draw.rect(self.screen, (171, 178, 185), pygame.Rect(x, y, self.pixels, 40))
                    # image = pygame.transform.scale(image,(self.pixels, 40))
                    # rect = image.get_rect(
                    #   center=(x + self.pixels / 2, y + self.pixels / 2))
                    # self.screen.blit(image, rect)

    def dessiner_map_3(self):

        for i in range(self.matrix_height):
            # Boucler sur chaque colonne de la matric
            for j in range(self.matrix_width):
                # Déterminer la position de la cellule dans la grille
                x = j * self.pixels
                y = i * self.pixels
                # on récupère chaque valeur de la matrice
                cellule = word_3[i][j]

                if cellule == 1:
                    # on charge  image
                    image = pygame.image.load("Assets/Armes/wals.png")
                    # On redimensionne l'image pour qu'il prenne la taille de la cellule
                    image = pygame.transform.scale(image, (self.pixels, 40))
                    # on recupere un rectangle de l'image
                    rect = image.get_rect(
                        center=(x + self.pixels / 2, y + self.pixels / 2))
                    self.screen.blit(image, rect)

                elif cellule == 0:
                    # on charge notre image
                    image = pygame.image.load("Assets/sable.jpg")
                    # On redimensionne l'image pour qu'il prenne la taille de la cellule
                    image = pygame.transform.scale(image, (self.pixels, 40))
                    # on recupere un rectangle de l'image
                    rect = image.get_rect(
                        center=(x + self.pixels / 2, y + self.pixels / 2))
                    self.screen.blit(image, rect)

                elif cellule == 2:
                    pygame.draw.rect(self.screen, (171, 178, 185), pygame.Rect(x, y, self.pixels, 40))
                    # image = pygame.transform.scale(image,(self.pixels, 40))
                    # rect = image.get_rect(
                    #   center=(x + self.pixels / 2, y + self.pixels / 2))
                    # self.screen.blit(image, rect)

        pygame.display.flip()

    def MenuPrincipal(self):
        self.screen.blit(self.Fond_Menu, (0, 0))
        # on charge le Menu
        self.screen.blit(
            self.mes_button["button_Menu"].image, self.mes_button["button_Menu"].rect)
        self.screen.blit(
            self.mes_button["button_NewGame"].image, self.mes_button["button_NewGame"].rect)
        self.screen.blit(
            self.mes_button["button_Options"].image, self.mes_button["button_Options"].rect)
        self.screen.blit(
            self.mes_button["button_Quitt"].image, self.mes_button["button_Quitt"].rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # On écoute les evenement du Menu
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.mes_button["button_NewGame"].is_clicked(pygame.mouse.get_pos()):
                    # si c'est le bouton New Game est (clique) on change l'etat du jeu pour quitter fenetre menu pour aller fenetre dujeux

                    self.etat = "map"
                elif self.mes_button["button_Options"].is_clicked(pygame.mouse.get_pos()):
                    # si c'est le bouton options est (clique) on change l'etat du jeu pour quitter fenetre menu pour aller fenetre des options
                    self.etat = "options"
                elif self.mes_button["button_Quitt"].is_clicked(pygame.mouse.get_pos()):
                    self.running = False
        pygame.display.flip()

    def MenuMap(self):
        # On charge notre fond d'ecran
        self.screen.blit(self.Fond_Menu, (0, 0))
        # On affiche le premier map pour permettre au joueur de choisir
        self.screen.blit(self.cartes["carte_1"].image, self.cartes["carte_1"].rect)
        # On lui indique le niveau de diffultite du map
        self.text["text_easy"].afficher_texte(self.screen)
        # On affiche la deuxime map
        self.screen.blit(self.cartes["carte_2"].image, self.cartes["carte_2"].rect)
        # On lui indique le niveau de diffultite du map
        self.text["text_medium"].afficher_texte(self.screen)
        # On affiche la troisime map
        self.screen.blit(self.cartes["carte_3"].image, self.cartes["carte_3"].rect)
        # On lui indique le niveau de diffultite du map
        self.text["text.difficile"].afficher_texte(self.screen)

        # On parcourt les evenements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Si l'utilisateur clique sur le premiere map
                if self.cartes["carte_1"].is_clicked_map(pygame.mouse.get_pos()):
                    # On change l'etat du jeu qui va charger le map choisie
                    self.etat = "jeu_map1"
                # Si l'utilisateur clique sur le deuxime map
                elif self.cartes["carte_2"].is_clicked_map(pygame.mouse.get_pos()):
                    # On change l'etat du jeu qui va charger le map choisie
                    self.etat = "jeu_map2"
                # Si l'utilisateur clique sur le troisime map
                elif self.cartes["carte_3"].is_clicked_map(pygame.mouse.get_pos()):
                    # On change l'etat du jeu qui charger le map choisie
                    self.etat = "jeu_map3"

        pygame.display.flip()

    def option_play_Musique(self):
        # On remplace le bouton par un nouveau
        new_button = Button(620, 100,
                            "Assets/Menu Buttons/Square Buttons/Colored Square Buttons/Play col_Square Button.png")
        self.mes_button["button_SousMenuStopMusique"] = new_button
        self.screen.blit(self.mes_button["button_SousMenuStopMusique"].image,
                         self.mes_button["button_SousMenuStopMusique"].rect)
        self.sound.play_sound()

    def option_stop_Musique(self):
        # On remet le boutton initial
        new_button = Button(620, 100,
                            "Assets/Menu Buttons/Square Buttons/Colored Square Buttons/Pause col_Square Button.png")
        self.mes_button["button_SousMenuStopMusique"] = new_button
        self.screen.blit(self.mes_button["button_SousMenuStopMusique"].image,
                         self.mes_button["button_SousMenuStopMusique"].rect)
        self.sound.stop_sound()

    def option_play_audio(self):
        # On remplace le bouton par un nouveau
        new_button = Button(620, 250,
                            "Assets/Menu Buttons/Square Buttons/Colored Square Buttons/Play col_Square Button.png")
        self.mes_button["button_SousMenuStopAudio"] = new_button
        self.screen.blit(self.mes_button["button_SousMenuStopAudio"].image,
                         self.mes_button["button_SousMenuStopAudio"].rect)

    def option_stop_audio(self):
        # On remet le boutton initial
        new_button = Button(620, 250,
                            "Assets/Menu Buttons/Square Buttons/Colored Square Buttons/Pause col_Square Button.png")
        self.mes_button["button_SousMenuStopAudio"] = new_button
        self.screen.blit(self.mes_button["button_SousMenuStopAudio"].image,
                         self.mes_button["button_SousMenuStopAudio"].rect)
        self.sound.stop_sound()

    def MenuOptions(self):
        #   On affiche les Boutons du Sous Menues Options
        self.screen.blit(self.Fond_Menu, (0, 0))
        self.screen.blit(self.mes_button["button_SousMenuMusique"].image,
                         self.mes_button["button_SousMenuMusique"].rect)
        self.screen.blit(self.mes_button["button_SousMenuStopMusique"].image,
                         self.mes_button["button_SousMenuStopMusique"].rect)
        self.screen.blit(self.mes_button["button_SousMenuAudio"].image,
                         self.mes_button["button_SousMenuAudio"].rect)
        self.screen.blit(self.mes_button["button_SousMenuStopAudio"].image,
                         self.mes_button["button_SousMenuStopAudio"].rect)
        self.screen.blit(
            self.mes_button["button_Retour"].image, self.mes_button["button_Retour"].rect)
        # On écoute les evenements sur les Bouttons qu'on attribue des etats et chaque etats correspond à un fenetre ou une action.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.mes_button["button_Retour"].is_clicked(pygame.mouse.get_pos()):
                    self.etat = "menu"

                elif self.mes_button["button_SousMenuMusique"].is_clicked(pygame.mouse.get_pos()):
                    # On définit aussi des etats aux niveaux des bouttons du Sous Menue Option
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

    def afficher_message_vague(self):
        font = pygame.font.SysFont(None, 48)
        message = f"Vague {self.vague_actuelle + 1} !"
        texte = font.render(message, True, (255, 255, 255))
        position = texte.get_rect(center=(self.window_width // 2, self.window_height // 2))
        self.screen.blit(texte, position)
        pygame.display.update()
        pygame.time.delay(3000)

    def verifier_degats_monstre(self, posX, posY, degat, screen):
        if posX == 165 and posY == -69:
            self.vie_joueur.degat(degat, screen)
        pygame.display.flip()

    def run(self):

        while self.running:
            # On affiche notre Menu et on attend l'action de l'utilisateur pour faire des actions
            # Mais le jeu est demarer avec l'isntance Menu et les changements des etats va permettre d'afficher l'autre fenetre.
            if self.etat == "menu":
                # on charge notre menu
                self.MenuPrincipal()

            elif self.etat == "map":
                self.MenuMap()

            elif self.etat == "options":
                # On affiche le sous menu d'options
                self.MenuOptions()
            # Map 1
            elif self.etat == "jeu_map1":

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False

                self.dessiner_map_1()

                # Vérifier si tous les monstres ont atteint la position de déclenchement de la prochaine vague
                declancher_prochaine_vague = all(
                    monstre.positionX == self.position_prochaine_vague and monstre.positionY == -78 for monstre in
                    self.vagues_de_monstres[self.vague_actuelle])
                if declancher_prochaine_vague:
                    self.vague_actuelle += 1
                    self.afficher_message_vague()

                # Afficher les monstres de la vague actuelle
                for monstre in self.vagues_de_monstres[self.vague_actuelle]:
                    if self.vie_joueur.vie_joueur > 0:
                        monstre.draw_monstre_map_1(self.screen, self.pixels)
                        monstre.update_bar_de_vie(self.screen)

                    if monstre.positionX == 165 and monstre.positionY == -69:
                        self.vie_joueur.degat(monstre.degat, self.screen)

                    if self.vie_joueur.vie_joueur == 0:
                        self.text["game_over"].afficher_texte(self.screen)

                self.vie_joueur.afficher_vie_joueur(self.screen)

                pygame.display.update()

            # Map 2
            elif self.etat == "jeu_map2":

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False

                self.dessiner_map_2()

                # Vérifier si tous les monstres ont atteint la position de déclenchement de la prochaine vague
                declancher_prochaine_vague = all(
                    monstre.positionX == 444 and monstre.positionY == -78 for monstre in
                    self.vagues_de_monstres[self.vague_actuelle])
                if declancher_prochaine_vague:
                    self.vague_actuelle += 1
                    self.afficher_message_vague()

                # Afficher les monstres de la vague actuelle
                for monstre in self.vagues_de_monstres[self.vague_actuelle]:
                    if self.vie_joueur.vie_joueur > 0:
                        monstre.draw_monstre_map_2(self.screen, self.pixels)
                        monstre.update_bar_de_vie(self.screen)

                    if monstre.positionX == 444 and monstre.positionY == -69:
                        self.vie_joueur.degat(monstre.degat, self.screen)

                    if self.vie_joueur.vie_joueur == 0:
                        self.text["game_over"].afficher_texte(self.screen)

                self.vie_joueur.afficher_vie_joueur(self.screen)

                pygame.display.update()


            # Map 3
            elif self.etat == "jeu_map3":

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                self.dessiner_map_3()
                # Vérifier si tous les monstres ont atteint la position de déclenchement de la prochaine vague
                declancher_prochaine_vague = all(
                    monstre.positionX == 84 and monstre.positionY == 327 for monstre in
                    self.vagues_de_monstres[self.vague_actuelle])
                if declancher_prochaine_vague:
                    self.vague_actuelle += 1
                    self.afficher_message_vague()

                # Afficher les monstres de la vague actuelle
                for monstre in self.vagues_de_monstres[self.vague_actuelle]:
                    if self.vie_joueur.vie_joueur > 0:
                        monstre.draw_monstre_map_3(self.screen, self.pixels)
                        monstre.update_bar_de_vie(self.screen)

                    if monstre.positionX == 84 and monstre.positionY == 321:
                        self.vie_joueur.degat(monstre.degat, self.screen)

                    if self.vie_joueur.vie_joueur == 0:
                        self.text["game_over"].afficher_texte(self.screen)

                self.vie_joueur.afficher_vie_joueur(self.screen)

                pygame.display.update()

            pygame.display.flip()

        pygame.quit()

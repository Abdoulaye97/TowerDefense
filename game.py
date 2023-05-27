import pygame
import time

from MenuMap import MenuGame
from Sound import Sound
from button import Button
from Monstre import Monstre
from Vie import Vie
from Armes import Arme
from Cartes import Carte
from AfficheurTexte import AfficheurTexte
from word import *


class Map:
    def __init__(self):
        # Pour lancer notre application en boucle
        self.selected_tower = None
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
        self.Fond_Map = pygame.image.load("Assets/Cartes/map_1.png")
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
            "carte_1": Carte(170, 250, "Assets/Cartes/map_1.png"),
            "carte_2": Carte(480, 250, "Assets/Cartes/map_2.png"),
            "carte_3": Carte(790, 250, "Assets/Cartes/map_3.png")
        }
        self.text = {
            "text_easy": AfficheurTexte("Facile", 150, 360, (128, 128, 128)),
            "text_medium": AfficheurTexte("Moyen", 430, 360, (128, 128, 128)),
            "text.difficile": AfficheurTexte("Difficile", 750, 360, (128, 128, 128)),
            "game_over": AfficheurTexte("Game Over", 400, 400, (199, 0, 57))
        }
        self.etat_button_options = "normal"
        self.etat = "menu"
        # instancier musique
        self.sound = Sound("Musique/1.mp3")
        self.vie_joueur = Vie()
        # self.armes = {
        #    "arme_1": Arme(715, 40, "Assets/Armes/arme.png", "arme_1")
        # }
        self.mes_armes = [
            Arme(715, 40, "Assets/Armes/arme.png", "arme_1"),
            Arme(820, 40, "Assets/Armes/Basic2 howitzer moving_waifu2x_photo_noise3_scale.png", "arme_2")
            # Ajoutez plus d'armes disponibles avec leurs positions
        ]
        self.vagues_de_monstres = [
            [Monstre(84, 480), Monstre(84, 552)],
            [Monstre(84, 480), Monstre(84, 552), Monstre(84, 624)]
        ]
        # self.monstre = Monstre(84, 480)
        self.monstres_vague_actuelle = 0
        self.vague_actuelle = 0
        self.position_prochaine_vague = 165
        self.vague_affichee = False
        self.menu_map_screen = MenuGame(self)
        self.click = ""
        self.towers = []
        self.placing_tower = False
        self.selected_weapon = None
        self.argent = 200

    def draw_map(self, world):

        for i in range(self.matrix_height):
            # Boucler sur chaque colonne de la matric
            for j in range(self.matrix_width):
                # Déterminer la position de la cellule dans la grille
                x = j * self.pixels
                y = i * self.pixels
                # on récupère chaque valeur de la matrice

                cellule = world[i][j]

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

    def afficher_message_vague(self):
        font = pygame.font.SysFont(None, 48)
        message = f"Vague {self.vague_actuelle + 1} !"
        texte = font.render(message, True, (255, 255, 255))
        position = texte.get_rect(center=(self.window_width // 2, self.window_height // 2))
        self.screen.blit(texte, position)
        pygame.display.update()
        pygame.time.delay(3000)

    def draw(self):
        # Afficher les armes disponibles
        for armes in self.mes_armes:
            armes.draw_armes(self.screen)

        # Dessiner les tours placées
        for tower in self.towers:
            tower.draw_armes(self.screen)

        # pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if self.placing_tower:
                    if len(self.mes_armes) < 5 :
                        self.towers.append(Arme(x, y, "Assets/Armes/arme.png", "arme_3"))
                        # Ajouter la dernière arme ajoutée à mes_armes
                        self.mes_armes.append(self.towers[-1])
                        self.towers[-1].resize_image((50, 50))
                        self.towers[-1].acheter(self)
                        self.placing_tower = False

                else:
                    for arme in self.mes_armes:
                        # Vérifier les conditions de clic sur l'arme
                        if arme.is_clicked_armes((x, y)):
                            arme.cliquer(self)
                            self.placing_tower = True
                            break

    def run(self):

        while self.running:
            # On affiche notre Menu et on attend l'action de l'utilisateur pour faire des actions
            # Mais le jeu est demarer avec l'isntance Menu et les changements des etats va permettre d'afficher l'autre fenetre.
            if self.etat == "menu":
                # on charge notre menu
                self.screen.blit(self.Fond_Menu, (0, 0))
                Button.MenuPrincipal(self.mes_button, self.screen, self)

            elif self.etat == "map":
                # self.MenuMap()
                self.menu_map_screen.MenuMap()

            elif self.etat == "options":
                # On affiche le sous menu d'options
                self.screen.blit(self.Fond_Menu, (0, 0))
                Button.MenuOptions(self.mes_button, self.screen, self, self.sound)

            # Map 1
            elif self.etat == "jeu_map1":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False

                self.draw_map(word)
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

                self.handle_events()
                self.draw()
                self.vie_joueur.afficher_vie_joueur(self.screen)
                pygame.display.update()


            # Map 2
            elif self.etat == "jeu_map2":

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False

                self.draw_map(word_2)
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
                        position = (monstre.positionX, monstre.positionY)
                        Arme.detecter_montres(self.mes_armes, position)
                        monstre.update_bar_de_vie(self.screen)

                    if monstre.positionX == 444 and monstre.positionY == -69:
                        self.vie_joueur.degat(monstre.degat, self.screen)

                self.handle_events()
                self.draw()
                self.vie_joueur.afficher_vie_joueur(self.screen)


                pygame.display.update()


            # Map 3
            elif self.etat == "jeu_map3":

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                self.draw_map(word_3)

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
                        monstre.draw_monstre_map_3(self.screen, self.pixels)
                        monstre.update_bar_de_vie(self.screen)

                    if monstre.positionX == 165 and monstre.positionY == -69:
                        self.vie_joueur.degat(monstre.degat, self.screen)

                self.handle_events()
                self.draw()
                self.vie_joueur.afficher_vie_joueur(self.screen)

                pygame.display.update()

        pygame.display.flip()

        pygame.quit()

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
        self.running = True
        pygame.display.set_caption("Tower Defense")
        self.word = word
        self.matrix_width = len(self.word[0])
        self.matrix_height = len(self.word)
        self.pixels = 40
        self.window_width = self.matrix_width * self.pixels
        self.window_height = self.matrix_height * self.pixels
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.background = pygame.image.load("Assets/sable.jpg")
        self.background = pygame.transform.scale(self.background, (self.window_width, self.window_height))
        self.Fond_Menu = pygame.image.load("Assets/BackTest.png")
        self.Fond_Map = pygame.image.load("Assets/Cartes/map_1.png")

        self.mes_button = {
            "button_Menu": Button(500, 100,"Assets/logo2-removebg-preview.png"),
            "button_NewGame": Button(380, 270,"Assets/Buttons/New_Game.png"),
            "button_Options": Button(620, 270,"Assets/Buttons/Options.png"),
            "button_Quitt": Button(500, 400,"Assets/Buttons/Quit.png"),
            "button_SousMenuMusique": Button(400, 100,"Assets/Buttons/Music_note_icon.png"),
            "button_SousMenuStopMusique": Button(620, 100,"Assets/Buttons/Decline.png"),
            "button_SousMenuAudio": Button(400, 250,"Assets/Buttons/Music_note_icon.png"),
            "button_SousMenuStopAudio": Button(620, 250,"Assets/Buttons/Decline.png"),
            "button_Retour": Button(520, 420,"Assets/Buttons/Back.png")
        }

        self.cartes = {
            "carte_1": Carte(170, 270, "Assets/Cartes/map_1.png"),
            "carte_2": Carte(480, 270, "Assets/Cartes/map_2.png"),
            "carte_3": Carte(790, 270, "Assets/Cartes/map_3.png")
        }

        self.text = {
            "text_easy": AfficheurTexte("Facile", 150, 140, (123,104,238)),
            "text_medium": AfficheurTexte("Moyen", 430, 140, (123,104,238)),
            "text.difficile": AfficheurTexte("Difficile", 750, 140, (123,104,238)),
            "game_over": AfficheurTexte("Game Over", 400, 400, (199, 0, 57))
        }

        self.etat_button_options = "normal"
        self.etat = "menu"
        self.sound = Sound("Musique/1.mp3")
        self.vie_joueur = Vie()
        self.armes = {"arme_1": Arme(655, -10, "Assets/Armes/armes.png", "arme_1")}

        self.vagues_de_monstres = [
            [Monstre(84, 480), Monstre(84, 552)],
            [Monstre(84, 480), Monstre(84, 552), Monstre(84, 624)]
        ]

        self.monstres_vague_actuelle = 0
        self.vague_actuelle = 0
        self.position_prochaine_vague = 165
        self.vague_affichee = False
        self.menu_map_screen = MenuGame(self)

    def draw_map(self, world):

        for i in range(self.matrix_height):
            for j in range(self.matrix_width):
                x = j * self.pixels
                y = i * self.pixels

                cellule = world[i][j]

                if cellule == 1:
                    image = pygame.image.load("Assets/Armes/wals.png")
                    image = pygame.transform.scale(image, (self.pixels, 40))
                    rect = image.get_rect(center=(x + self.pixels / 2, y + self.pixels / 2))
                    self.screen.blit(image, rect)

                elif cellule == 0:
                    image = pygame.image.load("Assets/sable.jpg")
                    image = pygame.transform.scale(image, (self.pixels, 40))
                    rect = image.get_rect(center=(x + self.pixels / 2, y + self.pixels / 2))
                    self.screen.blit(image, rect)

                elif cellule == 2:
                    pygame.draw.rect(self.screen, (171, 178, 185), pygame.Rect(x, y, self.pixels, 40))

                elif cellule == 3:
                    image = pygame.image.load("Assets/Armes/wals.png")
                    image = pygame.transform.scale(image, (self.pixels, 40))
                    rect = image.get_rect(center=(x + self.pixels / 2, y + self.pixels / 2))
                    self.screen.blit(image, rect)
                    image = pygame.image.load("Assets/Armes/armes-removebg-preview.png")
                    image = pygame.transform.scale(image, (self.pixels, 40))
                    rect = image.get_rect(center=(x + self.pixels / 2, y + self.pixels / 2))
                    self.screen.blit(image, rect)

                elif cellule == 4:
                    image = pygame.image.load("Assets/Armes/wals.png")
                    image = pygame.transform.scale(image, (self.pixels, 40))
                    rect = image.get_rect(center=(x + self.pixels / 2, y + self.pixels / 2))
                    self.screen.blit(image, rect)
                    image = pygame.image.load("Assets/Armes/Building5 laboratory.png")
                    image = pygame.transform.scale(image, (self.pixels, 40))
                    rect = image.get_rect(center=(x + self.pixels / 2, y + self.pixels / 2))
                    self.screen.blit(image, rect)

        pygame.display.flip()

    def afficher_message_vague(self):
        font = pygame.font.SysFont(None, 48)
        message = f"Vague {self.vague_actuelle + 1} !"
        texte = font.render(message, True, (255, 255, 255))
        position = texte.get_rect(center=(self.window_width // 2, self.window_height // 2))
        self.screen.blit(texte, position)
        pygame.display.update()
        pygame.time.delay(3000)

    def jeux_1(self, monde):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        self.draw_map(monde)
        declancher_prochaine_vague = all(monstre.positionX == self.position_prochaine_vague and monstre.positionY == -78 for monstre in self.vagues_de_monstres[self.vague_actuelle])
        
        if declancher_prochaine_vague:
            self.vague_actuelle += 1
            self.afficher_message_vague()

        for monstre in self.vagues_de_monstres[self.vague_actuelle]:
            if self.vie_joueur.vie_joueur > 0:
                monstre.draw_monstre_map_1(self.screen, self.pixels)
                monstre.update_bar_de_vie(self.screen)

            if monstre.positionX == 165 and monstre.positionY == -69:
                self.vie_joueur.degat(monstre.degat, self.screen)

        self.vie_joueur.afficher_vie_joueur(self.screen)
        pygame.display.update()

    def jeux_2(self, monde):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        self.draw_map(word_2)
        declancher_prochaine_vague = all(monstre.positionX == 444 and monstre.positionY == -78 for monstre in self.vagues_de_monstres[self.vague_actuelle])
        
        if declancher_prochaine_vague:
            self.vague_actuelle += 1
            self.afficher_message_vague()

        for monstre in self.vagues_de_monstres[self.vague_actuelle]:
            if self.vie_joueur.vie_joueur > 0:
                monstre.draw_monstre_map_2(self.screen, self.pixels)
                monstre.update_bar_de_vie(self.screen)

            if monstre.positionX == 444 and monstre.positionY == -69:
                self.vie_joueur.degat(monstre.degat, self.screen)

        self.vie_joueur.afficher_vie_joueur(self.screen)
        pygame.display.update()

    def jeux_3(self, monde):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        self.draw_map(word_3)
        declancher_prochaine_vague = all(monstre.positionX == self.position_prochaine_vague and monstre.positionY == -78 for monstre in self.vagues_de_monstres[self.vague_actuelle])
        if declancher_prochaine_vague:
            self.vague_actuelle += 1
            self.afficher_message_vague()

        for monstre in self.vagues_de_monstres[self.vague_actuelle]:
            if self.vie_joueur.vie_joueur > 0:
                monstre.draw_monstre_map_3(self.screen, self.pixels)
                monstre.update_bar_de_vie(self.screen)

            if monstre.positionX == 165 and monstre.positionY == -69:
                self.vie_joueur.degat(monstre.degat, self.screen)

        self.vie_joueur.afficher_vie_joueur(self.screen)

        pygame.display.update()


    def run(self):

        while self.running:
            if self.etat == "menu":
                self.screen.blit(self.Fond_Menu, (0, 0))
                Button.MenuPrincipal(self.mes_button, self.screen, self)

            elif self.etat == "map":
                self.menu_map_screen.MenuMap()

            elif self.etat == "options":
                self.screen.blit(self.Fond_Menu, (0, 0))
                Button.MenuOptions(self.mes_button, self.screen, self, self.sound)

            elif self.etat == "jeu_map1":
                self.jeux_1(word)

            elif self.etat == "jeu_map2":
                self.jeux_2(word)

            elif self.etat == "jeu_map3":
                self.jeux_3(word)

        pygame.display.flip()
        pygame.quit()

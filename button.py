import pygame

def Quitt():
    return False

class Button:
    # le constrcteur pour creer un bouton Menu
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (150, 100)).convert()
        self.rect = self.image.get_rect(center=(x, y))
        self.start = False
        self.menu_optons = pygame.image.load(image_path)

    # cet fonction permet de verifier si notre button est cliquer
    def is_clicked(self, position):
        # verifie si le bouton et le souris sont au meme coordonnes au clik
        if self.rect.collidepoint(position):
            self.start = True
            return True
        else:
            return False

    def Options(self):
        return self.image_options

    @classmethod
    def option_play_Musique(cls, mes_button, screen, sound):
        # On remplace le bouton par un nouveau
        new_button = cls(620, 100,"Assets/Buttons/Play_icon.png")
        mes_button["button_SousMenuStopMusique"] = new_button
        screen.blit(mes_button["button_SousMenuStopMusique"].image, mes_button["button_SousMenuStopMusique"].rect)
        sound.play_sound()

    @classmethod
    def option_stop_audio(cls, mes_button, screen, sound):
        # On remet le boutton initial
        new_button = cls(620, 250,"Assets/Buttons/Pause_icon.png")
        mes_button["button_SousMenuStopAudio"] = new_button
        screen.blit(mes_button["button_SousMenuStopAudio"].image,mes_button["button_SousMenuStopAudio"].rect)
        sound.stop_sound()

    @classmethod
    def option_play_audio(cls, mes_button, screen):
        # On remplace le bouton par un nouveau
        new_button = cls(620, 250,"Assets/Buttons/Play_icon.png")
        mes_button["button_SousMenuStopAudio"] = new_button
        screen.blit(mes_button["button_SousMenuStopAudio"].image,mes_button["button_SousMenuStopAudio"].rect)

    @classmethod
    def option_stop_Musique(cls, mes_button, screen, sound):
        # On remet le boutton initial
        new_button = cls(620, 100,"Assets/Buttons/Pause_icon.png")
        mes_button["button_SousMenuStopMusique"] = new_button
        screen.blit(mes_button["button_SousMenuStopMusique"].image,mes_button["button_SousMenuStopMusique"].rect)
        sound.stop_sound()

    @classmethod
    def MenuPrincipal(cls, mes_button, screen,Map):
        # self.screen.blit(self.Fond_Menu, (0, 0))
        # on charge le Menu

        screen.blit(mes_button["button_Menu"].image, mes_button["button_Menu"].rect)
        screen.blit(mes_button["button_NewGame"].image, mes_button["button_NewGame"].rect)
        screen.blit(mes_button["button_Options"].image, mes_button["button_Options"].rect)
        screen.blit(mes_button["button_Quitt"].image, mes_button["button_Quitt"].rect)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                Map.running = False

            # On écoute les evenement du Menu
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if mes_button["button_NewGame"].is_clicked(pygame.mouse.get_pos()):
                    # si c'est le bouton New Game est (clique) on change l'etat du jeu pour quitter fenetre menu pour aller fenetre dujeux
                    Map.etat = "map"

                elif mes_button["button_Options"].is_clicked(pygame.mouse.get_pos()):
                    # si c'est le bouton options est (clique) on change l'etat du jeu pour quitter fenetre menu pour aller fenetre des options
                    Map.etat = "options"

                elif mes_button["button_Quitt"].is_clicked(pygame.mouse.get_pos()):
                    Map.running = False

        pygame.display.flip()

    @classmethod
    def MenuOptions(cls, mes_button, screen, Map, sound):
        #   On affiche les Boutons du Sous Menues Options

        screen.blit(mes_button["button_SousMenuMusique"].image,mes_button["button_SousMenuMusique"].rect)
        screen.blit(mes_button["button_SousMenuStopMusique"].image,mes_button["button_SousMenuStopMusique"].rect)
        screen.blit(mes_button["button_SousMenuAudio"].image, mes_button["button_SousMenuAudio"].rect)
        screen.blit(mes_button["button_SousMenuStopAudio"].image,mes_button["button_SousMenuStopAudio"].rect)
        screen.blit(mes_button["button_Retour"].image, mes_button["button_Retour"].rect)
        # On écoute les evenements sur les Bouttons qu'on attribue des etats et chaque etats correspond à un fenetre ou une action.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Map.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if mes_button["button_Retour"].is_clicked(pygame.mouse.get_pos()):
                    Map.etat = "menu"

                elif mes_button["button_SousMenuMusique"].is_clicked(pygame.mouse.get_pos()):
                    # On définit aussi des etats aux niveaux des bouttons du Sous Menue Option
                    Map.etat_button_options = "musique"

                    if Map.etat_button_options == "musique":
                        Button.option_play_Musique(mes_button, screen, sound)

                elif mes_button["button_SousMenuStopMusique"].is_clicked(pygame.mouse.get_pos()):

                    if Map.etat_button_options == "musique":
                        Map.etat_button_options = "stop_musique"

                    if Map.etat_button_options == "stop_musique":
                        Button.option_stop_Musique(mes_button, screen, sound)

                elif mes_button["button_SousMenuAudio"].is_clicked(pygame.mouse.get_pos()):
                    Map.etat_button_options = "audio"

                    if Map.etat_button_options == "audio":
                        Button.option_play_audio(mes_button, screen)

                elif mes_button["button_SousMenuStopAudio"].is_clicked(pygame.mouse.get_pos()):
                    if Map.etat_button_options == "audio":
                        Map.etat_button_options = "stop_audio"

                    if Map.etat_button_options == "stop_audio":
                        Button.option_stop_audio(mes_button, screen, sound)

        pygame.display.flip()

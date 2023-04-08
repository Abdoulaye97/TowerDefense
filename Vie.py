import pygame


class Vie:
    def __init__(self):
        self.position_Vie_X = 370
        self.position_Vie_Y = 10
        self.vie_joueur = 100
        self.vie_joueur_max = 100

    def afficher_vie_joueur(self, surface):
        couleur_arriere_plan = (60, 63, 60)
        bar_color = (231, 52, 14)
        position = [self.position_Vie_X, self.position_Vie_Y, self.vie_joueur, 10]
        position_arriere_plan = [self.position_Vie_X, self.position_Vie_Y, self.vie_joueur_max, 10]
        pygame.draw.rect(surface, couleur_arriere_plan, position_arriere_plan)
        pygame.draw.rect(surface, bar_color, position)

    def afficher_le_vie(self, screen):
        police = pygame.font.Font(None, 36)

        # créer une surface qui contient le chiffre 100
        texte = police.render(str(self.vie_joueur), True, (255, 255, 255))

        # dessiner le texte sur la surface de jeu
        screen.blit(texte, (370, 10))

    def degat(self, nbr, screen):
        self.vie_joueur -= nbr
        if self.vie_joueur == 0:
            # Le joueur est mort, afficher un message et quitter le jeu
            font = pygame.font.Font(None, 36)
            message = font.render("Game over!", True, (255, 0, 0))
            screen.blit(message, (250, 250))
            pygame.display.update()

    def health_player(self, screen):
        if self.positionX == 165 and self.positionY == -72:
            self.health -= 1
            print(self.health)
            if self.health == 0:
                # Le joueur est mort, afficher un message et quitter le jeu
                message = self.font.render("Game over!", True, (255, 0, 0))
                screen.blit(message, (250, 250))
                pygame.display.update()
                pygame.time.delay(2000)
                pygame.quit()
            else:
                # Le joueur a encore de la vie, réinitialiser la position du monstre et du joueur
                self.position_depart()

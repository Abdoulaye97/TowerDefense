import pygame

class Monstre(pygame.sprite.Sprite):
    def __init__(self, positionX, positionY):
        super().__init__()
        self.image_monstre = pygame.image.load("alien.png").convert_alpha()
        self.image_monstre = pygame.transform.scale(
            self.image_monstre, (30, 30))
        # self.rect = self.image_monstre.get_rect(center=(positionX, positionY))
        self.positionX = positionX
        self.positionY = positionY
        self.vitesse = 3
        self.health = 2
        self.direction_x = 0
        self.direction_y = 0
        self.nbr_vie = 50
        self.nbr_vie_max = 50
        self.degat = 20

    def position_depart(self):
        self.positionX = 84
        self.positionY = 480

    def update_bar_de_vie(self, surface):
        # j'ai defini un code couleurs rouge qui va etre au dessus du monstre qui etre son niveau de vie
        bar_color = (231, 52, 14)
        # la position va permetrre le niveaux de vie se deplace avec le monstre
        position = [self.positionX + 30, self.positionY + 36, self.nbr_vie, 3]
        # couleur de l'arriere plan qui va permettre devoir si le monstre a subit un degat
        couleur_arriere_plan = (60, 63, 60)
        # la position de l'arriere plan
        position_arriere_plan = [self.positionX + 30, self.positionY + 36, self.nbr_vie_max, 3]
        pygame.draw.rect(surface, couleur_arriere_plan, position_arriere_plan)
        pygame.draw.rect(surface, bar_color, position)

    def move(self):

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.direction_y = -1
                    self.positionY += self.direction_y * 5
                elif event.key == pygame.K_DOWN:
                    self.direction_y = 1
                    self.positionY += self.direction_y * 5
                elif event.key == pygame.K_LEFT:
                    self.direction_x = -1
                    self.positionX += self.direction_x * 5
                elif event.key == pygame.K_RIGHT:
                    self.direction_x = 1
                    self.positionX += self.direction_x * 5

        print("{0},{1}".format(self.positionX, self.positionY))

    def draw_monstre(self, screen, pixels):
        # on affiche le joueur
        screen.blit(self.image_monstre, (self.positionX + pixels, self.positionY + pixels))
        # Dans ces conditions on verifies la position initiale du joueur lors du creation de l'objet si cette position respecte les conditions le monstre pourra se deplacer
        if self.positionY != 324 and self.positionX == 84:
            self.positionY -= self.vitesse

        elif self.positionX != 564 and self.positionY == 324:
            self.positionX += self.vitesse

        elif self.positionY != 42 and self.positionX == 564:
            self.positionY -= self.vitesse

        elif self.positionX != 165 and self.positionY == 42:
            self.positionX -= self.vitesse

        elif self.positionX == 165 and self.positionY != -72:
            self.positionY -= self.vitesse

            if self.positionX == 165 and self.positionY == -69:
                self.position_depart()

    def update_monstre(self, screen, pixels):
        screen.blit(self.image_monstre, (self.positionX +
                                         pixels, self.positionY + pixels))

    def getPositionY(self):
        print("Position X et Y: {0},{1}".format(self.positionX,self.positionY))
        # print("Taille {0}".format(self.image_monstre.get_size()))

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


import pygame


class AfficheurTexte:
    def __init__(self, texte,positionX, positionY,couleur):
        self.positionX=positionX
        self.positionY=positionY
        self.text = texte
        self.couleur=couleur

    def afficher_texte(self,  screen):
        font = pygame.font.Font(None, 36)
        color = pygame.Color(self.couleur[0], self.couleur[1], self.couleur[2])
        text = font.render(self.text, True, color)
        screen.blit(text, (self.positionX, self.positionY))

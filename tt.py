import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition des constantes
LARGEUR = 640
HAUTEUR = 480
COULEUR_FOND = (255, 255, 255)
COULEUR_JOUEUR = (255, 0, 0)

# Classe pour la carte
class Carte:
    def __init__(self):
        self.largeur = LARGEUR
        self.hauteur = HAUTEUR
        self.surface = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Carte")

    def afficher(self):
        self.surface.fill(COULEUR_FOND)
        pygame.display.flip()

# Classe pour le joueur
class Joueur:
    def __init__(self, x, y, couleur):
        self.x = x
        self.y = y
        self.couleur = couleur
        self.direction = "droite"
        self.vitesse = 5 # Vitesse de déplacement
        self.temps_attente = 10 # Temps d'attente en millisecondes entre chaque déplacement

    def se_deplacer(self):
        if self.direction == "droite":
            self.x += self.vitesse
            if self.x >= 600:
                self.direction = "gauche"
        elif self.direction == "gauche":
            self.x -= self.vitesse
            if self.x <= 0:
                self.direction = "droite"

        # Ajouter un délai pour ralentir le déplacement
        pygame.time.delay(self.temps_attente)

    def afficher(self, surface):
        pygame.draw.circle(surface, self.couleur, (self.x, self.y), 10)

# Création de la carte et du joueur
carte = Carte()
joueur = Joueur(320, 240, COULEUR_JOUEUR)

# Boucle de jeu
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mise à jour du joueur
    joueur.se_deplacer()

    # Affichage de la carte et du joueur
    carte.afficher()
    joueur.afficher(carte.surface)

    # Rafraîchissement de l'écran
    pygame.display.flip()

    # Limiter la vitesse de rafraîchissement de l'écran pour réduire le taux de rafraîchissement à 60 images par seconde
    pygame.time.Clock().tick(60)

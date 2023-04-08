import pygame
pygame.init()
word_2 = [

    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 2, 2, 2, 2, 2, 2],

]
class Arme:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.selected = False

    def afficher(self, fenetre):
        fenetre.blit(self.image, (self.rect.x, self.rect.y))

    def tirer(self):
        print("Tirer")

# Charger les images d'armes
image_arme1 = pygame.image.load("Assets/Armes/armes.png")
image_arme2 = pygame.image.load("Assets/Armes/armes.png")

# Créer les objets Arme
arme1 = Arme(50, 50, image_arme1)
arme2 = Arme(150, 50, image_arme2)

# Ajouter les objets Arme à une liste
armes = [arme1, arme2]

# Paramètres de la fenêtre
largeur_fenetre = 640
hauteur_fenetre = 480
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Mon Jeu")

# Boucle de jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for arme in armes:
                if arme.rect.collidepoint(event.pos):
                    arme.selected = True
                    arme_copy = Arme(arme.rect.x, arme.rect.y, arme.image)
                    break
        elif event.type == pygame.MOUSEMOTION:
            if arme_copy is not None and arme_copy.selected:
                arme_copy.rect.center = event.pos
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if arme_copy is not None and arme_copy.selected:
                arme_copy.selected = False
                armes.append(arme_copy)
                arme_copy = None

    fenetre.fill((0, 0, 0)) # Fond noir
    for arme in armes:
        arme.afficher(fenetre)

    pygame.display.flip()

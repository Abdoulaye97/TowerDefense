import pygame

pygame.init()

# Dimensions de la fenêtre
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Créer une classe Image
class Image:
    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)

    def afficher(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def clic(self, x, y):
        if self.x <= x <= self.x + self.image.get_width() and self.y <= y <= self.y + self.image.get_height():
            return Image(self.x, self.y, "chemin_de_votre_image.png")
        else:
            return None


# Initialiser la fenêtre et les variables du jeu
def init():
    global screen, image_originale, image_copiee
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Mon jeu")
    image_originale = Image(100, 100, "chemin_de_votre_image.png")
    image_copiee = None


# Gérer les événements du jeu
def gestion_evenements():
    global running, image_copiee
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if image_copiee is None:
                image_copiee = image_originale.clic(*event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            if image_copiee is not None:
                image_copiee = None
        elif event.type == pygame.MOUSEMOTION:
            if image_copiee is not None:
                image_copiee.x, image_copiee.y = event.pos


# Afficher les éléments du jeu
def afficher():
    screen.fill(WHITE)
    image_originale.afficher(screen)
    if image_copiee is not None:
        image_copiee.afficher(screen)
    pygame.display.flip()


# Gérer la boucle principale du jeu
def boucle_principale():
    global running
    running = True
    while running:
        gestion_evenements()
        afficher()

# Lancer le jeu

import pygame

pygame.init()

# Définir les dimensions de la fenêtre de jeu
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

# Définir les couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initialiser la fenêtre de jeu
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Jeu avec des armes")

# Créer une arme en tant que surface de Pygame
weapon_image = pygame.Surface((50, 50))
weapon_image.fill(RED)

# Initialiser la liste des positions d'armes
weapons_positions = []

# Boucle de jeu
running = True
while running:
    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Vérifier si l'utilisateur a cliqué sur une arme dans la liste des armes
            if pygame.mouse.get_pressed()[0]:
                weapons_positions.append(pygame.mouse.get_pos())

    # Afficher la surface de jeu et les armes
    screen.fill(WHITE)
    for position in weapons_positions:
        screen.blit(weapon_image, position)

    # Mettre à jour l'affichage
    pygame.display.update()

# Quitter Pygame
pygame.quit()

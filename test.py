# hauteur 12
# horizontale 23
# start 12, 3

import pygame

terrain = [

    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],

]

largeur_fenetre = 500
hauteur_fenetre = 500

couleur_fond = (255, 255, 255)
couleur_boule = (255, 0, 0)

taille_boule = 20
vitesse_boule = 5

pygame.init()
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Déplacement de boule")
horloge = pygame.time.Clock()

image_boule = pygame.image.load('Assets/alien.png')
image_boule = pygame.transform.scale(image_boule, (taille_boule, taille_boule))
boule_rect = image_boule.get_rect()

pos_monstre = [12, 3]
positions_visitees = []

def est_position_valide(position):
    x, y = position
    return 0 <= x < len(terrain) and 0 <= y < len(terrain[0]) and terrain[x][y] == 0

terminer = False
while not terminer:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            terminer = True

    x, y = pos_monstre

    if x - 1 >= 0 and est_position_valide([x - 1, y]) and [x - 1, y] not in positions_visitees:
        pos_monstre = [x - 1, y]  # Déplacer vers le haut
    elif x + 1 < len(terrain) and est_position_valide([x + 1, y]) and [x + 1, y] not in positions_visitees:
        pos_monstre = [x + 1, y]  # Déplacer vers le bas
    elif y + 1 < len(terrain[0]) and est_position_valide([x, y + 1]) and [x, y + 1] not in positions_visitees:
        pos_monstre = [x, y + 1]  # Déplacer vers la droite
    elif y - 1 >= 0 and est_position_valide([x, y - 1]) and [x, y - 1] not in positions_visitees:
        pos_monstre = [x, y - 1]  # Déplacer vers la gauche

    positions_visitees.append([x, y])
    fenetre.fill(couleur_fond)
    boule_rect.topleft = (pos_monstre[1] * taille_boule, pos_monstre[0] * taille_boule)
    fenetre.blit(image_boule, boule_rect)
    pygame.display.flip()
    horloge.tick(vitesse_boule)
pygame.quit()
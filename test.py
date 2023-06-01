import pygame
import os

pygame.init()

# Dimensions de la fenêtre
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Lecteur de musique")

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Chargement de la musique
musique_fichier = "Musique/3.mp3"
pygame.mixer.music.load(musique_fichier)

# Chargement des images pour les boutons
bouton_play_img = pygame.image.load("Assets/Buttons/Play_icon.png")
bouton_stop_img = pygame.image.load("Assets/Buttons/Pause_icon.png")

# Redimensionnement des images pour les boutons
largeur_bouton, hauteur_bouton = 100, 100
bouton_play_img = pygame.transform.scale(bouton_play_img, (largeur_bouton, hauteur_bouton))
bouton_stop_img = pygame.transform.scale(bouton_stop_img, (largeur_bouton, hauteur_bouton))

# Position des boutons
position_bouton_play = (largeur // 2 - largeur_bouton // 2, hauteur // 2 - hauteur_bouton // 2)
position_bouton_stop = (largeur // 2 - largeur_bouton // 2, hauteur // 2 - hauteur_bouton // 2)

# État de la musique
musique_en_cours = False

# Boucle principale du jeu
en_cours = True
while en_cours:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            en_cours = False
        elif evenement.type == pygame.MOUSEBUTTONDOWN:
            if evenement.button == 1:  # Clic gauche
                # Récupération de la position du clic
                x, y = evenement.pos
                
                # Vérification si le clic est sur le bouton play
                if position_bouton_play[0] <= x <= position_bouton_play[0] + largeur_bouton and \
                   position_bouton_play[1] <= y <= position_bouton_play[1] + hauteur_bouton:
                    if not musique_en_cours:
                        pygame.mixer.music.play()
                        musique_en_cours = True
                
                # Vérification si le clic est sur le bouton stop
                if position_bouton_stop[0] <= x <= position_bouton_stop[0] + largeur_bouton and \
                   position_bouton_stop[1] <= y <= position_bouton_stop[1] + hauteur_bouton:
                    if musique_en_cours:
                        pygame.mixer.music.stop()
                        musique_en_cours = False

    # Effacement de la fenêtre
    fenetre.fill(BLANC)

    # Affichage des boutons
    if musique_en_cours:
        fenetre.blit(bouton_stop_img, position_bouton_stop)
    else:
        fenetre.blit(bouton_play_img, position_bouton_play)

    # Rafraîchissement de la fenêtre
    pygame.display.flip()

pygame.quit()

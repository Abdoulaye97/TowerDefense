import pygame


class MenuGame:
    def __init__(self, game_instance):
        self.game_instance = game_instance

    def MenuMap(self):
        game = self.game_instance

        # On charge notre fond d'ecran
        game.screen.blit(game.Fond_Menu, (0, 0))
        # On affiche le premier map pour permettre au joueur de choisir
        game.screen.blit(game.cartes["carte_1"].image, game.cartes["carte_1"].rect)
        # On lui indique le niveau de diffultite du map
        game.text["text_easy"].afficher_texte(game.screen)
        # On affiche la deuxime map
        game.screen.blit(game.cartes["carte_2"].image, game.cartes["carte_2"].rect)
        # On lui indique le niveau de diffultite du map
        game.text["text_medium"].afficher_texte(game.screen)
        # On affiche la troisime map
        game.screen.blit(game.cartes["carte_3"].image, game.cartes["carte_3"].rect)
        # On lui indique le niveau de diffultite du map
        game.text["text.difficile"].afficher_texte(game.screen)

        # On parcourt les evenements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Si l'utilisateur clique sur le premiere map
                if game.cartes["carte_1"].is_clicked_map(pygame.mouse.get_pos()):
                    # On change l'etat du jeu qui va charger le map choisie
                    game.etat = "jeu_map1"
                # Si l'utilisateur clique sur le deuxime map
                elif game.cartes["carte_2"].is_clicked_map(pygame.mouse.get_pos()):
                    # On change l'etat du jeu qui va charger le map choisie
                    game.etat = "jeu_map2"
                # Si l'utilisateur clique sur le troisime map
                elif game.cartes["carte_3"].is_clicked_map(pygame.mouse.get_pos()):
                    # On change l'etat du jeu qui charger le map choisie
                    game.etat = "jeu_map3"

        pygame.display.flip()

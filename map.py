import pygame


class Map:
    def __init__(self):
        self.image = pygame.image.load("pirate-zombie-face.png")
        self.running = True
        self.screnn = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Tower Defense")

    def handling(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]:
            self.running = False
        elif pressed[pygame.K_UP]:
            print("haut")
        elif pressed[pygame.K_DOWN]:
            print("en bas")
        elif pressed[pygame.K_RIGHT]:
            print("right")
        elif pressed[pygame.K_LEFT]:
            print("left")

    def run(self):
        self.handling()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screnn.blit(self.image, (0, 0))
            pygame.display.flip()

        pygame.quit()

# A simple demo game
import pygame

card_detail_rect = (0, 192, 260, 384)

if __name__ == "__main__":
    pygame.init()
    
    pygame.display.set_caption("Magik: the Happening")
    screen = pygame.display.set_mode([1024, 768])

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

        # card detail
        pygame.draw.rect(screen, (120, 74, 48), (0, 192, 260, 384))

        # phase panel
        pygame.draw.rect(screen, (150, 150, 150), (260, 0, 40, 768))

        # player 1 board
        pygame.draw.rect(screen, (0, 255, 0), (300, 0, 724, 384))

        # player 1 deck
        pygame.draw.rect(screen, (255, 0, 0), (0, 59, 90, 133))

        # player 1 graveyard
        pygame.draw.rect(screen, (255, 255, 0), (90, 59, 90, 133))

        # player 1 mana pool
        pygame.draw.rect(screen, (0, 0, 255), (180, 0, 80, 192))

        # player 1 life total
        pygame.draw.rect(screen, (150, 150, 150), (0, 0, 180, 59))

        # player 2 board
        pygame.draw.rect(screen, (0, 0, 255), (300, 384, 724, 768))

        # player 2 deck
        pygame.draw.rect(screen, (255, 0, 0), (0, 635, 90, 133))

        # player 2 graveyard
        pygame.draw.rect(screen, (255, 255, 0), (90, 635, 90, 133))

        # player 2 mana pool
        pygame.draw.rect(screen, (0, 0, 255), (180, 576, 80, 192))

        # player 2 life total
        pygame.draw.rect(screen, (150, 150, 150), (0, 576, 180, 59))

        # some text
        default_font = pygame.font.SysFont("Verdana", 24)
        text = default_font.render("Magik: the Happening", True, (255, 255, 255))

        screen.blit(text, (500, 384))

        pygame.display.flip()

    pygame.quit()
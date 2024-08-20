"""
Entry point of the program. 
"""


if __name__ == "__main__":
    # pygame setup
    import pygame
    pygame.init()
    canvas = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Mini-Word")
    
    # main loop
    exit = False
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
        pygame.display.update()
import pygame

pygame.init()
yellow = (255, 255, 0)

clock = pygame.time.Clock()

display_surface = pygame.display.set_mode((700, 650))
pygame.display.set_caption("Best Image 2024")

image = pygame.image.load("0a7be45d2bcfe2d337708fd90098d954.jpg")

DEFAULT_IMAGE_SIZE = (400, 600)

image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

DEFAULT_IMAGE_POSITION = (150, 150)

while True:
    display_surface.fill(yellow)
    display_surface.blit(image, DEFAULT_IMAGE_POSITION)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
            quit()
            
            
    pygame.display.flip()
    clock.tick(30)
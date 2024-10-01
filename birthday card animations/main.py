import pygame
import time

pygame.init()

WIDTH = 600
HEIGHT = 600

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Birthday Greeting Card")

img = pygame.image.load("bg1.jpg")
image1 = pygame.transform.scale(img,(WIDTH,HEIGHT))

img2 = pygame.image.load("bg2.jpg")
image2 = pygame.transform.scale(img2,(WIDTH,HEIGHT))

img3 = pygame.image.load("bg3.jpg")
image3 = pygame.transform.scale(img3,(WIDTH,HEIGHT))

img4 = pygame.image.load("bg4.jpg")
image4 = pygame.transform.scale(img4,(WIDTH,HEIGHT))

img5 = pygame.image.load("bg5.jpg")
image5 = pygame.transform.scale(img5,(WIDTH,HEIGHT))

while True:
    display_surface.fill((255, 255, 255))
    display_surface.blit(image1, (0,0))
    font = pygame.font.SysFont("Ariel", 72)
    text1 = font.render("Happy", True, (0,0,0))
    text2 = font.render("Birthday", True, (0,0,0))
    display_surface.blit(text1,(210, 180))
    display_surface.blit(text2,(160, 264))
    pygame.display.update()
    time.sleep(3)

    display_surface.blit(image2, (0,0))
    font2 = pygame.font.SysFont("Times New Roman", 57)
    text3 = font.render("Wishing you", True, (0,0,0))
    text4 = font.render("a good life", True, "red")
    display_surface.blit(text3, (210, 180))
    display_surface.blit(text4, (160, 264))
    pygame.display.update()
    time.sleep(3)

    display_surface.blit(image3, (0,0))
    pygame.display.update()
    time.sleep(3)

    display_surface.blit(image4, (0,0))
    font3 = pygame.font.SysFont("Ariel", 57)
    text5 = font.render("congrats", True, "purple")
    display_surface.blit(text5, (210,170))
    pygame.display.update()
    time.sleep(3)

    display_surface.blit(image5, (0,0))
    font4 = pygame.font.SysFont("Comic sans", 57)
    text6 = font.render("have a nice day", True, "green")
    display_surface.blit(text6, (210, 100))
    pygame.display.update()
    time.sleep(3)


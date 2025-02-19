#Memory Match Game: Build a game where users match pairs of cards.
import pygame # has a function that can be used to start and stop the music from playing
pygame.init()

window = pygame.display.set_mode((500,800))
window.fill((255,255,255))
pygame.display.flip()

red = pygame.Rect(40,40,150,150)
green = pygame.Rect(190,40,80,150)
blue = pygame.Rect(140,40,150,150)
purple = pygame.Rect(40,190,150,150)
orange = pygame.Rect(190,190,150,150)
pink = pygame.Rect(340,150,150,150)

rectsData= [(red, (255, 38, 71)),(green, (89, 255, 89)),(blue, (43, 132, 255)),(purple, (111, 0, 255)),(orange, (255, 132, 0)),(pink, (246, 71, 255))]

running = True

def drawRectangles(margin_x, margin_y, win_size):
    try: 
        space_x = win_size - (margin_x * 2)
        rect_size = space_x / 3
    except ValueError:
        for i in range(3):
            pos_x = margin_x + (i * rect_size)
            rectsData[i].append(pygame.Rect(pos_x, margin_y, rect_size, rect_size))
        for i in range(3):
            pos_x = margin_x + (i * rect_size)
            rectsData[i + 3].append(pygame.Rect(pos_x, margin_y, rect_size, rect_size))

drawRectangles(40, 40, 800)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((255,255,255))

    
    #Draw Rects
    for i in rectsData:
        pygame.draw.rect(window, i[0], i[1])

    pygame.draw.circle(window, (0,0,0), pygame.mouse.get_pos(), 10)

    pygame.display.flip()

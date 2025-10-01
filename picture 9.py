import pygame
pygame.init()
font = pygame.font.SysFont(None, 60)

screen = pygame.display.set_mode((794, 1123))
pygame.display.set_caption("Картинка  9")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False





    #white screen fill
    screen.fill((255, 255, 255))    

    #background
    pygame.draw.polygon(screen, (83,108,103), [(0,714),(793,714),(793,1122),(0,1122)]) 
    pygame.draw.polygon(screen, (183,196,200), [(0,707),(793,707),(793,0),(0,0)])
    pygame.draw.polygon(screen, (219,227,226), [(777,744),(777,20),(597,20),(597,744)])
    pygame.draw.polygon(screen, (111,145,138), [(526,863),(698,863),(698, 198), (526,198)])
    pygame.draw.ellipse(screen, (168,186,186), (-250,59,800,180))      
    pygame.draw.polygon(screen, (147, 167, 172), [(16,21),(16,737),(178, 737), (178,21)])
    pygame.draw.polygon(screen, (147,172,167), [(206,57),(373,57),(373, 750), (206,750)])
    pygame.draw.ellipse(screen, (168,186,186, 10), (-350,500,800,180)) 
    pygame.draw.polygon(screen, (183, 200, 196), [(127,161),(312,161),(312, 847), (127,847)])
    pygame.draw.ellipse(screen, (168,186,186, 10), (166,277,800,180)) 
    pygame.draw.ellipse(screen, (168,186,186, 10), (233, -20 ,800,180)) 
    pygame.draw.circle(screen, (183, 200, 196), (500, 1935), 1000)

    #blue car + exhaust
    pygame.draw.ellipse(screen, (0,34,43, 10), (287,1004,30,9)) 
    pygame.draw.polygon(screen, (0, 204, 255), [(310,1023),(310,965),(371, 965), (371,929), (537,929), (537,965), (644,965), (644,1023)])
    pygame.draw.polygon(screen, (213, 246, 255), [(385,938),(438, 938),(438, 967), (385,967)])
    pygame.draw.polygon(screen, (213, 246, 255), [(470,936),(519, 936),(519, 964), (470,964)])
    pygame.draw.ellipse(screen, (0,34,43, 10), (335,995,67,48)) 
    pygame.draw.ellipse(screen, (0,34,43, 10), (561,994,67,48)) 
    pygame.draw.ellipse(screen, (168,186,186, 10), (166,277,800,180))
    pygame.draw.ellipse(screen, (168,186,186, 10), (59,958,220,60))
    pygame.draw.ellipse(screen, (168,186,186, 10), (53,884,220,60))
    pygame.draw.ellipse(screen, (168,186,186, 10), (-110,808,220,60))

  
                                                                

    mx, my = pygame.mouse.get_pos()
    text = font.render(f"x: {mx}, y: {my}", True, (0, 0, 0))
    screen.blit(text, (10, 10))


    pygame.display.flip()
    

pygame.quit()
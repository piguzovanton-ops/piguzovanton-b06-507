import pygame
import math
pygame.init()

#графика
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Бросок в баскетбольное кольцо")

background = pygame.image.load("kuchnya.jpg")
background = pygame.transform.scale(background, (600, 400))

egg_image = pygame.image.load("yaichko.jpg").convert()  
egg_image.set_colorkey((255, 255, 255))
egg_image = pygame.transform.scale(egg_image, (50, 50))

pot_image = pygame.image.load("kastrulya.jpg").convert()  
pot_image.set_colorkey((255, 255, 255))
pot_image = pygame.transform.scale(pot_image, (90, 90))

pan_image = pygame.image.load("scovoroda.jpg").convert()  
pan_image.set_colorkey((255, 255, 255))
pan_image = pygame.transform.scale(pan_image, (90, 40))

#музыка и звуковой эффект
pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1) 

score_sound = pygame.mixer.Sound("score.wav")  

#настройки начального положения яйца 
start_x, start_y = 100, 300
x, y = start_x, start_y
radius = 15

#физика
vx, vy = 0, 0
gravity = 0.5
power = 12
angle = 45
bounce_loss = 0.7
on_ground = True

#кастрюля (будет двигаться вверх - вниз)
pot_x, pot_y = 500, 200
pot_width, pot_height = 60, 70
pot_speed_y = 2
pot_direction_y = 1

#сковородка (будет двигаться зигзагообразно)
pan_x, pan_y = 300, 100
pan_width, pan_height = 40, 10
pan_speed = 3
pan_direction_x = 1
pan_direction_y = 1
pan_min_x = 200
pan_max_x = 400
pan_min_y = 50
pan_max_y = 150

#шрифт
font = pygame.font.Font(None, 24)

#попадание, счет
scored_flag = False
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                angle = min(angle + 5, 80)
            elif event.key == pygame.K_DOWN:
                angle = max(angle - 5, 10)
            elif event.key == pygame.K_w:
                power = min(power + 1, 25)
            elif event.key == pygame.K_s:
                power = max(power - 1, 5)
            elif event.key == pygame.K_SPACE and on_ground:
                rad = math.radians(angle)
                vx = power * math.cos(rad)
                vy = -power * math.sin(rad)
                on_ground = False

    #движение кастрюли
    pot_y += pot_speed_y * pot_direction_y
    if pot_y <= 100 or pot_y >= 250:
        pot_direction_y *= -1

    #траектории для сковородки
    pan_x += pan_speed * pan_direction_x
    pan_y += pan_speed * pan_direction_y
    
    #границы движения сковородки
    if pan_x <= pan_min_x or pan_x >= pan_max_x:
        pan_direction_x *= -1
    if pan_y <= pan_min_y or pan_y >= pan_max_y:
        pan_direction_y *= -1

    #движение яйца
    if not on_ground:
        vy += gravity
        x += vx
        y += vy

    #возврат яйца на место, если не попали
    if y + radius >= 400:
        y = 400 - radius
        vy = -vy * bounce_loss
        vx *= bounce_loss
        if abs(vy) < 1 and abs(vx) < 1:
            x, y = start_x, start_y
            vx, vy = 0, 0
            on_ground = True
            scored_flag = False

    #хитбоксы
    pot_rect = pygame.Rect(pot_x, pot_y, pot_width, pot_height)
    pan_rect = pygame.Rect(pan_x, pan_y, pan_width, pan_height)
    egg_rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)

    #начисление очков за попадание
    if egg_rect.colliderect(pot_rect) and not scored_flag:
        scored_flag = True
        score += 1
        score_sound.play()
    if egg_rect.colliderect(pan_rect) and not scored_flag:
        scored_flag = True
        score += 3
        score_sound.play()

    screen.blit(background, (0, 0))

    #отрисовка прицела
    if on_ground:
        points = []
        rad = math.radians(angle)
        temp_vx = power * math.cos(rad)
        temp_vy = -power * math.sin(rad)
        temp_x, temp_y = start_x, start_y
        for i in range(60):
            temp_vy += gravity
            temp_x += temp_vx
            temp_y += temp_vy
            if temp_y + radius >= 400:
                break
            points.append((int(temp_x), int(temp_y)))
        if len(points) > 1:
            pygame.draw.lines(screen, (255, 255, 255), False, points, 2)

    #отрисовка яйца, кастрюли и сковородки
    screen.blit(egg_image, (int(x - radius), int(y - radius)))
    screen.blit(pot_image, (pot_x - 12, pot_y - 5))
    screen.blit(pan_image, (pan_x - 10, pan_y - 15))

    #важная информация
    text_angle = font.render(f"Угол: {angle}°", True, (255, 255, 255))
    text_power = font.render(f"Сила: {power}", True, (255, 255, 255))
    text_score = font.render(f"Счёт: {score}", True, (255, 255, 255))
    text_tutorial = font.render(f"Сковорода = +3 очка, кастрюля = +1 очко", True, (255, 255, 255))
    screen.blit(text_angle, (10, 10))
    screen.blit(text_power, (10, 30))
    screen.blit(text_score, (10, 50))
    screen.blit(text_tutorial, (10, 70))

    #попадание
    if scored_flag:
        hit_text = font.render("ПОПАДАНИЕ!", True, (0, 255, 0))
        screen.blit(hit_text, (250, 50))

    pygame.display.flip()
    pygame.time.delay(20)

pygame.quit()
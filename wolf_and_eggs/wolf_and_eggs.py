import pygame
import random

pygame.init()

#звуки
score_sound = pygame.mixer.Sound("score.wav")
egg_sound = pygame.mixer.Sound("egg1.wav")


#настройка экрана и фона
screen_height = 800
screen_width = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Волк в корзинке ловит яйца")

background = pygame.image.load("farm_background.png")
background = pygame.transform.scale(background, (screen_width, screen_height))

#загрузка изображений с удалением белого фона
egg_image = pygame.image.load("egg.jpg").convert()  
egg_image.set_colorkey((255, 255, 255))
egg_image = pygame.transform.scale(egg_image, (150, 150))

wolf_image = pygame.image.load("wolf.jpg").convert()  
wolf_image.set_colorkey((255, 255, 255)) 
wolf_image = pygame.transform.scale(wolf_image, (300, 200))


#яйца и их точки спавна
spawn_points = [(0.1 * screen_width, 0.3 * screen_height), (0.1 * screen_width, 0.1 * screen_height), (0.9 * screen_width, 0.3 * screen_height), (0.9 * screen_width, 0.1 * screen_height)]

running = True
clock = pygame.time.Clock()

eggs = []
spawn_interval = 1000  
last_spawn_time = 0

#сколько живут яйца + счетчик пропущенных
egg_lifetime = 2000
missed_streak = 0
max_misses = 3


#параметры игрока (корзиночный волк)
player_radius = 100
player_x = screen_width // 2
player_y = screen_height - 100
player_speed = 5


#счет
score = 0
font = pygame.font.SysFont(None, 36)


while running:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #управление по wasd + границы
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player_x > player_radius:
        player_x -= player_speed
    if keys[pygame.K_d] and player_x < screen_width - player_radius:
        player_x += player_speed
    if keys[pygame.K_w] and player_y > player_radius:
        player_y -= player_speed
    if keys[pygame.K_s] and player_y < screen_height - player_radius:
        player_y += player_speed

    #спавн яиц + направление(если у яйца спавн слева, то направление вправо (+), если справа, то налево (-))
    if current_time - last_spawn_time > spawn_interval:
        x, y = random.choice(spawn_points)
        if x < screen_width / 2:
            direction = 2
        else:
            direction = -2
        eggs.append([x, y, direction, current_time])
        last_spawn_time = current_time

    #движение яиц(по x задал через direction)
    for egg in eggs:
        egg[1] += 4
        egg[0] += egg[2]

    
    egg_radius = 50
    eggs_to_remove = []
    
    for egg in eggs:
        x, y, direction, spawn_time = egg
        
        #если яйцо не поймано вовремя, то + к числу пропущенных подряд
        if current_time - spawn_time > egg_lifetime:
            egg_sound.play()
            eggs_to_remove.append(egg)
            missed_streak += 1
            
            
        #засчитываем, если сталкиваются (высчитываем через формулу для окружностей)
        dx = player_x - x
        dy = player_y - y
        distance = (dx**2 + dy**2)**0.5
        
        if distance < player_radius + egg_radius:
            score_sound.play()
            eggs_to_remove.append(egg)
            score += 1
            missed_streak = 0

    #убираем яйца после 
    for egg in eggs_to_remove:
        if egg in eggs:
            eggs.remove(egg)

    #закрытие игры, если несколько раз пропустить яйцо(тут 3 раза подярд)
    if missed_streak >= max_misses:
        running = False

   

    #фон
    screen.fill((255, 255, 255))
    screen.blit(background, (0,0))
    
    #картинки для яиц
    for egg in eggs:
        x, y, direction, spawn_time = egg
        image_rect = egg_image.get_rect(center=(int(x), int(y)))
        screen.blit(egg_image, image_rect)
    
    #картинка для корзиночного волка
    wolf_rect = wolf_image.get_rect(center=(int(player_x), int(player_y)))
    screen.blit(wolf_image, wolf_rect)
    
    #показываем счет
    score_text = font.render(f"Счет: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
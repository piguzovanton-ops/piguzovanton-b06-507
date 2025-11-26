import pygame
import math
import random


WIDTH, HEIGHT = 1200, 800
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Солнечная система")
cx = WIDTH // 2
cy = HEIGHT // 2   
FPS = 60
clock = pygame.time.Clock()

time_scale = 1.0 #для изменения скорости(интерактивный элемент)


background = pygame.image.load("space_background.jpg") #фон
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

sun = pygame.image.load("sun.jpg")  #красивое солнце
sun = pygame.transform.scale(sun, (45, 45))
sun.set_colorkey((255, 255, 255))

pygame.mixer.init() #музыка
pygame.mixer.music.load("space_music.mp3")
pygame.mixer.music.play(-1) 


class Planet:
    def __init__(self, screen, radius, orbit_radius, color=None, speed=0, angle=0, image_path=None):
        self.screen = screen
        self.radius = radius
        self.orbit_radius = orbit_radius
        self.color = color
        self.speed = speed
        self.angle = angle
        self.x = 0
        self.y = 0
        self.image = None
        if image_path:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (radius*2, radius*2))
            self.image.set_colorkey((255, 255, 255))

    def update(self, dt):
        global cx, cy
        self.angle += self.speed * dt
        self.x = cx + self.orbit_radius * math.cos(self.angle)
        self.y = cy + self.orbit_radius * math.sin(self.angle)

    def draw(self):
        if self.image:
            self.screen.blit(self.image, (int(self.x - self.radius), int(self.y - self.radius)))
        else:
            pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.radius)


class Asteroid: #класс астероид по аналогии с классом планет
    def __init__(self, screen, radius, color=None, speed=0, image_path=None):
        self.screen = screen
        self.radius = radius
        self.color = color
        self.speed = speed
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0
        self.active = False
        self.image = None
        if image_path:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (radius*4, radius*4))
            self.image.set_colorkey((255, 255, 255))
        
    def reset(self):
        #случайный выбор откуда полетит астероид
        side = random.choice(['top', 'right', 'bottom', 'left'])
        
        if side == 'top':
            self.x = random.randint(0, WIDTH)
            self.y = -10
            self.dx = random.choice([-4, 4])
            self.dy = random.choice([4, 6])
        elif side == 'right':
            self.x = WIDTH + 10
            self.y = random.randint(0, HEIGHT)
            self.dx = random.choice([-4, -6])
            self.dy = random.choice([-4, 4])
        elif side == 'bottom':
            self.x = random.randint(0, WIDTH)
            self.y = HEIGHT + 10
            self.dx = random.choice([-4, 4])
            self.dy = random.choice([-4, -6])
        elif side == 'left':
            self.x = -10
            self.y = random.randint(0, HEIGHT)
            self.dx = random.choice([4, 6])
            self.dy = random.choice([-4, 4])
            
        self.active = True
        
    def update(self):
        if not self.active:
            return
            
        self.x += self.dx
        self.y += self.dy
        
        #убираем астероид, если улетел за пределы окна
        if (self.x < -100 or self.x > WIDTH + 100 or self.y < -100 or self.y > HEIGHT + 100):
            self.active = False
            
    def draw(self):
        if self.active:
            if self.image:
                self.screen.blit(self.image, (int(self.x - self.radius), int(self.y - self.radius)))
            else:
                pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.radius)



class Moon: #класс Луна по аналогии с планетами
    def __init__(self, screen, radius, orbit_radius, planet, color=None, speed=0, angle=0, image_path=None):
        self.screen = screen
        self.radius = radius
        self.orbit_radius = orbit_radius
        self.planet = planet  #планета, около которой будет ее орбита
        self.color = color
        self.speed = speed
        self.angle = angle
        self.x = 0
        self.y = 0
        self.image = None
        if image_path:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (radius*2, radius*2))
            self.image.set_colorkey((255, 255, 255))

    def update(self, dt):
        #обновляем угол вращения вокруг планеты
        self.angle += self.speed * dt
        #позиция луны относительно планеты
        self.x = self.planet.x + self.orbit_radius * math.cos(self.angle)
        self.y = self.planet.y + self.orbit_radius * math.sin(self.angle)

    def draw(self):
        if self.image:
            self.screen.blit(self.image, (int(self.x - self.radius), int(self.y - self.radius)))
        else:
            pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.radius)


mercury  = Planet(screen, radius = 4, orbit_radius = 50, color=(155, 105, 105), speed =1.59)
venus  = Planet(screen, radius = 9, orbit_radius = 80, color=(255, 100, 80), speed = 1.17, image_path = "venus.jpg")
earth = Planet(screen, radius = 10, orbit_radius=120, speed=1, image_path = "earth.jpg")
mars  = Planet(screen, radius = 5, orbit_radius=160, color=(255, 100, 80), speed=0.81)
jupiter  = Planet(screen, radius = 25, orbit_radius=220, color=(255, 100, 80), speed = 0.44, image_path = "jupiter.jpg")
saturn  = Planet(screen, radius = 20, orbit_radius=280, color=(255, 100, 80), speed = 0.33, image_path = "saturn.jpg")
uranus  = Planet(screen, radius = 12, orbit_radius=330, color=(255, 100, 80), speed = 0.23, image_path = "uranus.jpg")
neptune  = Planet(screen, radius = 12, orbit_radius=360, color=(255, 100, 80), speed = 0.18, image_path = "neptune.jpg")
pluto  = Planet(screen, radius = 2 , orbit_radius=380, color=(105, 105, 105), speed = 0.16)


moon = Moon(screen, radius=3, orbit_radius=20, planet=earth, color=(200, 200, 200), speed= 5)


asteroid = Asteroid(screen, radius=5, color=(150, 150, 150), image_path = "asteroid.jpg")
asteroid_timer = 0
ASTEROID_INTERVAL = 5000 


running = True
while running:
    dt = clock.tick(FPS) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            cx = WIDTH // 2
            cy = HEIGHT // 2  
        elif event.type == pygame.KEYDOWN:
            #управление скоростью времени
            if event.key == pygame.K_UP:
                time_scale *= 1.5  #ускорить время
            elif event.key == pygame.K_DOWN:
                time_scale /= 1.5  #замедлить время
                #ограничим скорость снизу
                if time_scale < 0.1:
                    time_scale = 0.1
    
    mercury.update(dt*time_scale)
    venus.update(dt*time_scale)
    earth.update(dt*time_scale)
    mars.update(dt*time_scale)
    jupiter.update(dt*time_scale)
    saturn.update(dt*time_scale)
    uranus.update(dt*time_scale)
    neptune.update(dt*time_scale)
    pluto.update(dt*time_scale)

    moon.update(dt*time_scale)
    
    #таймер астероида
    current_time = pygame.time.get_ticks()
    if current_time - asteroid_timer > ASTEROID_INTERVAL:
        asteroid.reset()
        asteroid_timer = current_time
    
    asteroid.update()
    

    #отрисовки
    screen.fill((0, 0, 20))
    screen.blit(background, (0, 0))
    
    screen.blit(sun, (WIDTH // 2 - 23, HEIGHT // 2  - 23))
    mercury.draw()
    venus.draw()
    earth.draw()
    mars.draw()
    jupiter.draw()
    saturn.draw()
    uranus.draw()
    neptune.draw()
    pluto.draw()
    

    moon.draw()


    asteroid.draw()
    
    pygame.display.flip()

pygame.quit()
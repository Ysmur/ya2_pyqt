import pygame

# инициализация Pygame:
pygame.init()
# размеры окна:
size = width, height = 800, 600
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)
# метод clock.tick() возвращает количество миллисекунд, прошедших с момента последнего вызова
clock = pygame.time.Clock()
# формирование кадра:
# команды рисования на холсте
running = True
x_pos = 0
v = 20   # пикселей в секунду
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (int(x_pos), 200), 20)
    x_pos += v * clock.tick() / 1000 # v * t в секундах
    pygame.display.flip()

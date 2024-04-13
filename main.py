import pygame

BLUE = (205, 255, 255)
WHITE = (255, 255, 255)
FRAME_COLOR = (0, 255, 215)
SIZE_BLOCK = 20
COUNT_BLOCKS = 20
MARGIN = 1

size = [450, 600]

screen = pygame.display.set_mode(size)   # создаем окно размером 600 x 800
pygame.display.set_caption('Snake')     # создание заголовка

while True:
    for event in pygame.event.get():    # получаем все события которые к нам приходят
        if event.type == pygame.QUIT:
            pygame.quit()               # закрытие окна

    screen.fill(FRAME_COLOR)    # заливка экрана

    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row + column) % 2 == 0:
                color = BLUE
            else:
                color = WHITE
            pygame.draw.rect(screen, color, [10 + column * SIZE_BLOCK + MARGIN * (column + 1),
                                              20 + row * SIZE_BLOCK + MARGIN * (row + 1), SIZE_BLOCK, SIZE_BLOCK])   # рисуем квдратики на игровом поле

    pygame.display.flip()       # метод применяет все что нарисовано на экране
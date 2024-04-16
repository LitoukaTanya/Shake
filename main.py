import pygame
import sys
import random

pygame.init()

RED = (230, 0, 0)
BLUE = (205, 255, 255)
WHITE = (255, 255, 255)
FRAME_COLOR = (0, 255, 215)
SIZE_BLOCK = 20
COUNT_BLOCKS = 20
MARGIN = 1
HEADER_MARGIN = 70
HEADER_COLOR = (0, 204, 205)
SNAKE_COLOR = (0, 240, 15)

size = [SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS,
        SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS + HEADER_MARGIN]

screen = pygame.display.set_mode(size)  # создаем окно размером size
pygame.display.set_caption('Snake')  # создание заголовка
timer = pygame.time.Clock()
courier = pygame.font.SysFont('courier', 36)      # шрифт


class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0 <= self.x < COUNT_BLOCKS and 0 <= self.y < COUNT_BLOCKS

    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y


def get_random_empty_block():
    x = random.randint(0, COUNT_BLOCKS - 1)
    y = random.randint(0, COUNT_BLOCKS - 1)
    empty_block = SnakeBlock(x, y)
    while empty_block in snake_blocks:
        empty_block.x = random.randint(0, COUNT_BLOCKS - 1)
        empty_block.x = random.randint(0, COUNT_BLOCKS - 1)
    return empty_block


def draw_block(color, row, column):
    pygame.draw.rect(screen, color, [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
                                     HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1), SIZE_BLOCK,
                                     SIZE_BLOCK])


snake_blocks = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)]

total = 0
apple = get_random_empty_block()
d_row = buf_row = 0
d_col = buf_col = 1
speed = 1

while True:
    for event in pygame.event.get():  # получаем все события которые к нам приходят
        if event.type == pygame.QUIT:
            pygame.quit()  # закрытие окна
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and d_col != 0:
                buf_row = -1
                buf_col = 0
            elif event.key == pygame.K_DOWN and d_col != 0:
                buf_row = 1
                buf_col = 0
            elif event.key == pygame.K_LEFT and d_row != 0:
                buf_row = 0
                buf_col = -1
            elif event.key == pygame.K_RIGHT and d_row != 0:
                buf_row = 0
                buf_col = 1

    screen.fill(FRAME_COLOR)  # заливка экрана
    pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])

    text_total = courier.render(f"Total: {total}", 0, WHITE)
    text_speed = courier.render(f"Speed: {speed}", 0, WHITE)
    screen.blit(text_total, (SIZE_BLOCK, SIZE_BLOCK))
    screen.blit(text_speed, (SIZE_BLOCK + 210, SIZE_BLOCK))

    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row + column) % 2 == 0:
                color = BLUE
            else:
                color = WHITE
            draw_block(color, row, column)  # рисуем квдратики на игровом поле

    head = snake_blocks[-1]
    if not head.is_inside():
        print('crash')
        pygame.quit()
        sys.exit()

    draw_block(RED, apple.x, apple.y)
    for block in snake_blocks:
        draw_block(SNAKE_COLOR, block.x, block.y)

    pygame.display.flip()  # метод применяет все что нарисовано на экране

    if apple == head:
        total += 1
        speed = total // 2 + 1
        snake_blocks.append(apple)
        apple = get_random_empty_block()

    d_row = buf_row
    d_col = buf_col
    new_head = SnakeBlock(head.x + d_row, head.y + d_col)

    if new_head in snake_blocks:
        print("crash your self")
        pygame.quit()
        sys.exit()

    snake_blocks.append(new_head)
    snake_blocks.pop(0)

    timer.tick(speed)

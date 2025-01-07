import pygame
from viewport import Viewport
from line import Line
from utils import draw_dashed_line

WIDTH, HEIGHT = 800, 600
WINDOW_COLOR = (200, 200, 200)
LINE_COLOR_VISIBLE = (0, 0, 255)
LINE_COLOR_HIDDEN = (200, 0, 0)
VIEWPORT_COLOR = (0, 255, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Line clipper")
clock = pygame.time.Clock()

lines = [Line.random(WIDTH, HEIGHT) for _ in range(20)]
viewport = Viewport(WIDTH // 4, HEIGHT // 4, WIDTH // 2, HEIGHT // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    viewport.move(keys)

    screen.fill(WINDOW_COLOR)
    pygame.draw.rect(screen, VIEWPORT_COLOR, viewport.rect, 2)

    for line in lines:
        segments_visible, segments_hidden = line.clip(viewport)

        for start, end in segments_visible:
            pygame.draw.line(screen, LINE_COLOR_VISIBLE, start, end, 2)

        for start, end in segments_hidden:
            draw_dashed_line(screen, LINE_COLOR_HIDDEN, start, end)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

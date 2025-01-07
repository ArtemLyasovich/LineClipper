import pygame

def draw_dashed_line(surface, color, start_pos, end_pos, width=1, dash_length=10):
    x1, y1 = start_pos
    x2, y2 = end_pos
    length = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

    if length == 0:
        return

    dx, dy = (x2 - x1) / length, (y2 - y1) / length

    for i in range(0, int(length // dash_length)):
        if i % 2 == 0:
            start = (x1 + dx * i * dash_length, y1 + dy * i * dash_length)
            end = (x1 + dx * (i + 1) * dash_length, y1 + dy * (i + 1) * dash_length)
            pygame.draw.line(surface, color, start, end, width)

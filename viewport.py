import pygame

class Viewport:
    def __init__(self, x, y, width, height, speed=10):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    @property
    def left(self):
        return self.rect.left

    @property
    def right(self):
        return self.rect.right

    @property
    def top(self):
        return self.rect.top

    @property
    def bottom(self):
        return self.rect.bottom

    def move(self, dx, dy):
        self.rect.move_ip(dx, dy)

    def clamp(self, bounds):
        self.rect.clamp_ip(bounds)

    def draw(self, surface, color):
        pygame.draw.rect(surface, color, self.rect, 2)

    def collidepoint(self, point):
        """Proxy method for checking if a point is inside the viewport."""
        return self.rect.collidepoint(point)
    
    def move(self, keys):
        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -self.speed)
        if keys[pygame.K_DOWN]:
            self.rect.move_ip(0, self.speed)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)

        self.rect.clamp_ip(pygame.Rect(0, 0, 800, 600))

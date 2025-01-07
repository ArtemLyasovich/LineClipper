import random
from pygame import Vector2

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.start = (x1, y1)
        self.end = (x2, y2)

    @staticmethod
    def random(width, height):
        """Generates a random line within the given width and height."""
        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 = random.randint(0, width), random.randint(0, height)
        return Line(x1, y1, x2, y2)

    def clip(self, viewport):
        def compute_intersection(p1, p2, bound, axis):
            p1, p2 = Vector2(p1), Vector2(p2)
            d = p2 - p1
            t = (bound - p1[axis]) / d[axis] if d[axis] != 0 else None
            if t is not None and 0 <= t <= 1:
                return p1 + t * d
            return None

        segments_visible = []
        segments_hidden = []

        x1, y1 = self.start
        x2, y2 = self.end

        # Find all intersections with the viewport edges
        intersections = []
        for bound, axis in [(viewport.left, 0), (viewport.right, 0), (viewport.top, 1), (viewport.bottom, 1)]:
            inter = compute_intersection((x1, y1), (x2, y2), bound, axis)
            if inter:
                intersections.append(inter)

        # Combine start/end points with intersections and sort
        points = [(x1, y1), (x2, y2)] + intersections
        points.sort(key=lambda p: (p[0], p[1]))

        # Determine visibility of each segment
        for i in range(len(points) - 1):
            p_start, p_end = points[i], points[i + 1]
            midpoint = ((p_start[0] + p_end[0]) / 2, (p_start[1] + p_end[1]) / 2)
            if viewport.collidepoint(midpoint):
                segments_visible.append((p_start, p_end))
            else:
                segments_hidden.append((p_start, p_end))

        return segments_visible, segments_hidden

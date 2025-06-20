from manim import *

class crucible(Scene):
    def construct(self):
        crucible_points = [
            [-3, 3, 0],
            [-3, -3, 0],
            [3, -3, 0],
            [3, 3, 0],
            [2, 3, 0],
            [2, -2, 0],
            [-2, -2, 0],
            [-2, 3, 0]
        ]
        crucible = Polygon(*crucible_points, fill_color=ManimColor.from_hex('#03dbfc'), fill_opacity=0.5)
        circle = Circle()
        self.play(Create(circle))
        self.play(Transform(circle, crucible))
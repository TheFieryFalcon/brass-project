from manim import *
# manim -pql [file] [method]
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

        ziggurat_points = [
            [-3,0,0],
            [-3,1,0],
            [-2,1,0],
            [-2,2,0],
            [-1,2,0],
            [-2,0,0],
            [-1,2,0],
            [-1,3,0],
            [0,3,0],
            [0,2,0],
            [1,2,0],
            [1,1,0],
            [2,1,0],
            [2,0,0],
            

        ]
        ziggurat = Polygon(*ziggurat_points, fill_color=ManimColor.from_hex('#EDC9AF'),fill_opacity=0.5)
        self.play(Create(ziggurat))
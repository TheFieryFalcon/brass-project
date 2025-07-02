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
        shcrucible_copper = Polygon(*crucible_points, fill_color=ManimColor.from_hex('#03dbfc'), fill_opacity=1).move_to([-2, 0, 0])
        shcrucible_tin = Polygon(*crucible_points, fill_color=ManimColor.from_hex('#03dbfc'), fill_opacity=1).scale(0.3).next_to(shcrucible_copper, RIGHT, buff=1)
        copper_fill = Rectangle(ORANGE, 4, 4, fill_color=ORANGE, fill_opacity=1).move_to([shcrucible_copper.get_x(), shcrucible_copper.get_y(), 0])
        tin_fill = Rectangle(LIGHT_GRAY, 1.2, 1.2, fill_color=GRAY, fill_opacity=1).move_to([shcrucible_tin.get_x(), shcrucible_tin.get_y(), 0])
        self.play(Create(shcrucible_copper), Create(shcrucible_tin), Create(copper_fill), Create(tin_fill))
        crucible_tin = Group(shcrucible_tin, tin_fill)
        tin_fill_in = Rectangle(LIGHT_GRAY, 0.3, 4, fill_color=LIGHT_GRAY, fill_opacity=1).next_to(copper_fill, UP, buff=0)
        self.wait(3)
        self.play(crucible_tin.animate.move_to([shcrucible_tin.get_x(), 3, 0]))
        self.play(shcrucible_tin.animate.rotate(90, X_AXIS, crucible_tin.center()), tin_fill.animate.rotate(90, X_AXIS, crucible_tin.center()))
        self.play(ReplacementTransform(tin_fill, tin_fill_in))
        self.play(tin_fill_in.animate.set_color(interpolate_color(ORANGE, LIGHT_GRAY)), copper_fill.animate.set_color(interpolate_color(ORANGE, LIGHT_GRAY)))

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

        skyscraper_points = [
            [-2,-3,0]
            [2,-3,0]
            [1.5,3,0]
            [-1.5,3,0]
        ]
        skyscraper = Polygon(*skyscraper_points, fill_color=ManimColor.from_hex('#CED2D7'), fill_opacity=0.75)
        self.play(create(skyscraper))

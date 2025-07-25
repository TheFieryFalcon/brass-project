from manim import *
# manim -pql [file] [method]
def fade_out(scene: Scene):
    animations = []
    for mobject in scene.get_top_level_mobjects():
        animations.append(FadeOut(mobject))
    scene.play(*animations)
class main(Scene):
    def construct(self):
        scene_order = [crucible, ziggurat, stainless_steel_skyscraper, bighole]
        for scene in scene_order:
            iscene = scene()
            iscene.construct()
            fade_out(iscene)
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
        shcrucible_copper = Polygon(*crucible_points, fill_color=ManimColor.from_hex('#41424C'),stroke_color=ManimColor.from_hex('#41424C'), fill_opacity=1).scale(0.8).move_to([-2, 0, 0])
        shcrucible_tin = Polygon(*crucible_points, fill_color=ManimColor.from_hex('#41424C'), stroke_color=ManimColor.from_hex('#41424C'), fill_opacity=1).scale(0.3).next_to(shcrucible_copper, RIGHT, buff=1)
        copper_fill = Rectangle(ORANGE, 3.2, 3.2, fill_color=ORANGE, fill_opacity=1).move_to([shcrucible_copper.get_x(), shcrucible_copper.get_y(), 0])
        tin_fill = Rectangle(LIGHT_GRAY, 1.2, 1.2, fill_color=GRAY, fill_opacity=1).move_to([shcrucible_tin.get_x(), shcrucible_tin.get_y(), 0])
        tin_fill_in = Rectangle(LIGHT_GRAY, 0.3, 3.2, fill_color=LIGHT_GRAY, fill_opacity=1).next_to(copper_fill, UP, buff=0)
        self.play(Create(shcrucible_copper), Create(shcrucible_tin), Create(copper_fill), Create(tin_fill))
        crucible_tin = Group(shcrucible_tin, tin_fill)
        self.wait(3)
        self.play(crucible_tin.animate.move_to([shcrucible_tin.get_x()-1, 4, 0]))
        self.play(Rotate(crucible_tin, PI*0.5, Z_AXIS, shcrucible_tin.get_center(), rate_func=linear))
        self.play(ReplacementTransform(tin_fill, tin_fill_in))
        self.play(tin_fill_in.animate.set_color('#CE8946'), copper_fill.animate.set_color('#CE8946'))

class ziggurat(Scene):
    def construct(self):
        ziggurat_points = [
            [-3,0,0],
            [-3,1,0],
            [-2,1,0],
            [-2,2,0],
            [-1,2,0],
            [-2,0,0],#Frame of left side steps
            [-1,2,0],
            [-1,3,0],
            [0,3,0],
            [0,2,0],
            [1,0,0], #Frame of right side steps
            [0,2,0],
            [1,2,0],
            [1,1,0],
            [2,1,0],
            [2,0,0],
        ]
        ziggurat_step_points = [
            [-1.8,0,0],
            [-1.8,0.4,0],
            [-1.6,0.4,0],
            [-1.6,0.8,0],
            [-1.4,0.8,0],
            [-1.4,1.2,0],
            [-1.2,1.2,0],
            [-1.2,1.6,0],
            [-1,1.6,0],
            [-1,2,0],
            [-0.77,2,0],
            [-0.77,2.77,0],
            [-0.22,2.77,0],
            [-0.22,2,0],
            [0,2,0],
            [-1,2,0],
            [0,2,0],
            [0,1.6,0],
            [-1,1.6,0], # top step divider
            [0,1.6,0],
            [0.2,1.6,0],
            [0.2,1.2,0],
            [-1.2,1.2,0], #second step divider
            [0.4,1.2,0],
            [0.4,0.8,0],
            [-1.6,.8,0], #third step divider
            [0.6,0.8,0],
            [0.6,0.4,0],
            [-1.8,0.4,0], #bottom step divider
            [0.8,0.4,0],
            [0.8,0,0],
        ]
        ziggurat = Polygon(*ziggurat_points, fill_color=ManimColor.from_hex('#EDC9AF'), stroke_color=ManimColor.from_hex('#c9ae74'),fill_opacity=0.5)
        ziggurat_steps = Polygon(*ziggurat_step_points, fill_color=ManimColor.from_hex('#EDC9AF'), stroke_color=ManimColor.from_hex('#c9ae74'),fill_opacity=0.5)
        self.play(Create(ziggurat),Create(ziggurat_steps))
        self.wait(5)
class stainless_steel_skyscraper(Scene):
    def construct(self):
        skyscraper_points = [
            [-2,-3,0],
            [2,-3,0],
            [2,3,0],
            [-2,3,0]
        ]
        window1 = Rectangle(height=0.23, width=0.20, stroke_color=ManimColor.from_hex("#aeb2b8"), stroke_width=0.01, fill_color=ManimColor.from_hex("#C7E3E1"), fill_opacity=0.85).set_x(-1.66).set_y(2.66)
        w2 = window1.copy().next_to(window1, RIGHT, buff=0.16)
        w3 = w2.copy().next_to(w2, RIGHT, buff=0.16)
        w4 = w3.copy().next_to(w3, RIGHT, buff=0.16)
        w5 = w4.copy().next_to(w4, RIGHT, buff=0.16)
        w6 = w5.copy().next_to(w5, RIGHT, buff=0.16)
        w7 = w6.copy().next_to(w6, RIGHT, buff=0.16)
        w8 = w7.copy().next_to(w7, RIGHT, buff=0.16)
        w9 = w8.copy().next_to(w8, RIGHT, buff=0.16)
        w10 = w9.copy().next_to(w9, RIGHT, buff=0.16)
        warray = Group(window1, w2, w3, w4, w5, w6, w7, w8, w9, w10)
        warray2 = warray.copy().next_to(warray, DOWN, buff=0.14)
        warray3 = warray2.copy().next_to(warray2, DOWN, buff=0.14)
        warray4 = warray3.copy().next_to(warray3, DOWN, buff=0.14)
        warray5 = warray4.copy().next_to(warray4, DOWN, buff=0.14)
        warray6 = warray5.copy().next_to(warray5, DOWN, buff=0.14)
        warray7 = warray6.copy().next_to(warray6, DOWN, buff=0.14)
        warray8 = warray7.copy().next_to(warray7, DOWN, buff=0.14)
        warray9 = warray8.copy().next_to(warray8, DOWN, buff=0.14)
        warray10 = warray9.copy().next_to(warray9, DOWN, buff=0.14)
        warray11 = warray10.copy().next_to(warray10, DOWN, buff=0.14)
        warray12 = warray11.copy().next_to(warray11, DOWN, buff=0.14)
        warray13 = warray12.copy().next_to(warray12, DOWN, buff=0.14)
        warray14 = warray13.copy().next_to(warray13, DOWN, buff=0.14)
        warray15 = warray14.copy().next_to(warray14, DOWN, buff=0.14)
        fullwindowarray = Group(warray, warray2, warray3, warray4, warray5, warray6, warray7, warray8, warray9, warray10, warray11, warray12, warray13, warray14, warray15)
        stainless_pipe = Circle(radius=0.6, stroke_color=ManimColor.from_hex('#b4bdc7'), fill_opacity=0, stroke_width=1)
        sp2 = stainless_pipe.copy().next_to(stainless_pipe, DR, 0)
        sp3 = sp2.copy().next_to(sp2, LEFT, 0)
        sp4 = sp3.copy().next_to(sp3, LEFT, 0)
        sp5 = sp2.copy().next_to(sp2, DR, 0)
        sp6 = sp2.copy().next_to(sp2, DOWN, 0)
        sp7 = sp2.copy().next_to(sp2, DL, 0)
        sp8 = sp2.copy().next_to(sp4, DOWN, 0)
        sp9 = sp2.copy().next_to(sp4, DL, 0)
        spall = Group(stainless_pipe, sp2, sp3, sp4, sp5, sp6, sp7, sp8, sp9)
        text2 = Text("Stainless Steel: In 1796, chromium was discovered and found to have\n anti-oxidant properties when added to metals. It was\n used throughout the 19th century, but the modern stainless\n steel was invented by Harry Brearley in 1913 and greatly aided\n the Allies in fighting World War I. Today, it is used in pretty much everything.", 0.5, 0.05, ManimColor.from_hex("#A7C7E7"), line_spacing=1.5).set_x(2).set_y(3).scale(0.25)
        self.play(Create(spall), FadeIn(text2))
        self.wait(4)
        skyscraper_body = Polygon(*skyscraper_points, fill_color=ManimColor.from_hex('#CED2D7'), fill_opacity=0.75)
        self.play(ReplacementTransform(stainless_pipe, skyscraper_body), FadeOut(sp2, sp3, sp4, sp5, sp6, sp7, sp8, sp9, text2))
        self.add(fullwindowarray)
        self.wait(2)
class bighole(Scene):
    def construct(self):
        hole1=Ellipse(width=8.0,height=4.0,stroke_color=("#000000")).set_fill("#d5682e",opacity=1)
        hole2=hole1.copy().scale(0.9).set_fill("#c05d28").align_to(hole1,DOWN)
        hole3=hole2.copy().scale(0.9).set_fill("#aa5425").align_to(hole1,DOWN)
        hole4=hole3.copy().scale(0.9).set_fill("#813f1b").align_to(hole1,DOWN)
        hole5=hole4.copy().scale(0.9).set_fill("#5d2c12").align_to(hole1,DOWN)
        hole6=hole5.copy().set_fill("#06bee4").scale(0.2).move_to([0,-1.5,0])
        holecut=Rectangle(width=4,height=1).set_color("#000000",opacity=1).move_to([0,-2.1,0])
        pit=Group(hole1,hole2,hole3,hole4,hole5,hole6,holecut)
        excavator_cabin_points= [
            [0,1.5,0],
            [0,2,0],
            [0.5,2,0],
            [0.5,2.5,0],
            [1,2.5,0],
            [1,2,0],
            [2,2,0],
            [2,1.5,0],
        ]
        excavator_window_points=[
            [0,2,0],
            [0.5,2,0],
            [0.5,2.5,0],
        ]
        excavator_tread_points= [
            [0,0,0],
            [0,0.5,0],
            [1,0.5,0],
            [1,0,0],
            [3,0,0],
            [3.33,-0.33,0],
            [3.33,-0.66,0],
            [3,-1,0],
            [-1,-1,0],
            [-1.33,-0.66,0],
            [-1.33,-0.33,0],
            [-1,0,0],
        ]
        excavator_arm_points=[
            [0,0,0],
            [0,1,0],
            [2.5,1,0],
            [2.5,0,0],
        ]
        excavator_scoop_points=[
            [0,0,0],
            [-1,-1,0],
            [0,-3,0],
            [2,-3,0],
            [3,-2,0],
            
        ]
        excavator_cabin=Polygon(*excavator_cabin_points,fill_color=ManimColor.from_hex('#ffc400'),stroke_color=ManimColor.from_hex('#ffffff'),fill_opacity=1)
        excavator_window=Polygon(*excavator_window_points,color=BLUE_C,fill_opacity=1,stroke_color='#ffffff')
        excavator_base=Group(excavator_cabin,excavator_window).move_to([3.5,2.5,0]).scale(0.5)
        excavator_tread=Polygon(*excavator_tread_points,fill_color=ManimColor.from_hex('#2c2a27'),stroke_color=ManimColor.from_hex('#ffffff'),fill_opacity=1).scale(0.3).next_to(excavator_base,DOWN,0)
        excavator_arm_base=Polygon(*excavator_arm_points,fill_color=ManimColor.from_hex('#ffc400'),fill_opacity=1,stroke_color=ManimColor.from_hex('#ffffff'))
        arm_joint=Circle(radius=0.6,stroke_color='#ffffff').set_fill('#ffc400',opacity=1).next_to(excavator_arm_base,LEFT,buff=-0.5)
        scoop_joint=Circle(radius=0.4,stroke_color='#ffffff').set_fill('#6f6f6e',opacity=1)
        excavator_arm_1=Group(excavator_arm_base,arm_joint).scale(0.25).move_to([3.1,2.75,0])
        excavator_arm_2=excavator_arm_1.copy().move_to([2.6,2.8,0])
        excavator_arm_1.rotate(PI*280/360)
        excavator_arm_2.rotate(PI*435/360)
        excavator_scoop_base=Polygon(*excavator_scoop_points, fill_color=ManimColor.from_hex('#6f6f6e'), stroke_color=ManimColor.from_hex('#ffffff'),fill_opacity=1).scale(0.4).align_to(scoop_joint,UP).align_to(scoop_joint,LEFT)
        excavator_scoop=Group(excavator_scoop_base,scoop_joint).scale(0.4).move_to([2.5,2.5,0])
        self.play(Create(excavator_arm_1),Create(excavator_arm_2),Create(excavator_scoop),Create(excavator_base),Create(excavator_tread),Create(pit))
        #self.wait(5)
        truck_head_points= [
            [2, 1, 0],
            [2, 2, 0],
            [3, 4, 0],
            [5, 4, 0],
            [5, 1, 0]
        ]
        truck_window_points=[
            [2.5, 3, 0],
            [3.5, 3, 0],
            [3.5, 2, 0],
            [2, 2, 0]
        ]
        truck_head = Polygon(*truck_head_points, color=LIGHT_GRAY, fill_opacity=1)
        truck_window = Polygon(*truck_window_points, color=BLUE_C, fill_opacity=1)
        trailer = Rectangle(WHITE, 3, 4, fill_opacity=1).next_to(truck_head, buff=0)
        truck_body = Group(truck_head, truck_window, trailer).scale(0.3).move_to([0,0,0]).flip(Y_AXIS)
        truck_back = Rectangle(WHITE, 3, 0.2, fill_opacity=1).scale(0.3).next_to(truck_body,LEFT,0)
        basewheel = Circle(1, GRAY, fill_opacity=1).scale(0.18)
        wheel1 = basewheel.copy().set_x(basewheel.get_x() - 0.85)
        wheel2 = basewheel.copy().set_x(basewheel.get_x() + 0.75)
        wheel3 = basewheel.copy().next_to(wheel1, RIGHT, 0.05)
        wheels = Group(wheel1, wheel2, wheel3).next_to(truck_body, DOWN, -0.05)
        truck = Group(truck_body, truck_back)
        fulltruck = Group(truck, wheels)
        self.add(wheels)
        self.add(truck)
        self.wait(3)
        self.play(Rotate(truck_back, 0.5*PI, Z_AXIS, truck_back.get_corner(DR)))
        self.play(AnimationGroup(*[fulltruck.animate.move_to([10, 0, 0])]))
class sorting(Scene):
    def construct(self):
        conveyerbelt1 = RoundedRectangle(corner_radius=0.15, height=0.3, width=3).set_x(-1).set_y(-1)
        cbw1 = Circle(radius=0.13, stroke_width=3).set_x(-2.355).set_y(-1)
        cbw2 = cbw1.copy().next_to(cbw1, RIGHT, buff=0)
        cbw3 = cbw2.copy().next_to(cbw2, RIGHT, buff=0) 
        cbw4 = cbw3.copy().next_to(cbw3, RIGHT, buff=0)
        cbw5 = cbw4.copy().next_to(cbw4, RIGHT, buff=0)
        cbw6 = cbw5.copy().next_to(cbw5, RIGHT, buff=0)
        cbw7 = cbw6.copy().next_to(cbw6, RIGHT, buff=0)
        cbw8 = cbw7.copy().next_to(cbw7, RIGHT, buff=0)
        cbw9 = cbw8.copy().next_to(cbw8, RIGHT, buff=0)
        cbw10 = cbw9.copy().next_to(cbw9, RIGHT, buff=0)
        cbw11 = cbw10.copy().next_to(cbw10, RIGHT, buff=0)
        conveyer1 = Group(conveyerbelt1, cbw1, cbw2, cbw3, cbw4, cbw5, cbw6, cbw7, cbw8, cbw9, cbw10, cbw11)
        self.add(conveyer1)
        self.wait(4)
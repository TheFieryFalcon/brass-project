from manim import *
import math
# manim -pql [file] [method]
def fade_out(scene: Scene):
    animations = []
    for mobject in scene.get_top_level_mobjects():
        animations.append(FadeOut(mobject))
    scene.play(*animations)
class main(Scene):
    def construct(self):
        scene_order = [crucible, ziggurat, stainless_steel_skyscraper, bighole, sorting, comminution, flotation, smelting, oxidizing, refining, alloying, annealing]
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
        skyscraper_body = Polygon(*skyscraper_points, fill_color=ManimColor.from_hex('#CED2D7'), fill_opacity=0.75)
        self.play(ReplacementTransform(stainless_pipe, skyscraper_body), FadeOut(sp2, sp3, sp4, sp5, sp6, sp7, sp8, sp9, text2))
        self.add(fullwindowarray)
        self.wait(2)
        self.remove(fullwindowarray)
class bighole(Scene):
    def construct(self):
        from shared import fulltruck
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
        excavator_arm_base1=Polygon(*excavator_arm_points,fill_color=ManimColor.from_hex('#ffc400'),fill_opacity=1,stroke_color=ManimColor.from_hex('#ffffff'))
        excavator_arm_base2=Polygon(*excavator_arm_points,fill_color=ManimColor.from_hex('#ffc400'),fill_opacity=1,stroke_color=ManimColor.from_hex('#ffffff'))
        arm_joint1=Circle(radius=0.6,stroke_color='#ffffff').set_fill('#ffc400',opacity=1).next_to(excavator_arm_base1,RIGHT,buff=-0.5)
        arm_joint2=Circle(radius=0.6,stroke_color='#ffffff').set_fill('#ffc400',opacity=1).next_to(excavator_arm_base2,RIGHT,buff=-0.5)
        scoop_joint=Circle(radius=0.4,stroke_color='#ffffff').set_fill('#6f6f6e',opacity=1)
        excavator_arm_1=Group(excavator_arm_base1,arm_joint1).scale(0.25).move_to([3.1,2.7,0])
        excavator_arm_2=Group(excavator_arm_base2,arm_joint2).scale(0.25).move_to([2.6,2.7,0])
        Arm1Originx,Arm1Originy=3.4,2.7#Arm 1 pivot point
        Arm2Originx,Arm2Originy=2.9,2.7
        
        excavator_scoop_base=Polygon(*excavator_scoop_points, fill_color=ManimColor.from_hex('#6f6f6e'), stroke_color=ManimColor.from_hex('#ffffff'),fill_opacity=1).scale(0.4).align_to(scoop_joint,UP).align_to(scoop_joint,LEFT)
        excavator_scoop=Group(excavator_scoop_base,scoop_joint).scale(0.4).move_to([2.5,2.65,0]).rotate(20*PI/180)
        excavator_arm_1.rotate(-45*PI/180,about_point=([Arm1Originx,Arm1Originy,0]))
        excavator_arm_2.rotate(-45*PI/180,about_point=([Arm1Originx,Arm1Originy,0]))
        excavator_scoop.rotate(-45*PI/180,about_point=([Arm1Originx,Arm1Originy,0]))
        excavator_arm_2.rotate(45*PI/180,about_point=([3.1*math.cos(-45*PI/180),3.1*math.sin(-45*PI/180),0]))
        excavator_scoop.rotate(45*PI/180,about_point=([3.1*math.cos(-45*PI/180),2.1*math.sin(-45*PI/180),0]))
        
        self.play(Create(excavator_arm_1),Create(excavator_arm_2),Create(excavator_scoop),Create(excavator_base),Create(excavator_tread))
        self.add(pit)
        
        self.play(Rotate(excavator_arm_1,angle=45*PI/180,about_point=([Arm1Originx,Arm1Originy,0])),Rotate(excavator_arm_2,angle=45*PI/180,about_point=([Arm1Originx,Arm1Originy,0])),Rotate(excavator_scoop,angle=45*PI/180,about_point=([Arm1Originx,Arm1Originy,0])))#Arm 1 pivot point is (3.4,2.7,0)
        
        #self.wait(5)
        self.add(fulltruck)
        self.wait(3)
        self.play(AnimationGroup(*[fulltruck.animate.move_to([10, 0, 0])]))
class sorting(Scene):
    def construct(self):
        from shared import fulltruck, conveyora, truck_back, ore_points, ccolor
        fulltruck.set_x(-10).set_y(-0.7)
        sorter = Square(2, color='#FFFFFF', fill_opacity=0.2, stroke_width=6).next_to(conveyora, RIGHT, 0.1)
        conveyor1 = conveyora.copy().next_to(sorter, RIGHT, 0.1).set_y(0)
        conveyor2 = conveyor1.copy().set_y(-1)
        conveyor3 = conveyor2.copy().set_y(-2)

        ore0 = Polygon(*ore_points, color=ccolor, fill_opacity=0.6).scale(0.03)
        ore1 = ore0.copy().set_color('#EFBF04')
        ore2 = ore1.copy().set_color('#0BDA51')
        oredict = {
            0 : ore0,
            1 : ore1,
            2 : ore2
        }
        pathastart = [-2.5, -0.7,0]
        pathaend = [0.5, -0.7,0]
        path1start = [2.7, 0.3,0]
        path2start = [2.7, -0.7,0]
        path3start = [2.7, -1.7,0]
        path1end = [5.7, 0.3,0]
        path2end = [5.7, -0.7,0]
        path3end = [5.7, -1.7,0]
        fpath1 = VMobject().set_points_as_corners([pathastart, pathaend, path1start, path1end])
        fpath2 = VMobject().set_points_as_corners([pathastart, pathaend, path2start, path2end])
        fpath3 = VMobject().set_points_as_corners([pathastart, pathaend, path3start, path3end])
        pathdict = {
            0 : fpath1,
            1 : fpath2,
            2 : fpath3
        }
        pathanims = []
        for i in range(18):
            index = i % 3
            if i > 2:
                oredict[i] = oredict[index].copy()
            pathanims.append(Create(oredict[i], run_time=0.1))
            pathanims.append(MoveAlongPath(oredict[i], pathdict[index], run_time=1, rate_func=rate_functions.linear))
            #print(f'Number of points for ore number {i}: {len(oredict[i].get_all_points())}')
            #print(f'Number of points for path number {index}: {len(pathdict[index].get_all_points())}')
        self.add(conveyora, conveyor1, conveyor2, conveyor3, sorter)
        self.play(AnimationGroup(*[fulltruck.animate.move_to([-5, 0, 0])]))
        self.play(fulltruck.animate.flip(Y_AXIS))
        self.play(Rotate(truck_back, -0.5*PI, Z_AXIS, truck_back.get_corner(DL)))
        #debug only
        #for anim in pathanims:
        #    print(f"Playing animation {anim}")
        #   self.play(anim)
        self.play(LaggedStart(*pathanims, lag_ratio=0.05, run_time=5))
class comminution(Scene):
    #ID: 06 (see doc for more info)
    def construct(self):
        from shared import conveyora, ore_points, chalcopyriteslurry, slurry_vupdater, ccolor
        generic_trapezoid = [[-1,1,0], [1,1,0], [2,-1,0], [-2,-1,0]]
        funnel = Polygon(*generic_trapezoid, color=WHITE, fill_opacity=0.7).stretch(0.5, 1).flip(X_AXIS)
        conveyor1 = conveyora.copy().scale(1.5).next_to(funnel, UL, 0.5)
        conveyor1.rotate(135, Z_AXIS)
        conveyor2 = conveyora.copy().set_y(-3.2).set_x(0)
        conveyor3 = conveyor2.copy().set_x(3)
        conveyor4 = conveyor2.copy().set_x(6)
        conveyor5 = conveyor2.copy().set_x(9)
        grinder = Rectangle(fill_opacity=1, color=GRAY).next_to(funnel, DOWN, 0)
        ore0 = Polygon(*ore_points, color=ccolor, fill_opacity=1).scale(0.1)
        oredict = {0: ore0}
        slurrydict = []
        # debugpoint1 = Circle(0.05, YELLOW).move_to([0, 0, 0])
        path = VMobject().set_points_as_corners([[-6.8, 2.1, 0], [-2.6,1.8,0], [-2, 1, 0], [0, 0, 0]])
        sequence = []
        for i in range(6):
            if (i > 0):
                oredict[i] = oredict[0].copy()
            slurrydict.append(chalcopyriteslurry.copy().move_to([0, -1, 0]))
            slurrydict[i].add_updater(slurry_vupdater(-3, slurrydict[i]))    
            sequence.append(Succession(Create(oredict[i], runtime=0.1), MoveAlongPath(oredict[i], path, runtime=2, rate_func=rate_functions.linear), FadeOut(oredict[i], runtime=0.1)))
        self.add(grinder, funnel, conveyor1, conveyor2, conveyor3, conveyor4, conveyor5)
        self.play(LaggedStart(*sequence, lag_ratio=0.20, runtime=5))
        for obj in slurrydict:
            self.add(obj)
            self.bring_to_front(grinder)
        self.wait(1)
class flotation(Scene):
    #ID: 07 (see doc for more info)
    #01 - Container + Water
    #02 - Agitator, Slurry, and Stirring
    def construct(self):
        print('todo')
class smelting(Scene):
    #ID: 08 (see doc for more info)
    #01 - The flash furnace
    #02 - Literally everything else
    def construct(self):    
        print('todo')
class oxidizing(Scene):
    #ID: 09 (see doc for more info)
    #The machine is called a 'Peirce-Smith Converter'
    def construct(self):
        print('todo')
class refining(Scene):
    #ID: 10 (see doc for more info)
    #01 - Anode Furnace
    #02 - Anode Casting Wheel
    #03 - Electrowinning (known as IsaKidd Technology for copper)
    def construct(self):
        print('todo')
class alloying(Scene):
    #ID: 11 (see doc for more info)
    #01: Alloyer (just reuse the flash furnace tbh)
    #02: Casting (we will use ingot casting because it's easier to animate)
    def construct(self):
        print('todo')
class annealing(Scene):
    #ID: 12 (see doc for more info)
    def construct(self):
        print('todo')


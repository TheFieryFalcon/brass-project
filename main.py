from manim import *
import numpy
# manim -pql [file] [method]
def fade_out(scene: Scene):
    animations = []
    for mobject in scene.get_top_level_mobjects():
        animations.append(FadeOut(mobject))
    scene.play(*animations)
class main(Scene):
    def construct(self):
        scene_order = [crucible, ziggurat, stainless_steel_skyscraper, bighole, sorting, comminution, flotation, smelting, oxidizing, refining, electrorefining, alloying, annealing]
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
        stainless_pipe = Circle(radius=0.6, stroke_color=ManimColor.from_hex('#b4bdc7'), fill_opacity=0, stroke_width=10)
        sp2 = stainless_pipe.copy().next_to(stainless_pipe, DR, 0)
        sp3 = sp2.copy().next_to(sp2, LEFT, 0)
        sp4 = sp3.copy().next_to(sp3, LEFT, 0)
        sp5 = sp2.copy().next_to(sp2, DR, 0)
        sp6 = sp2.copy().next_to(sp2, DOWN, 0)
        sp7 = sp2.copy().next_to(sp2, DL, 0)
        sp8 = sp2.copy().next_to(sp4, DOWN, 0)
        sp9 = sp2.copy().next_to(sp4, DL, 0)
        spall = Group(stainless_pipe, sp2, sp3, sp4, sp5, sp6, sp7, sp8, sp9)
        # text will be added in post due to Manim's extremely janky rendering
        #text2 = Text("Stainless Steel: In 1796, chromium was discovered and found to have\n anti-oxidant properties when added to metals. It was\n used throughout the 19th century, but the modern stainless\n steel was invented by Harry Brearley in 1913 and greatly aided\n the Allies in fighting World War I. Today, it is used in pretty much everything.", 0.5, 0.05, ManimColor.from_hex("#A7C7E7"), line_spacing=1.5).set_x(2).set_y(3).scale(0.25)
        self.play(Create(spall))
        skyscraper_body = Polygon(*skyscraper_points, fill_color=ManimColor.from_hex('#CED2D7'), fill_opacity=0.75)
        self.play(ReplacementTransform(stainless_pipe, skyscraper_body), FadeOut(sp2, sp3, sp4, sp5, sp6, sp7, sp8, sp9))
        self.add(fullwindowarray)
        self.wait(4)
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
        arm_joint1=Circle(radius=0.6,stroke_color='#ffffff').set_fill('#ffc400',opacity=1).next_to(excavator_arm_base1,LEFT,buff=-0.5)
        arm_joint2=Circle(radius=0.6,stroke_color='#ffffff').set_fill('#ffc400',opacity=1).next_to(excavator_arm_base2,LEFT,buff=-0.5)
        scoop_joint=Circle(radius=0.4,stroke_color='#ffffff').set_fill('#6f6f6e',opacity=1)
        excavator_arm_1=Group(excavator_arm_base1,arm_joint1).scale(0.25).move_to([3.1,2.7,0])
        excavator_arm_2=Group(excavator_arm_base2,arm_joint2).scale(0.25).move_to([2.7,2.8,0])     
        excavator_scoop_base=Polygon(*excavator_scoop_points, fill_color=ManimColor.from_hex('#6f6f6e'), stroke_color=ManimColor.from_hex('#ffffff'),fill_opacity=1).scale(0.4).align_to(scoop_joint,UP).align_to(scoop_joint,LEFT)
        excavator_scoop=Group(excavator_scoop_base,scoop_joint).scale(0.4).move_to([2.55,2.5,0]).rotate(20*PI/180)
        excavator_arm_1.rotate(135*PI/180)
        excavator_arm_2.rotate(225*PI/180)
        excavator_scoop.rotate(315*PI/180)
        
        self.play(Create(excavator_arm_1),Create(excavator_arm_2),Create(excavator_scoop),Create(excavator_base),Create(excavator_tread))
        self.add(pit)       
        #self.wait(5)
        self.add(fulltruck)
        #self.wait(3)
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
        path = VMobject().set_points_as_corners([[-6.8, 2.1, 0], [-2.6,1.8,0], [-2, 1, 0], [0, 0, 0]])
        sequence = []
        for i in range(6):
            if (i > 0):
                oredict[i] = oredict[0].copy()
            slurrydict.append(chalcopyriteslurry.copy().move_to([0, -1, 0]))
            if i % 2 == 1:
                slurrydict[i].set_color('#262112')
            slurrydict[i].add_updater(slurry_vupdater(-3, True, slurrydict[i]))    
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
        from shared import chalcopyriteslurry, slurry_hupdater, conveyora
        flotation_points = [
            [4,-3,0],
            [3,-3,0],
            [3,0,0],
            [0,0,0],
            [0,-3,0],
            [-1,-3,0],
            [-1,-4,0],
            [0,-4,0],
            [0,-5,0],
            [3,-5,0],
            [3,-4,0],
            [4,-4,0],
        ]
        agitate_points = [
            [0,0,0],
            [-1,0,0],
            [-1,-0.5,0],
            [1,-0.5,0],
            [1,0,0],
            [0,0,0],
            [0,0,1],
            [0,-0.5,1],
            [0,-0.5,-1],
            [0,0,-1],
            [0,0,0],
            [0,4,0],
        ]
        hmoving_copper_slurry = chalcopyriteslurry.copy()
        hmoving_gangue_slurry = chalcopyriteslurry.copy().set_color('#262112')
        flotation=Polygon(*flotation_points,stroke_color='#a2aab7').move_to([0,0.5,0])
        agitator=Polygon(*agitate_points,stroke_color="#384650").move_to([0,0.5,0]) 
        water=Rectangle(height=4.5,width=3).move_to([0,0.25,0]).set_color("#558cdf",opacity=1)
        conveyor1=conveyora.copy().scale(1.75).move_to([-5,-1,0])
        conveyor2=conveyor1.copy().move_to([5,-1,0])
        self.play(Create(water),Create(flotation),Create(agitator),Create(conveyor1),Create(conveyor2))
        self.add(hmoving_copper_slurry, hmoving_gangue_slurry)
        hmoving_copper_slurry.add_updater(slurry_hupdater([-5, -0.7, 0], 0.3, 0.2, 1.5, 2.5, hmoving_copper_slurry)) # feel free to tweak parameters as needed, definitions are in shared.py
        hmoving_gangue_slurry.add_updater(slurry_hupdater([-5, -0.7, 0], 0.3, 0.2, 10, -0.5, hmoving_gangue_slurry))
        #print(hmoving_copper_slurry.get_updaters())
        #print(hmoving_gangue_slurry.get_updaters())
        self.play(Rotate(agitator,axis=[0,1,0],angle=720*PI/180,run_time=5, rate_func=rate_functions.ease_in_quad))
class smelting(Scene):
    #ID: 08 (see doc for more info)
    #01 - The flash furnace
    #02 - Input, oxygen tank, some sort of visualization of oxygen flow, slag separation (ideally of a different color than below)
    def construct(self):
        from shared import chalcopyriteslurry, slurry_vupdater
        furnace_ex_points=[
            [0,3,0],
            [0,0,0],
            [3,0,0],
            [3,2.75,0],
            [3.25,3,0]
        ]
        furnaceex=Polygon(*furnace_ex_points,fill_color="#8e8e8e",stroke_color="#4f4f4f",stroke_width=30).move_to([0,-1,0])
        furnaceint1=Rectangle(width=2.75,height=0.01).move_to([-0.1,-2.4,0]).set_color("#b82500",1)
        furnaceint2=Rectangle(width=2.65,height=2.5).move_to([-0.12,-1.1,0]).set_color("#b82500",1)
        smelts=chalcopyriteslurry.copy().scale(0.8).add_updater(slurry_vupdater(-2.5, False, chalcopyriteslurry)).move_to([0, 10, 0])
        Tank=RoundedRectangle(height=2.5,width=1,corner_radius=0.5).move_to([-2.5,-1.5,0]).set_color("#969998",1)
        Pipe=Rectangle(width=1,height=0.5).move_to([-2,-2.5,0]).set_color("#969998",1)
        Pipe2=Pipe.copy().move_to([-3,-0.5,0])
        FurnFuel=Group(Tank,Pipe,Pipe2).move_to([-2.5,-1.3,0])
        self.add(furnaceint1, FurnFuel,smelts,furnaceex)
        self.wait(1.8)
        #self.play(MoveAlongPath()) make heat waves if you'd like but imma move on & finish this later (Priority:Low)
        self.play(Transform(furnaceint1,furnaceint2,run_time=2))        
        self.play(FadeToColor(furnaceint2,color="#e97705"))
        self.play(FadeToColor(furnaceint2,color="#ffd711"))
        self.play(FadeToColor(furnaceint2,color="#ffffff"))
class oxidizing(Scene):
    #ID: 09 (see doc for more info)
    #The machine is called a 'Peirce-Smith Converter'
    def construct(self):
        from shared import ccolor, cucolor
        psconv_points = [
            [-4.7, 1.7, 0],
            [-4.1, 1.7, 0],
            [-4.1, 1.6, 0],
            [-0.2, 1.6, 0],
            [-0.2, 1.7, 0],
            [0.1, 1.7, 0],
            [0.9, 1.2, 0],
            [0.9, 0.2, 0],
            [0.1, -0.3, 0],
            [-4.7, -0.3, 0] 
        ]
        psconv_foot_points = [
            [-4.325, -0.3, 0],
            [-4.175, -0.3, 0],
            [-4.175, -0.5, 0],
            [-4.0, -0.5, 0],
            [-4.0, -0.9, 0],
            [-4.5, -0.9, 0],
            [-4.5, -0.5, 0],
            [-4.325, -0.5, 0]
        ]
        psconv_hull = Polygon(*psconv_points, fill_opacity=0.8)
        foot = Polygon(*psconv_foot_points, fill_opacity=1)
        foot2 = foot.copy().set_x(-2.2)
        foot3 = foot.copy().set_x(-0.2)
        psconv = Group(psconv_hull, foot, foot2, foot3).set_color('#6e6d6b')
        psconv_basic_lining = Rectangle(width=4, height=1.5, color='#7d7757', fill_opacity=0.8).move_to([psconv.get_x()-0.3, psconv.get_y()+0.3, 0])
        psconv_interior = Rectangle(width=3, height=1, fill_opacity=0.8).move_to([psconv.get_x()-0.3, psconv.get_y()+0.3, 0])
        copper_slag = Rectangle(width=3, height=0.15, fill_opacity=1, color=ccolor).move_to([psconv.get_x()-0.3, psconv.get_y()+0.05, 0])
        copper_blister = Rectangle(width=3, height=0.35, fill_opacity=1, color=ccolor).move_to([psconv.get_x()-0.3, psconv.get_y()-0.2, 0])
        tuyere = Cylinder(0.15, 2, X_AXIS, color=WHITE, fill_color=WHITE, fill_opacity=0.8, checkerboard_colors=False, stroke_width=0, v_resolution=30).move_to([psconv.get_x()-2.5, psconv.get_y(), 0])
        tuyere2 = tuyere.copy().set_y(psconv.get_y()+0.5)
        self.play(Create(psconv))
        self.add(tuyere, tuyere2, psconv, psconv_basic_lining, psconv_interior, copper_slag, copper_blister)
        self.play(FadeToColor(copper_slag, '#5e574e', run_time=4), FadeToColor(copper_blister, cucolor, run_time=4))
class refining(Scene):
    #ID: 10 (see doc for more info)
    #02 - Anode Casting Wheel
    #03 - Electrowinning (known as IsaKidd Technology for copper) (split into another scene)
    def construct(self):
        from shared import cucolor
        acwheel_base = Circle(2.2, color=GRAY, fill_opacity=1).set_x(-4)
        acwheel_gsquare = Rectangle(LIGHT_GRAY, 0.7, 0.5, fill_opacity=1)
        nrect = 14
        dist = 1.7
        acwheel_indents = VGroup()
        #acwheel_sindents = VGroup()
        pipe = Rectangle(WHITE, 0.5, 5, fill_color=GRAY_A, fill_opacity=1)
        cutter1 = Rectangle(WHITE, 0.4, 5).move_to([pipe.get_x()-0.3, pipe.get_y(), pipe.get_z()])
        pipeoutline = Difference(pipe, cutter1, color=WHITE, fill_opacity=1)
        fullpipe = VGroup(pipe, pipeoutline).rotate(1/14*PI).set_y(1)
        pipepath = Line(pipe.get_right(), pipe.get_left()).rotate(1/14*PI).set_y(1)
        #ingot = Rectangle(cucolor, 0.4, 0.5, fill_opacity=1).rotate(1/14*PI).move_to(fullpipe.get_center())
        #anims = []
        for i in range(nrect):
            theta = (i/nrect)*2*PI
            irect = acwheel_gsquare.copy().move_to(acwheel_base.get_center()).set_y(dist)
            irect.rotate(theta + 11/7*PI, Z_AXIS, acwheel_base.get_center())
            acwheel_indents.add(irect)
            #acwheel_sindents.add(irect)
        # old code (really terrible and caused MANY undiagnosable bugs)
        #for i in range(nrect):
            #iingot = ingot.copy()
            #srect = acwheel_sindents[i].copy().set_color(cucolor)
            #anims.append(Create(iingot))
            #anims.append(MoveAlongPath(iingot, pipepath))
            #anims.append(ReplacementTransform(iingot, srect))
            #anims.append(ApplyMethod(acwheel_sindents.remove, acwheel_indents[i], run_time=0))
            #anims.append(ApplyMethod(acwheel_sindents.remove, srect, run_time=0))
            #anims.append(ApplyMethod(acwheel_sindents.add, iingot, run_time=0))
            #anims.append(ApplyMethod(acwheel_indents.remove, acwheel_indents[i], run_time=0))
            #anims.append(FadeOut(iingot, run_time=0))
            #anims.append(Rotate(acwheel_sindents, 1/7*PI, about_point=acwheel_base.get_center(), rate_func=rate_functions.linear))
        acwheel_base.set_x(acwheel_indents.get_x()-0.06) # no clue why I have to do this
        self.add(acwheel_base, acwheel_indents, fullpipe)
        #for i in acwheel_sindents:
        #    print(i.get_color())
        #print ("________________THIS IS A DIFFERENT LIST_____________________")
        #print(f"LENGTH OF SINDENTS (INIT): {len(acwheel_sindents)}")
        #print ("________________THIS IS A DIFFERENT LIST_____________________")
        #for i in acwheel_indents:
        #    print(i.get_color())
        #print ("________________THIS IS A DIFFERENT LIST_____________________")
        #print(f"LENGTH OF INDENTS (INIT): {len(acwheel_indents)}")
        #self.wait(1)
        # for i in acwheel_sindents:
        #     print(i.get_color())
        # print ("________________THIS IS A DIFFERENT LIST_____________________")
        # print(f"LENGTH OF SINDENTS (BEFORE): {len(acwheel_sindents)}")
        # print ("________________THIS IS A DIFFERENT LIST_____________________")
        # for i in acwheel_indents:
        #     print(i.get_color())
        # print ("________________THIS IS A DIFFERENT LIST_____________________")
        # print(f"LENGTH OF INDENTS (BEFORE): {len(acwheel_indents)}")
        # print ("________________THIS IS A DIFFERENT LIST_____________________")
        #self.play(Succession(*anims, run_time=20))

        # migrate to just a LOT of self.play calls (much worse practice but much easier to work with because I don't need lag ratio)
        # I can probably just speed this up in post
        for i in range(nrect):
            iingot = Rectangle(cucolor, 0.4, 0.5, fill_opacity=1)
            iingot.rotate(1/14*PI).move_to(pipepath.get_start())
            self.add(iingot)
            self.play(MoveAlongPath(iingot, pipepath))
            self.play(ReplacementTransform(acwheel_indents[i], acwheel_indents[i].copy().set_color(cucolor)), FadeOut(iingot))
            self.play(Rotate(acwheel_indents, -1/7*PI, about_point=acwheel_base.get_center(), rate_func=rate_functions.linear))
class electrorefining(Scene):
    def construct(self):
        from shared import cucolor, crucible_points
        nfins = 20
        starter_base = Rectangle(YELLOW, 1, 4, stroke_width=20)
        cutter1 = starter_base.copy().set_y(-0.55).set_color(BLUE)
        crane = Difference(starter_base, cutter1, color=YELLOW, fill_opacity=0.5)
        genfin = Rectangle(cucolor, 2, 0.05, fill_opacity=1).set_y(-0.55).set_x(-1.9)
        tub = Polygon(*crucible_points, color=WHITE, fill_opacity=1).scale(0.5).stretch(2, 0).set_y(-3)
        solvent = Rectangle(ManimColor('#141ad9', 0.4), 2, 4, fill_opacity=0.8, opacity=0.4).set_y(-3)
        fins = VGroup()
        mgroup = VGroup(crane)
        cgroup = VGroup(solvent, tub)
        path1 = Line(crane.get_center(), solvent.get_center())
        path2 = Line(solvent.get_center(), [crane.get_x() - 4, crane.get_y() + 1, 0])
        path3 = VMobject().set_points_as_corners(points=[[crane.get_x() - 4, crane.get_y(), 0], crane.get_center(), solvent.get_center()])
        cheatingpath = Line(solvent.get_center(), [solvent.get_x() - 0.075, solvent.get_y(), 0])
        for i in range(nfins):
            ifin = genfin.copy()
            fins.add(ifin)
        fins.arrange(buff=0.15).set_y(-0.55)
        anode_fins = fins.copy().set_x(fins.get_x()-4).set_y(fins.get_y()+1).set_color("#8e5f30")
        self.add(crane, solvent, fins, anode_fins, tub)
        mgroup.add(fins)
        self.wait(1)
        self.play(MoveAlongPath(mgroup, path1, rate_func=rate_functions.ease_in_out_quad))
        mgroup.remove(fins)
        self.add(solvent, fins, tub)
        cgroup.add(fins)
        self.play(MoveAlongPath(mgroup, path2, rate_func=rate_functions.ease_in_out_quad), MoveAlongPath(cgroup, cheatingpath))
        mgroup.add(anode_fins)
        self.play(MoveAlongPath(mgroup, path3, rate_func=rate_functions.ease_in_out_quad), run_time=2)
        mgroup.remove(anode_fins)
        self.add(solvent, fins, anode_fins, tub)
        self.play(crane.animate.set_y(0))
        self.wait(3)
class alloying(Scene):
    #ID: 11 (see doc for more info)
    #01: Alloyer (just reuse the flash furnace tbh)
    #02: Continuous Casting Apparatus
    #03: Animation
    def construct(self):
        from shared import crucible_points
        Alloy_pourer_points=[
            [0,2,0],
            [1,2,0],
            [1,0,0],
            [1+pow(2,0.5),pow(2,0.5),0],
            [1+pow(2,0.5)+pow(0.5,0.5),pow(2,0.5)-pow(0.5,0.5),0],
            [1+pow(0.5,0.5),-pow(0.5,0.5),0],
            [3+pow(0.5,0.5),-pow(0.5,0.5),0],
            [3+pow(0.5,0.5),-1-pow(0.5,0.5),0],
            [1+pow(0.5,0.5),-1-pow(0.5,0.5),0],
            [1+pow(2,0.5)+pow(0.5,0.5),-1-pow(2,0.5)-pow(0.5,0.5),0],
            [1+pow(2,0.5),-1-pow(2,0.5)-2*pow(0.5,0.5),0],
            [1,-1-2*pow(0.5,0.5),0],
            [1,-3-2*pow(0.5,0.5),0],
            [0,-3-2*pow(0.5,0.5),0],
            [0,-1-2*pow(0.5,0.5),0],
            [-pow(2,0.5),-1-2*pow(0.5,0.5)-pow(2,0.5),0],
            [-pow(2,0.5)-pow(0.5,0.5),-1-pow(0.5,0.5)-pow(2,0.5),0],
            [-pow(0.5,0.5),-1-pow(0.5,0.5),0],
            [-2-pow(0.5,0.5),-1-pow(0.5,0.5),0],
            [-2-pow(0.5,0.5),-pow(0.5,0.5),0],
            [-pow(0.5,0.5),-pow(0.5,0.5),0],
            [-pow(2,0.5)-pow(0.5,0.5),-pow(0.5,0.5)+pow(2,0.5),0],
            [-pow(2,0.5),pow(2,0.5),0],
            [0,0,0],
        ]
        alloyer=Polygon(*crucible_points).set_color(GREY,1).scale(0.5)
        crucible_copper=alloyer.copy().set_color(GREY,1).scale(0.5).move_to([1,0,0])
        crucible_tin=crucible_copper.copy().set_color(GREY,1).move_to([-1,0,0])
        alloy_bronze1=Rectangle(width=2,height=0.5).set_color("#ce8946",1).move_to([0,-0.75,0])
        alloy_bronze2=alloy_bronze1.copy().next_to(alloy_bronze1,UP,buff=0)
        alloy_copper=Rectangle(width=4,height=2.25).scale(0.25).move_to([1,-0.25,0]).set_color("#d37854",1)
        alloy_tin=alloy_copper.copy().move_to([-1,-0.25,0]).set_color("#d5d5d5",1)
        bronze_pour=Rectangle(width=0.25,height=0.05).move_to([0,-1.4,0]).set_fill("#ce8946",1).set_stroke("#000000")
        tin=Group(alloy_tin,crucible_tin).move_to([2.5,2,0])
        copper=Group(alloy_copper,crucible_copper).move_to([-2.5,2,0])
        Alloy_pourer=Polygon(*Alloy_pourer_points).set_fill(WHITE,1).set_stroke(DARK_GREY).scale(0.5).move_to([0,-6,0])
        Cast_Funnel=Triangle(width=3,height=1.5).rotate(angle=PI*180/180).set_fill(WHITE,1).set_stroke(DARK_GREY).move_to([0,-6,0])
        Caster=Group(Cast_Funnel,Alloy_pourer)
        self.add(bronze_pour,alloyer,tin,copper,Alloy_pourer)
        self.play(tin.animate.move_to([2.5,3,0]),copper.animate.move_to([-2.5,3,0]))
        self.play(tin.animate.move_to([1.5,3,0]),copper.animate.move_to([-1.5,3,0]))
        self.play(Rotate(tin,angle=PI*135/180),Rotate(copper,angle=PI*-135/180))
        self.play(Transform(alloy_tin,alloy_bronze1),Transform(alloy_copper,alloy_bronze2))
        alloy_bronze=Group(alloy_bronze1,alloy_bronze2)
        self.play(bronze_pour.animate.stretch_to_fit_height(6).shift(DOWN*2))
        self.play(alloyer.animate.move_to([0,6,0]),
                  crucible_copper.animate.move_to([-1.5,9,0]),
                  crucible_tin.animate.move_to([1.5,9,0]),
                  alloy_bronze.animate.move_to([0,5.25,0]),
                  alloy_tin.animate.move_to([0,5.25,0]),
                  alloy_copper.animate.move_to([0,4.75,0]),
                  bronze_pour.animate.move_to([0,2.6,0]),
                  Caster.animate.move_to([0,0,0]))
        
        self.play(Rotate(Alloy_pourer,angle=PI*360/180,run_time=6,rate_func=linear))

class annealing(Scene):
    #ID: 12 (see doc for more info)
    def construct(self):
        from shared import conveyora
        annealerpoints = [
            [3, -1.5, 0],
            [3, 1.5, 0],
            [-3, 1.5, 0],
            [-3, -1.5, 0]
        ]
        conveyor1 = conveyora.copy().set_x(-1.5).set_y(-1.34)
        conveyor2 = conveyor1.copy().set_x(1.5).set_y(-1.34)
        bronzeingotpoints = [
            [-0.2, 0.2, 0],
            [-0.25, -0.2, 0],
            [0.25, -0.2, 0],
            [0.2, 0.2, 0]
        ]
        bronzeingot = Polygon(*bronzeingotpoints, stroke_color="#CD7F32", fill_color="#CD7F32", fill_opacity=1).set_y(-1)
        bi2= bronzeingot.copy().set_x(bronzeingot.get_x()+1)
        annealingbox = Polygon(*annealerpoints, stroke_color="#999CA0", fill_color="#999CA0", fill_opacity=0.7)
        annealer = Group(annealingbox, conveyor1, conveyor2)
        annealingprocess = Group(annealer, bronzeingot, bi2)
        self.play(Create(annealingprocess,run_time=2))
        self.wait(3)


# DEBUG ONLY
#with tempconfig({"quality": "medium_quality", "disable_caching": True, "renderer": "opengl"}):
#    scene = flotation()
#    scene.render()
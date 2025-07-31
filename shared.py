# PLEASE PUT YOUR END PRODUCTS IN HERE
# If you need to use any of these, just add a "from shared import " and then the name of the thing you want

from manim import *
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
fulltruck = Group(wheels, truck)      


conveyorbelt1 = RoundedRectangle(corner_radius=0.15, height=0.3, width=3).set_x(-1).set_y(-1)
cbw1 = Circle(radius=0.13, stroke_width=3, color=GRAY).set_x(-2.355).set_y(-1)
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
conveyora = Group(conveyorbelt1, cbw1, cbw2, cbw3, cbw4, cbw5, cbw6, cbw7, cbw8, cbw9, cbw10, cbw11)

ore_points= [
    [8,10,0],
    [10,8,0],
    [9,5,0],
    [8,3,0],
    [6,0,0],
    [4,0.5,0],
    [2,0,0],
    [0,2,0],
    [0,5,0],
    [1,9,0]
]
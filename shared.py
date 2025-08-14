# PLEASE PUT YOUR END PRODUCTS IN HERE
# If you need to use any of these, just add a "from shared import " and then the name of the thing you want

from manim import *
import numpy
ccolor = ManimColor.from_hex('#b5a642') # c stands for chalcopyrite, this is the standard color we're using for all end products
cucolor = ManimColor.from_hex('#ce8946')
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

# this just makes the slurry fall one point at a time and then start moving horizontally at v after it's hit something
def slurry_vupdater(trgy, moveh, mobject:PMobject): # the : is just type annotation
    velocities = numpy.zeros(mobject.points.shape) # mobject.points.shape is a two-dimensional Nx3 matrix, this is the first derivative of that
    velocities[:, 1] = numpy.random.uniform(-0.2, -0.4, mobject.points.shape[0]) # : means "every point in this dimension"
    def actual_updater(mobject:PMobject, dt): # this is a closure; https://en.wikipedia.org/wiki/Closure_(computer_programming)
            if len(mobject.get_updaters()) > 1:
                 mobject.remove_updater(actual_updater)
            mobject.points += velocities # applies the matrix to the points
            below_floor_points = mobject.points[:, 1] < trgy # for some reason this returns the indices??? I am going insane
            velocities[below_floor_points, 1] = 0
            if (moveh == True):
                velocities[below_floor_points, 0] = 0.5
            mobject.points[below_floor_points, 1] = trgy
            
                 

    return actual_updater # god I hope this works IT WORKS WTF

# variant of the above but it only moves horizontally and then vertically until a certain point is reached after which it removes itself
# spos = starting position, vx = x velocity, vy = y velocity, trg = target
def slurry_hupdater(spos, vx, vy, trgx, trgy, mobject:PMobject):
    velocities = numpy.zeros(mobject.points.shape)
    velocities[:, 0] = numpy.random.uniform(vx/1.5, vx, mobject.points.shape[0])
    def actual_updater2(mobject:PMobject, dt): 
        if dt == 0:
            mobject.points[:, 0] = numpy.random.uniform(spos[0], spos[0] + 0.1, mobject.points.shape[0])
            mobject.points[:, 1] = numpy.random.uniform(spos[1], spos[1] + 0.1, mobject.points.shape[0])
        mobject.points += velocities
        below_floor_points = mobject.points[:, 0] > trgx
        velocities[below_floor_points, 0] = numpy.random.uniform(-0.13, 0, numpy.sum(below_floor_points))
        velocities[below_floor_points, 1] = numpy.random.uniform(vy/1.5, vy, numpy.sum(below_floor_points))
        mobject.points[below_floor_points, 0] = trgx
        above_ceiling_points = mobject.points[:, 1] > trgy # note to self: do not write code when tired
        velocities[above_ceiling_points] = [0, 0, 0]
        mobject.points[above_ceiling_points, 1] = trgy
        if above_ceiling_points.all() == mobject.points[:, 1].all():
            mobject.remove_updater(actual_updater2)

    return actual_updater2
chalcopyriteslurry = DotCloud(radius=1.5, density=15, color=ccolor)
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
     

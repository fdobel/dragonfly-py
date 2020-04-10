"""
Initialize the dragonflies population Xi (i = 1, 2, ..., n)
Initialize step vectors dXi (i = 1, 2, ..., n)
while the end condition is not satisfied
       Calculate the objective values of all dragonflies
       Update the food source and enemy
       Update w, s, a, c, f, and e
       Calculate S, A, C, F, and E using Eqs. (3.1) to (3.5) in the paper (or above the page)
       Update neighbouring radius
       if a dragonfly has at least one  neighbouring dragonfly
               Update velocity vector using Eq. (3.6) in the paper (or above the page)
               Update position vector using Eq. (3.7) in the paper (or above the page)
       else
               Update position vector using Eq. (3.8) in the paper (or above the page)
       end if
       Check and correct the new positions based on the boundaries of variables
end while
"""
from dragonfly import Dragonfly, Swarm
import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

dragonfly_population = 10
swarm = Swarm()

food_source = None
enemy_source = None

stepvectors = {}
dims = 2


class EnvSetup:
    def __init__(self, w, s, a, c, f, e):
        self.inertia_weight = w
        self.separation_weight = s
        self.alignment_weight = a
        self.cohesion_weight = c
        self.food_factor = f
        self.enemy_factor = e


setting = EnvSetup(0.5, 0.5, 0.2, 0.3, 1, 1)
food = np.array([-5, -5])
enemy = np.array([5, 5])


class ObjectiveFunction:
    def __call__(self, array):
        return sum(array)


for i in range(dragonfly_population):
    r = np.random.rand(2)
    swarm.add(Dragonfly(i, ObjectiveFunction(), r * 20 - 10, food, enemy, setting))


DISPLAY_LIMS = 10


def record_animation():
    fig = plt.figure()
    ax = plt.axes(xlim=(-DISPLAY_LIMS, DISPLAY_LIMS), ylim=(-DISPLAY_LIMS, DISPLAY_LIMS))
    line = ax.scatter([], [], marker='o')

    def init():
        line.set_offsets([])
        return line,

    def step_function(i):
        swarm.next_step(i)
        print(swarm.objective_values())
        xy = []
        for p in swarm.positions:
            xy.append([p[0], p[1]])

        xy.append(enemy)
        xy.append(food)
            # y.append(p[1])

        line.set_array(
            np.union1d(np.array(list(range(len(xy)))), np.array([240, 241]))
        )
        line.set_offsets(xy)
        return line,

    anim = FuncAnimation(fig, step_function, init_func=init, frames=500, interval=30, blit=True)

    anim.save('dragonflies.gif', writer='imagemagick')


print("Start recording...")
record_animation()
print("Finished.")

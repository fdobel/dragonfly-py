import numpy as np

class Swarm:

    INITIAL_NEIGHBOURHOOD = 0.1

    def __init__(self):
        self.__dragonflies = []

    def add(self, dragonfly):
        self.__dragonflies.append(dragonfly)

    def objective_values(self):
        return list(map(lambda d: d.objective_value(), self.__dragonflies))

    def __iter__(self):
        return self.__dragonflies.__iter__()

    @property
    def positions(self):
        return list(map(lambda d: d.X, self.__dragonflies))

    def deltas(self, neighbourhood_size):
        return list(map(lambda d: d.next_delta(self.__dragonflies, neighbourhood_size), self.__dragonflies))

    def next_step(self, iteration):
        ds = self.deltas(iteration * self.INITIAL_NEIGHBOURHOOD)
        for dragonfly, delta in zip(self.__dragonflies, ds):
            dragonfly.update(delta)


def neighbouring_dragonflies(dragonfly, dragonflies, neighbourhood_size):
    return list(
        filter(
            lambda other: other != dragonfly and dragonfly.dist(other) <= neighbourhood_size,
            dragonflies
        )
    )


class Dragonfly:

    def __eq__(self, other):
        return self.__id == other.__id

    def dist(self, other):
        return np.linalg.norm(self.__position - other.__position)

    def __init__(self, id, objective_function, initial_position, food_source, enemy_source, options, initial_step='random'):
        self.__id = id
        self.__position = initial_position
        self.__separation = None
        self.__alignment = None
        self.__cohesion = None
        self.__food_source = food_source
        self.__enemy_source = enemy_source

        self.__objective_function = objective_function

        if initial_step == 'random':
            self.__dXt = np.random.rand(initial_position.shape[0])/10
        else:
            raise NotImplementedError("Other step initialization not implemented")

        self.__options = options

    @property
    def X(self):
        return self.__position

    @property
    def dX(self):
        return self.__dXt

    def objective_value(self):
        return self.__objective_function(self.__position)

    def next_delta(self, dragonflies, neighbourhood_size):
        relevant_dragonflies = neighbouring_dragonflies(self, dragonflies, neighbourhood_size)
        ds = relevant_dragonflies
        N = len(ds)
        if N == 0:
            return np.random.rand(2) - 0.5

        S_i = - sum(self.X - D.X for D in ds)
        A_i = sum(D.dX for D in ds) / N
        C_i = A_i - self.X
        F_i = self.__food_source - self.X
        E_i = self.__enemy_source + self.X

        e = self.__options
        dX_t = (
                e.separation_weight * S_i +
                e.alignment_weight * A_i +
                e.cohesion_weight * C_i +
                e.food_factor * F_i +
                e.enemy_factor * E_i
        ) + e.inertia_weight * self.__dXt
        return dX_t

    def update(self, delta):
        self.__position = self.__position + delta
        self.__dXt = delta
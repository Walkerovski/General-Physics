from random import randint
from time import sleep

# stale fizyczne ?
ACCELERATION_X = 0
ACCELERATION_Y = 0


class Atom:
    def __init__(self, start_location_x, start_location_y, max_deviation, size, temperature):
        self.start_location_x = start_location_x
        self.start_location_y = start_location_y
        self.actual_location_x = start_location_x
        self.actual_location_y = start_location_y
        self.max_deviation = max_deviation
        self.size = size
        self.temperature = temperature
        self.velocity_x = 0
        self.velocity_y = 0

    def random_move(self, temperature):
        way = randint(1, 4) % 4
        # try move right
        if way == 0:
            if self.actual_location_x + 1 <= self.start_location_x + self.max_deviation:
                self.actual_location_x += 1
        # try to move left
        elif way == 1:
            if self.actual_location_x - 1 >= self.start_location_x - self.max_deviation:
                self.actual_location_x -= 1
        # try to move up
        elif way == 2:
            if self.actual_location_y + 1 <= self.start_location_y + self.max_deviation:
                self.actual_location_y += 1
        # try to move down
        else:
            if self.actual_location_y - 1 >= self.start_location_y - self.max_deviation:
                self.actual_location_y -= 1

    def set_dim_x(self, new_dim_x):
        self.actual_location_x = new_dim_x

    def set_dim_y(self, new_dim_y):
        self.actual_location_y = new_dim_y

    def set_max_deviation(self, new_max_deviation):
        self.max_deviation = new_max_deviation

    def set_size(self, new_size):
        self.size = new_size

    def set_temperature(self, new_temperature):
        self.temperature = new_temperature

    def set_new_velocity_x(self, new_velocity_x):
        self.velocity_x = new_velocity_x

    def set_new_velocity_y(self, new_velocity_y):
        self.velocity_y = new_velocity_y

    def get_dim_x(self):
        return self.actual_location_x

    def get_dim_y(self):
        return self.actual_location_y

    def get_max_deviation(self):
        return self.max_deviation

    def get_size(self):
        return self.size

    def get_temperature(self):
        return self.temperature

    def get_new_velocity_x(self):
        return self.velocity_x

    def get_new_velocity_y(self):
        return self.velocity_y


class Electron():
    def __init__(self, start_location_x, start_location_y, size):
        self.actual_location_x = start_location_x
        self.actual_location_y = start_location_y
        self.size = size
        self.acceleration_x = ACCELERATION_X  # do ustalenia ze wzorow
        self.acceleration_y = ACCELERATION_Y  # do ustalenia ze wzorow
        self.velocity_x = 0
        self.velocity_y = 0
        self.velocity_without_atoms = VELOCITY_WITHOUT_ATOMS  # x-owa predkosc
        #  ^ nie jest to chyba predkosc maksymalna jaka moze miec elektron

    def change_velocity_after_collision_with_atom(self, atom_velocity_x, atom_velocity_y):
        # prawo zachowania pedu ?
        pass

    def set_new_location_x(self, new_location_x):
        self.actual_location_x = new_location_x

    def set_new_location_y(self, new_location_y):
        self.actual_location_y = new_location_y

    def set_new_size(self, new_size):
        self.size = new_size

    def set_new_acceleration_x(self, new_acceleration_x):
        self.acceleration_x = new_acceleration_x

    def set_new_acceleration_y(self, new_acceleration_y):
        self.acceleration_y = new_acceleration_y

    def set_new_velocity_x(self, new_velocity_x):
        self.velocity_x = new_velocity_x

    def set_new_velocity_y(self, new_velocity_y):
        self.velocity_y = new_velocity_y

    def set_new_velocity_without_atoms(self, new_velocity_without_atoms):
        self.velocity_without_atoms = new_velocity_without_atoms

    def get_new_location_x(self):
        return self.actual_location_x

    def get_new_location_y(self):
        return self.actual_location_y

    def get_new_size(self):
        return self.size

    def get_new_acceleration_x(self):
        return self.acceleration_x

    def get_new_acceleration_y(self):
        return self.acceleration_y

    def get_new_velocity_x(self):
        return self.velocity_x

    def get_new_velocity_y(self):
        return self.velocity_y

    def get_new_velocity_without_atoms(self):
        return self.velocity_without_atoms


if __name__ == "__main__":
    atom1 = Atom(1, 1, 10, 10, 5)
    print(atom1.get_temperature())
    print(atom1.get_size())
    print(atom1.get_max_deviation())
    print(atom1.get_dim_y())
    print(atom1.get_dim_x())
    while True:
        # ruchy atomu zaleza jakos od temperatury, trzeba by to jakos wykorzystac
        atom1.random_move(atom1.get_temperature())
        print(atom1.get_dim_x(), atom1.get_dim_y())
        sleep(0.1)

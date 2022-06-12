from random import randint, gauss
from time import sleep


ACCELERATION_X = 0.1
ACCELERATION_Y = 0.1
MAX_X_VELOCITY = 1


class Atom:
    def __init__(self, start_location_x, start_location_y, max_deviation, size, temperature):
        self.start_location_x = start_location_x
        self.start_location_y = start_location_y
        self.actual_location_x = start_location_x
        self.actual_location_y = start_location_y
        self.max_deviation = max_deviation
        self.size = size
        self.temperature = temperature

    def random_move(self):
        way = randint(1, 4) % 4
        # try move right
        if way == 0:
            if self.actual_location_x + self.temperature <= self.start_location_x + self.max_deviation:
                self.actual_location_x += self.temperature
        # try to move left
        elif way == 1:
            if self.actual_location_x - self.temperature >= self.start_location_x - self.max_deviation:
                self.actual_location_x -= self.temperature
        # try to move up
        elif way == 2:
            if self.actual_location_y + self.temperature <= self.start_location_y + self.max_deviation:
                self.actual_location_y += self.temperature
        # try to move down
        else:
            if self.actual_location_y - self.temperature >= self.start_location_y - self.max_deviation:
                self.actual_location_y -= self.temperature

    def set_max_deviation(self, new_max_deviation):
        self.max_deviation = new_max_deviation

    def set_size(self, new_size):
        self.size = new_size

    def set_temperature(self, new_temperature):
        self.temperature = new_temperature

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


class Electron():
    def __init__(self, start_location_x, start_location_y, size):
        self.actual_location_x = start_location_x
        self.actual_location_y = start_location_y
        self.size = size
        self.acceleration_x = ACCELERATION_X
        self.acceleration_y = ACCELERATION_Y
        self.velocity_x = 0
        self.velocity_y = 0
        self.max_x_velocity = MAX_X_VELOCITY

    def move(self, atoms):
        self.set_new_velocity_x()
        self.set_new_velocity_y()
        self.set_new_location_x()
        self.set_new_location_y()
        self.check_collision(atoms)

    def check_collision(self, atoms):
        for a in atoms:
            if self.actual_location_x > a.get_dim_x() - 1.7 \
                and self.actual_location_x < a.get_dim_x() + 1.7:
                if self.actual_location_y > a.get_dim_y() - 1.7 \
                    and self.actual_location_y < a.get_dim_y() + 1.7:
                    self.change_velocity_after_collision_with_atom(a)

    def change_velocity_after_collision_with_atom(self, atom):
        self.velocity_x = -self.velocity_x * 0.7
        if self.actual_location_y > atom.get_dim_y() - 1.7 \
            and self.actual_location_y < atom.get_dim_y():
                self.velocity_y = -1
        else:
            self.velocity_y = 1

    def set_new_location_x(self):
        self.actual_location_x += self.velocity_x
        if self.actual_location_x > 90:
            self.actual_location_x = 0
            self.actual_location_y += gauss(0, 5)

    def set_new_location_y(self):
        self.actual_location_y += self.velocity_y
        if self.actual_location_y > 50:
            self.actual_location_y = 1
        if self.actual_location_y < 0:
            self.actual_location_y = 49

    def set_new_velocity_x(self):
        self.velocity_x += self.acceleration_x
        self.velocity_x = min(self.velocity_x, self.max_x_velocity)

    def set_new_velocity_y(self):
        if abs(self.velocity_y) < self.acceleration_y:
            self.velocity_y = 0 
        elif self.velocity_y > 0:
            self.velocity_y -= self.acceleration_y
        else:
            self.velocity_y += self.acceleration_y

    def get_location_x(self):
        return self.actual_location_x

    def get_location_y(self):
        return self.actual_location_y
    
    def get_size(self):
        return self.size

    def get_velocity_x(self):
        return self.velocity_x

    def get_velocity_y(self):
        return self.velocity_y
    
    def get_max_x_velocity(self):
        return self.max_x_velocity



if __name__ == "__main__":
    atom1 = Atom(1, 1, 2, 50, 0.1)
    print(atom1.get_temperature())
    print(atom1.get_size())
    print(atom1.get_max_deviation())
    print(atom1.get_dim_y())
    print(atom1.get_dim_x())
    while True:
        atom1.random_move()
        print(atom1.get_dim_x(), atom1.get_dim_y())
        sleep(0.1)

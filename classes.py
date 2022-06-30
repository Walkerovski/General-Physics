from math import atan2, pi, cos, sin
from random import gauss


ACCELERATION_X = 0.2
ACCELERATION_Y = 0.2
MAX_X_VELOCITY = 5

class Atom:
    def __init__(self, start_location_x, start_location_y, max_deviation, size, temperature):
        self.start_location_x = start_location_x
        self.start_location_y = start_location_y
        self.actual_location_x = start_location_x
        self.actual_location_y = start_location_y
        self.velocity_x = 0
        self.velocity_y = 0
        self.max_deviation = max_deviation
        self.size = size
        self.temperature = temperature

    def move(self):
        self.set_new_location_x()
        self.set_new_location_y()
        self.set_new_velocity_x()
        self.set_new_velocity_y()

    def set_new_location_x(self):
        self.actual_location_x += self.velocity_x
        self.actual_location_x = min(self.actual_location_x, self.start_location_x + self.max_deviation)
        self.actual_location_x = max(self.actual_location_x, self.start_location_x - self.max_deviation)
    
    def set_new_location_y(self):
        self.actual_location_y += self.velocity_y
        self.actual_location_y = min(self.actual_location_y, self.start_location_y + self.max_deviation)
        self.actual_location_y = max(self.actual_location_y, self.start_location_y - self.max_deviation)

    def set_new_velocity_x(self):
        self.velocity_x += gauss(0, self.temperature)
        self.velocity_x = max(self.velocity_x, - self.temperature / 30)
        self.velocity_x = min(self.velocity_x, self.temperature / 30)

    def set_new_velocity_y(self):
        self.velocity_y += gauss(0, self.temperature)
        self.velocity_y = max(self.velocity_y, - self.temperature / 30)
        self.velocity_y = min(self.velocity_y, self.temperature / 30)

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
    
    def get_velocity_x(self):
        return self.velocity_x

    def get_velocity_y(self):
        return self.velocity_y


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
        self.last_pos = self.actual_location_x

    def move(self, atoms, HEIGHT, WIDTH):
        self.last_pos = self.actual_location_x
        self.set_new_location_x(WIDTH, HEIGHT)
        self.set_new_location_y(HEIGHT)
        self.set_new_velocity_x()
        self.set_new_velocity_y()
        self.check_collision(atoms, HEIGHT)

    def check_collision(self, atoms, HEIGHT):
        for a in atoms:
            if self.actual_location_x > a.get_dim_x() - a.size \
                and self.actual_location_x < a.get_dim_x() + a.size:
                if self.actual_location_y > a.get_dim_y() - a.size \
                    and self.actual_location_y < a.get_dim_y() + a.size:
                    self.change_velocity_after_collision_with_atom(a)

    def change_velocity_after_collision_with_atom(self, atom):
        radians = atan2(self.get_location_y() - atom.get_dim_y(), self.get_location_x() - atom.get_dim_x())
        vx = abs(self.velocity_x) * cos(radians) + abs(self.velocity_y) * sin(radians)
        vy = abs(self.velocity_x) * sin(radians) + abs(self.velocity_y) * cos(radians)
        if vy < 1:
            if cos(radians) <= 0:
                vy = -3
            else:
                vy = 3
        self.velocity_x = max(min(vx, self.max_x_velocity), - self.max_x_velocity)
        self.velocity_y = max(min(vy, self.max_x_velocity), - self.max_x_velocity)
    
    def set_new_location_x(self, WIDTH, HEIGHT):
        self.actual_location_x += self.velocity_x
        if self.actual_location_x > WIDTH:
            self.actual_location_x = 0
            self.actual_location_y += gauss(0, HEIGHT/10)

    def set_new_location_y(self, HEIGHT):
        self.actual_location_y += self.velocity_y
        if self.actual_location_y > HEIGHT:
            self.actual_location_y = 0
        if self.actual_location_y < 0:
            self.actual_location_y = HEIGHT

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
    
    def get_last_pos(self):
        return self.last_pos


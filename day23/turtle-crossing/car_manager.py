from car import Car

class CarManager:
    
    def __init__(self):
        self.cars = []
        self.level = 0

    def add_car(self):
        car = Car(self.level)
        self.cars.append(car)
    
    def move_all_cars(self):
        for car in self.cars:
            car.move()

    def detect_collision(self, turtle):
        for car in self.cars:
            if car.distance(turtle) < 20:
                return True
        return False
    
    def new_level(self):
        self.level += 1
        for car in self.cars:
            car.increase_speed(self.level)


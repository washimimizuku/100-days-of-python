from car import Car

class CarManager:
    
    def __init__(self):
        self.cars = []

    def add_car(self, level):
        car = Car(level)
        self.cars.append(car)
    
    def move_all_cars(self):
        for car in self.cars:
            car.move()

    def detect_collision(self, turtle):
        for car in self.cars:
            if car.distance(turtle) < 30:
                return True
        return False
    
    def new_level(self, level):
        for car in self.cars:
            car.increase_speed(level)


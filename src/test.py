with open('data/Day 13. input.txt', 'r') as f:
    grid = f.read().rstrip('\n').split('\n')  # grid[y][x]


class Car:
    def __init__(self, char, coords):
        self.xdir = 0
        self.ydir = 0
        if char == '>':
            self.xdir = 1
        elif char == '<':
            self.xdir = -1
        elif char == 'v':
            self.ydir = 1
        elif char == '^':
            self.ydir = -1
        else:
            raise RuntimeError('invalid character for a car ' + char)
        self.coords = coords
        self.turns = 0
        self.crashed = False

    def move(self):
        self.coords = (self.coords[0] + self.xdir, self.coords[1] + self.ydir)
        next_location = grid[self.coords[1]][self.coords[0]]
        if next_location == '/':
            if self.ydir == 0:
                self.left()
            else:
                self.right()
        elif next_location == '\\':
            if self.ydir == 0:
                self.right()
            else:
                self.left()
        elif next_location == '+':
            self.turn()

    def turn(self):
        next_turn = self.turns % 3
        if next_turn == 0:
            self.left()
        elif next_turn == 1:
            pass
        elif next_turn == 2:
            self.right()
        self.turns += 1

    def left(self):
        self.xdir, self.ydir = self.ydir, self.xdir * -1

    def right(self):
        self.xdir, self.ydir = self.ydir * -1, self.xdir


cars = set()
all_cars = {'<', '>', '^', 'v'}
coords = None
for y, row in enumerate(grid):
    for char in all_cars:
        if char in row:
            coords = (row.index(char), y)
            cars.add(Car(char, coords))

iteration = 0 
while len(cars) > 1:
    iteration = iteration + 1
    to_remove = set()
    for car in sorted(sorted(cars, key=lambda c: c.coords[0]), key=lambda c: c.coords[1]):
        car.move()
        for other_car in cars:
            if other_car != car:
                if other_car.coords == car.coords:
                    print(iteration, car.coords)
                    to_remove.add(other_car)
                    to_remove.add(car)
    for car in to_remove:
        cars.remove(car)
    cars = [c for c in cars if c.crashed is False]

print(cars[0].coords)
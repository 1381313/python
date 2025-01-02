import turtle as t
import random
import math

WIDTH, HEIGHT = 800, 600

SQUARE = "square"
RECTANGLE = "rectangle"
TRIANGLE = "triangle"

PROB_SQUARE = 0.5
PROB_RECTANGLE = 0.3
PROB_TRIANGLE = 0.2

t.setup(WIDTH, HEIGHT)
screen = t.Screen()
screen.title("Shape Game")
screen.bgcolor("white")

class Shape:
    def __init__(self, shape_type, x, y):
        self.shape_type = shape_type
        self.x = x
        self.y = y
        self.direction = random.randint(0, 360)
        self.update_dimensions()
        self.t = t.Turtle()
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.pendown()
    
    def update_dimensions(self):
        if self.shape_type == SQUARE:
            self.width, self.height = 30, 30
        elif self.shape_type == RECTANGLE:
            self.width, self.height = 50, 30
        elif self.shape_type == TRIANGLE:
            self.width, self.height = 50, 50
    
    def draw(self):
        self.t.clear()
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.pendown()
        if self.shape_type == SQUARE:
            for _ in range(4):
                self.t.forward(self.width)
                self.t.right(90)
        elif self.shape_type == RECTANGLE:
            for _ in range(2):
                self.t.forward(self.width)
                self.t.right(90)
                self.t.forward(self.height)
                self.t.right(90)
        elif self.shape_type == TRIANGLE:
            for _ in range(3):
                self.t.forward(self.width)
                self.t.right(120)
    
    def move(self):
        self.x += 5 * math.cos(math.radians(self.direction))
        self.y += 5 * math.sin(math.radians(self.direction))

        if self.x < -WIDTH // 2 or self.x > WIDTH // 2:
            self.direction = 180 - self.direction
            self.change_shape()
        if self.y < -HEIGHT // 2 or self.y > HEIGHT // 2:
            self.direction = 360 - self.direction
            self.change_shape()
        
        self.draw()
    
    def change_shape(self):
        rand = random.random()
        if rand < PROB_SQUARE:
            self.shape_type = SQUARE
        elif rand < PROB_SQUARE + PROB_RECTANGLE:
            self.shape_type = RECTANGLE
        else:
            self.shape_type = TRIANGLE
        self.update_dimensions()

    def check_collision(self, other):
        return not (self.x > other.x + other.width or
                    self.x + self.width < other.x or
                    self.y > other.y + other.height or
                    self.y + self.height < other.y)

def main():
    shapes = [Shape(SQUARE, random.randint(-WIDTH//2, WIDTH//2), random.randint(-HEIGHT//2, HEIGHT//2)) for _ in range(10)]
    shapes += [Shape(RECTANGLE, random.randint(-WIDTH//2, WIDTH//2), random.randint(-HEIGHT//2, HEIGHT//2)) for _ in range(5)]
    shapes += [Shape(TRIANGLE, random.randint(-WIDTH//2, WIDTH//2), random.randint(-HEIGHT//2, HEIGHT//2)) for _ in range(5)]

    running = True
    while running:
        for shape in shapes:
            shape.move()
        
        for i in range(len(shapes)):
            for j in range(i + 1, len(shapes)):
                if shapes[i].check_collision(shapes[j]):
                    shapes[i].change_shape()
                    shapes[j].change_shape()
        
        screen.update()

if __name__ == "__main__":
    t.tracer(0, 0)  
    main()
    t.done()

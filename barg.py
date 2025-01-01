import matplotlib.pyplot as mp
import random
point= 100000

x, y = [0], [0]

coe = [
    (0, 0, 0, 0.16, 0, 0),       
    (0.85, 0.04, -0.04, 0.85, 0, 1.6), 
    (0.2, -0.26, 0.23, 0.22, 0, 1.6),   
    (-0.15, 0.28, 0.26, 0.24, 0, 0.44)
]

probabilities = [0.01, 0.85, 0.07, 0.07]
def choose_function():
    r = random.random()
    cumulative_probability = 0
    for i, p in enumerate(probabilities):
        cumulative_probability += p
        if r <= cumulative_probability:
            return coe[i]

for _ in range(point):
    a, b, c, d, e, f = choose_function()
    x_new = a * x[-1] + b * y[-1] + e
    y_new = c * x[-1] + d * y[-1] + f
    x.append(x_new)
    y.append(y_new)
    
    
mp.figure(figsize=(5, 7))
mp.scatter(x, y, s=0.1, color='green')
mp.title("Barnsley Fern")
mp.axis("off")
mp.show()

import random
import matplotlib.pyplot as plt
import numpy as np
num_points = 7
iterations = 5000
points = [(random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range(num_points)]
final_points = []
for _ in range(iterations):
    new_points = []
    for x, y in points:
        rand = random.uniform(0, 1) 
        if rand <= 0.4: 
            new_x = 0.31 * x - 0.53 * y + 0.89
            new_y = -0.46 * x - 0.29 * y + 1.04
        elif rand <= 0.55:  
            new_x = 0.31 * x - 0.08 * y + 0.22
            new_y = 0.15 * x - 0.45 * y + 0.38
        else:  
            new_x = 0.55 * y + 0.01
            new_y = -0.69 * x - 0.20 * y + 0.38
        new_points.append((new_x, new_y))
    points = new_points
    final_points.extend(points)
x_vals, y_vals = zip(*final_points)
colors = np.linspace(0, 1, len(x_vals))
plt.figure(figsize=(8,5))
plt.scatter(x_vals, y_vals, c=colors, cmap="viridis", s=0.06, alpha=0.7)
plt.axis("off")
plt.show()

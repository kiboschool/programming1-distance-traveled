# Write your code here
import math

def distance(x, y):
    return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)


def total_distance(points):
    total = 0.0
    for i in range(len(points) - 1):
        total += distance(points[i], points[i+1])
    return total

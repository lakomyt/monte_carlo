import matplotlib.pyplot as plt
import matplotlib.patches as ptc
from random import uniform

def show_shape(patch):
	ax=plt.gca()
	ax.add_patch(patch)
	plt.axis("scaled")

Cx = int(input("Circle center x = "))
Cy = int(input("Circle center y = "))
Cr = int(input("Circle radius = "))

Rx = int(input("Rectangle left corner x = "))
Ry = int(input("Rectangle left corner y = "))
Rw = int(input("Rectangle width = "))
Rh = int(input("Rectangle height = "))

circle_center = (Cx, Cy)
circle_radius = Cr

points_inside = 0

samples = int(input("Number of samples: "))
for x in range(samples):
	x = uniform(Rx,Rx+Rw)
	y = uniform(Ry,Ry+Rh)
	if pow(x-circle_center[0], 2) + pow(y-circle_center[1], 2) <= pow(circle_radius, 2):
		points_inside += 1
	points = plt.scatter(x, y, s=30)

circle = plt.Circle(circle_center, circle_radius, fill=False)

rectangle = ptc.Rectangle((Rx, Ry), Rw, Rh, fill=False)

print("\n\ncircle area/rectangle area ~ ", points_inside/samples)

show_shape(circle)
show_shape(rectangle)
plt.show()

import matplotlib.pyplot as plt
import matplotlib.patches as ptc
from random import uniform

def show_shape(patch):
	ax=plt.gca()
	ax.add_patch(patch)
	plt.axis('scaled')

points_inside=0

samples = int(input("Number of samples: "))
for x in range(samples):
	x = uniform(0,2)
	y = uniform(0,2)
	if pow(x-1, 2)+pow(y-1, 2) <= pow(1, 2):
		points_inside += 1
	points = plt.scatter(x, y, s=20)

circle = plt.Circle((1, 1), 1, fill=False)

rectangle = ptc.Rectangle((0, 0), 2, 2, fill=False)

print("\nπ ~ ", points_inside/samples*4)

show_shape(circle)
show_shape(rectangle)
plt.show()

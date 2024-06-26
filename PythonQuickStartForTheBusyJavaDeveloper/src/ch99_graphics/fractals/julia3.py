# https://www.geeksforgeeks.org/julia-fractal-python/
import matplotlib.pyplot as plt

# ADJUSTABLE VARIABLES/PARAMETERS
center = -0.05 - 0.66j
range_ = 0.9 + abs(center)
max_iterations = 100

x1, y1 = -1.5, -1  # plotting julia-set in the rectangle with opposite corners (x1,y1) and (x2,y2)
x2, y2 = 1.5, 1
linearResolution = 500

# PERFORMING CALCULATIONS TO GET THE 2D-ARRAY REPRESENTING JULIA SET
M, N = int((y2 - y1) * linearResolution), int((x2 - x1) * linearResolution)

xcoordinates = [(x1 + ((x2 - x1) / N) * i) for i in range(N)]  # x-coordinates of the sample-points
ycoordinates = [(y1 + ((y2 - y1) / M) * i) for i in range(M)]  # y-coordinates of the sample-points

# juliaSet is a 2D Array representing values at the sample points of the julia-set.
# Initially all the values are set to None.
# Later, if the sample-point belongs to the julia set, set the corresponding location in
# juliaSet array to 0. If it does not, set it to the number of iterations it too to cross range_ .
juliaSet = [[None for i in xcoordinates] for j in ycoordinates]

for y in range(len(ycoordinates)):
    for x in range(len(xcoordinates)):
        z = complex(xcoordinates[x], ycoordinates[y])
        iteration = 0
        while (abs(z) < range_ and iteration < max_iterations):
            iteration += 1
            z = z ** 2 + center

        if (iteration == max_iterations):
            juliaSet[y][x] = 0  # the corresponding sample point belongs to the julia set
        else:
            juliaSet[y][x] = iteration  # the corresponding sample point doesn't belong to the julia set

# PLOTTING THE DATA
ax = plt.axes()
ax.set_aspect('equal')  # directing matplotlib to keep the scale of x and y axes same.
plot = ax.pcolormesh(xcoordinates, ycoordinates, juliaSet, cmap='magma')  # creating the heatmap of julia-set array
plt.colorbar(plot)  # adding scale of the colors
plt.title('Julia-set \ncenter = {}, range = {:.3f}, max-iterations = {}'.format(center, range_,
                                                                                max_iterations))  # setting title
plt.show()
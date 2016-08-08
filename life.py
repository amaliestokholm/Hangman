"""
This is my attempt to write Conway's Game of Life using numpy.

# Conway's Game of Life Challenge

https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

# Rules

> Any live cell with fewer than two live neighbours dies,
  as if caused by under-population.
> Any live cell with two or three live neighbours lives on to the next
  generation.
> Any live cell with more than three live neighbours dies,
  as if by overcrowding.
> Any dead cell with exactly three live neighbours becomes a live cell,
  as if by reproduction.
"""

import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt


def life(size, interval, frames):
    """
    Input:
     - size: the size for the grid. Must be (n, m)
     - interval: the pause in ms between each frame in the animation
     - frames: the number of frames in the animation
    """
    X = np.random.randint(0, 2, size)

    """
    # Glider-test (see https://en.wikipedia.org/wiki/Glider_(Conway%27s_Life))
    X = np.zeros([Y, Y])
    X[0,1] = 1
    X[1,2] = 1
    X[2,0] = 1
    X[2,1] = 1
    X[2,2] = 1
    """
    assert X.ndim == 2
    animate(X, interval, frames)


def life_step(X):
    # Count the number of neightbours
    size = X.shape
    xdim = size[0]
    ydim = size[1]
    N = np.zeros(X.shape)

    """
    I could optimize a lot by avoiding these loops - but this is just 
    a naive implementation. I'm using toroidal boundary conditions.
    """
    for i in np.arange(xdim):
        for j in np.arange(ydim):
            u = (i, (j-1) % ydim)
            d = (i, (j+1) % ydim)
            l = ((i-1) % xdim, j)
            r = ((i+1) % xdim, j)
            ul = ((i-1) % xdim, (j-1) % ydim)
            ur = ((i+1) % xdim, (j-1) % ydim)
            dl = ((i-1) % xdim, (j+1) % ydim)
            dr = ((i+1) % xdim, (j+1) % ydim)
            N[i, j] = (X[u] + X[d] + X[l] + X[r] +
                       X[ul] + X[ur] + X[dl] + X[dr])

    # Apply rules
    reproduce = np.logical_and(N == 3, X == 0)
    survive = np.logical_and(np.logical_or(N == 2, N == 3), X == 1)
    die = np.logical_and(X == 1, np.logical_or(N < 2, N > 3))
    X[die] = 0
    X[survive] = 1
    X[reproduce] = 1
    return X


def animate(X, interval, frames):
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1], xticks=[], yticks=[], frameon=False)
    im = ax.imshow(X, interpolation='nearest')

    def init():
        im.set_data(X)
        return im,

    def animate(i):
        im.set_data(animate.X)
        animate.X = life_step(animate.X)
        return (im,)
    animate.X = X

    anim = animation.FuncAnimation(fig, animate,
                                   frames=frames, interval=interval)
    plt.show()


life((30, 40), 50, 40)

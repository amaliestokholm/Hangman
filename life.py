# This is my attempt to write Conway's Game of Life using numpy
import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt


def life():
    size = 30
    X = np.random.randint(0, 2, (size, size))
    
    # Glider
    """
    X = np.zeros([Y, Y])
    X[0,1] = 1
    X[1,2] = 1
    X[2,0] = 1
    X[2,1] = 1
    X[2,2] = 1
    """
    assert X.ndim == 2

    interval = 200
    frames = 40
    animate(X, interval, frames)


def life_step(X):
    # Count the number of neightbours
    dim = len(X)
    N = np.zeros(X.shape)

    # I could optimize a lot by avoiding these loops
    for i in np.arange(dim):
        for j in np.arange(dim ):
            u = (i, (j-1) % dim)
            d = (i, (j+1) % dim)
            l = ((i-1) % dim, j)
            r = ((i+1) % dim, j)
            ul = ((i-1) % dim, (j-1) % dim)
            ur = ((i+1) % dim, (j-1) % dim)
            dl = ((i-1) % dim, (j+1) % dim)
            dr = ((i+1) % dim, (j+1) % dim)
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


life()

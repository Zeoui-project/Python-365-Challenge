# %% [markdown]
# # Three Dimensional Contour Plot using Python

# %%
import numpy as np
import matplotlib.pyplot as plt
import sys

def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

question = int(input("Welcome to Dimensional Contour project!! type 1 for default or any number to input manually : "))
if question == 1:
    x = np.linspace(-6, 6, 30)
    y = np.linspace(-6, 6, 30)

    x, y = np.meshgrid(x, y)
    z = f(x, y)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.contour3D(x, y, z, 60, cmap='binary')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()

else:
    for retry in range(2):
        xpos = [int(input("Enter the X position (3 axis) : ")) for _ in range(3)]
        x1, x2, x3 = xpos
        ypos = [int(input("Enter the Y position (3 axis) : ")) for _ in range(3)]
        y1, y2, y3 = ypos

        a = int(input(f"{x1=}, {x2=}, {x3=} and {y1=}, {y2=}, {y3=}, is this number correct? type '1' for 'YES' or any number if to re-submit"))
        
        if a == 1:
            x = np.linspace(x1, x2, x3)
            y = np.linspace(y1, y2, y3)

            x, y = np.meshgrid(x, y)
            z = f(x, y)
            fig = plt.figure()
            ax = plt.axes(projection='3d')
            ax.contour3D(x, y, z, 60, cmap='binary')
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_zlabel('z')
            plt.show()

            break
        else:
            print("Input the correct number this time!")
    else:
        print("you keep making invalid choices, exiting.")
        sys.exit(1)



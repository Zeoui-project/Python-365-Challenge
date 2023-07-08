# %% [markdown]
# # A. Print Triangle of Stars

# %%
rows = 6
for i in range(rows):
    for j in range(i + 1):
        print('*', end='')
    print()

# %% [markdown]
# # B. Print an inverted triangle of Stars

# %%
rows = 6
for i in range(rows, 0, -1):
    for j in range(0, i):
        print('*', end='')
    print()

# %%
rows = 6
for i in range(1, rows+1):
    for j in range(1, rows-i+1):
        print(' ', end='')
    for k in range(1, 2*i):
        print('*', end='')
    print()
for i in range(rows-1, 0, -1):
    for j in range(1, rows-i+1):
        print(' ', end='')
    for k in range(1, 2*i):
        print('*', end='')
    print()

# %% [markdown]
# # D. Print hollow square of Stars

# %%
rows = 6
for i in range(rows):
    for j in range(rows):
        if i == 0 or i == rows-1 or j == 0 or j == rows-1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# %% [markdown]
# # E. Print solid square of Stars

# %%
rows = 6
for i in range(rows):
    for j in range(rows):
        print('*', end='')
    print()

# %% [markdown]
# # F. Print hollow diamond of Stars

# %%
rows = 6
for i in range(1, rows+1):
    for j in range(1, rows-i+1):
        print(' ', end='')
    for k in range(1, 2*i):
        if k == 1 or k == 2*i-1:    
            print('*', end='')
        else:
            print(' ', end='')
    print()
for i in range(rows-1, 0, -1):
    for j in range(1, rows-i+1):
        print(' ', end='')
    for k in range(1, 2*i):
        if k == 1 or k == 2*i-1:    
            print('*', end='')
        else:
            print(' ', end='')
    print()

# %% [markdown]
# # G. Print parallelogram Star pattern

# %%
rows = 6
for i in range(1, rows+1):
    for j in range(1, rows-i+1):
        print(' ', end='')
    for k in range(1, rows+1):
        print('*', end='')
    print()

# %% [markdown]
# # H. Print Triangle shaped Star

# %%
rows = 6
for i in range(1, rows+1):
    for j in range(1, rows-i+1):
        print(' ', end='')
    for k in range(1, 2*i):
        print('*', end='')
    print()

# %% [markdown]
# # I. Print Arrow Star Pattern

# %%
rows = 6
for i in range(1, rows):
    for j in range(i):
        print('*', end='')
    print()
for i in range(rows, 0, -1):
    for j in range(i):
        print('*', end='')
    print()

# %% [markdown]
# # J. Print Heart shaped Star pattern

# %%
rows = 7
for i in range(rows):
    for j in range(rows):
        if i == 0 and j % 3 != 0 or i == 1 and j % 3 == 0 or i-j == 2 or i+j == 8:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# %% [markdown]
# # K. Print a Butterfly shaped Star Pattern

# %%
rows = 6
for i in range(rows):
    for j in range(i+1):
        print('*', end='')
    for j in range(2*rows-2*i-2):
        print(' ', end='')
    for j in range(i+1):
        print('*', end='')
    print()
for i in range(rows):
    for j in range(rows-i):
        print('*', end='')
    for j in range(2*i):
        print(' ', end='')
    for j in range(rows-i):
        print('*', end='')
    print()
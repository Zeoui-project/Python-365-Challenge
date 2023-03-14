# %% [markdown]
# # Full Diamond Pattern using Python

# %%
rows = int(input("Enter Diamond Pattern Rows = "))
print("Diamond Star Pattern")
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(end = ' ')
    for k in range(0, 2 * i - 1):
        print("*", end = '')
    print()
for i in range(1, rows):
    for j in range(1, i + 1):
        print(end = ' ')
    for l in range(1, (2 * (rows - i))):
        print("*", end = '')
    print()



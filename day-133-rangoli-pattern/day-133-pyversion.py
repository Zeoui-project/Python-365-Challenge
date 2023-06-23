# %% [markdown]
# # Rangoli Pattern with Alphabets using Python

# %%
def print_rangoli(size):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    data = [alpha[i] for i in range(size)]
    items = list(range(size))
    items = items[:-1]+items[::-1]

    for i in items:
        temp = data[-(i+1):]
        row = temp[::-1]+temp[1:]
        print("-".join(row).center(n*4-3, "-"))

if __name__ == '__main__':
    n = int(input("Enter the size of Rangoli Pattern (>5 for better visualization)"))
    if n > 26:
        print_rangoli(26)
    elif n < 1:
        print_rangoli(1)
    else:
        print_rangoli(n)



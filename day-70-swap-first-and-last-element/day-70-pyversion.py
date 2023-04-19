# %% [markdown]
# # Swap First and Last Element

# %%
# Swap Function
def swapList(newList):
    size = len(newList)

    # Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList

# Driver code
newList = []
newList = [int(item) for item in input("Enter the list items : ").split()]

print(swapList(newList))



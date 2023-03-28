# %% [markdown]
# # Insertion Sort using Python

# %%
def insertionSort(List):
    for i in range(1, len(List)):
        currentNumber = List[i]
        for j in range(i - 1, -1, -1):
            if List[j] > currentNumber :
                List[j], List[j + 1] = List[j + 1], List[j]
            else:
                List[j + 1] = currentNumber
                break
    return List

if __name__ == '__main__':
    List = [8, 4, 2, 6, 5, 7, 1, 9]
    print('Sorted List: ', insertionSort(List))



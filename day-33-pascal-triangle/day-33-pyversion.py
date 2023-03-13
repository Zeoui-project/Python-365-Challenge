# %% [markdown]
# # Pascal Triangle using Python

# %%
def Pascal(N):
    arr = [1]
    temp = []
    print("Pascal's triangle of", N, "Rows...")
    for i in range(N):
        print("rows", i+1, end=" : ")
        for j in range(len(arr)):
            print(arr[j], end=' ')
        print()
        temp.append(1)
        for j in range(len(arr)-1):
            temp.append(arr[j] + arr[j+1])
        temp.append(1)
        arr = temp
        temp = []

N = int(input("Enter the Number for the Pascal Triangle :"))
Pascal(N)



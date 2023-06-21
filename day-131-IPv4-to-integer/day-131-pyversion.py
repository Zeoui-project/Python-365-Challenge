# %% [markdown]
# # Converts IPv4 to Integer using Python

# %%
ip = input("Enter your IP : ")
def convert(s: str):
    # Extract each digit from s
    digits = [int(x) for x in s.split('.')]
    # Add them together
    shift = [24, 16, 8, 0]
    for i in range(4):
    digits[i] <<= shift[i]
    return sum(digits)
result = convert(ip)
print(result)
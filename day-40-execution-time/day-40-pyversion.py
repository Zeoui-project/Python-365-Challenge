# %% [markdown]
# # Execution Time of a Python program

# %%
from time import time
start = time()

#code start
email = input("Enter Your Email: ")
email = email.strip()
slicer_index = email.index("@")
username = email[:slicer_index]
domain_name = email[slicer_index+1:]
print("Your user name is ", username," and your domain is ", domain_name)

end = time()
execution_time = end - start
print("Execution Time (s) : ", execution_time)



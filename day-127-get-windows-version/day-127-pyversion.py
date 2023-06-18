# %% [markdown]
# # Get windows version using Python

# %%
%pip install wmi

# %%
# pip install wmi
import wmi
data = wmi.WMI()
for os_name in data.Win32_OperatingSystem():
    print(os_name.Caption)
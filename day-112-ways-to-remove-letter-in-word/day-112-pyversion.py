# %% [markdown]
# # 5 Ways to Remove Letter in Word using Python

# %%
#1st Method
a='zeoui-project'
a.replace('zeoui-','')

# %%
#2nd Method
a='zeoui-project'
a[0:5]

# %%
#3rd Method
a='zeoui-project'
a.partition('zeoui-')[2]

# %%
#4th Method
import re
a='zeoui-project'
re.sub(r'zeoui-','',a)

# %%
#5th Method
a='zeoui-project'
a.strip('zeoui-')
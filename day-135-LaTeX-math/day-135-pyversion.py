# %% [markdown]
# # LaTeX math description using Python functions

# %% [markdown]
# ONLY SUPPORT PYTHON 3.7 until 3.10

# %%
%pip install latexify-py==0.2.0

# %%
import math
import latexify

# %%
@latexify.with_latex
def solve(a, b, c):
    return (-b + math.sqrt(b**2 - 4*a*c)) / (2*(a+b))
solve

# %%
@latexify.with_latex
def sinc(x):
    if x == 0:
        return 1
    else:
        return math.sin(x) / x
sinc

# %%
@latexify.with_latex
def greek(alpha, beta, gamma, Omega):
    return alpha * beta * math.gamma(gamma) + Omega
greek
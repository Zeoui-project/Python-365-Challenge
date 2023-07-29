# %% [markdown]
# # Twitter Logo Generation using Python

# %%
%pip install pyfiglet

# %%
import pyfiglet
import random

def generate_logo_ko(font):
    logo_k = pyfiglet.figlet_format("X", font=font)
    return f"{logo_k}"

def generate_random_font():
    figlet_instance = pyfiglet.Figlet()
    fonts = figlet_instance.getFonts()
    return random.choice(fonts)

if __name__ == "__main__":
    random_font = generate_random_font()
    logo = generate_logo_ko(random_font)
    print(logo)
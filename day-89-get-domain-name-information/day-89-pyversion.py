# %% [markdown]
# # Get Domain Name Information using Python

# %%
import whois
domain = input("Enter your Domain : ")
domain_info = whois.whois(domain)
for key, value in domain_info.items():
    print(key, ':', value)



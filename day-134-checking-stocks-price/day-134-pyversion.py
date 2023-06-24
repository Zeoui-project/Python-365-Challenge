# %% [markdown]
# # Checking Stocks Price using Python

# %%
%pip install yfinance

# %%
import yfinance as yf
STK = input("Enter share name : ")
Share = yf.Ticker(STK).info
market_price = Share['currentPrice']
print("Current Price : ", market_price)
# %% [markdown]
# # Decimal to Roman numeral using Python

# %%
decimal_num = int(input("Enter a Decimal Number : "))

def decimal_to_roman(decimal_num):
    roman_to_decimal = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 
                        100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X',
                        9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    roman_numeral = ''
    for value, numeral in roman_to_decimal.items():
        while decimal_num >= value:
            roman_numeral += numeral
            decimal_num -= value
    return roman_numeral
print(decimal_to_roman(decimal_num))
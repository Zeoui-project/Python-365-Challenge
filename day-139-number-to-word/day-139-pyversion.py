# %% [markdown]
# # Converts number to its equivalent word using Python

# %%
num = int(input("Enter a Number : "))
def number_to_words(num):
    units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", 
             "eleven", "twelve","thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty","thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if num < 20:
        return (units[int(num)])
    elif num < 100:
        return tens[num // 10] + ('' if num % 10 == 0 else ' ' + units[int(num % 10)])
    elif num < 1000:
        return units[int(num // 100)] + " hundred" + ('' if num % 100 == 0
                                                      else ' ' + number_to_words(num % 100))
    elif num < 1000000:
        return number_to_words(num // 1000) + " thousand" + (
            '' if num % 1000 == 0 else ' ' + number_to_words(num % 1000))
    else:
        return "Number exceeded the range"
print(number_to_words(num))
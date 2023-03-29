# %% [markdown]
# # Progress Bar using Python

# %%
import sys, time

def progressBar(count, total, suffix=''):
    barLength = 60
    filledLength = int(round(barLength * count / float(total)))

    percent = round(100.0 * count / float(total), 1)
    bar = "=" * filledLength + '-' * (barLength - filledLength)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percent, '%', suffix))
    sys.stdout.flush()

# if n = n (progress bar 90% not 100%)
for i in range(11):
    time.sleep(1)
    progressBar(i, 10)



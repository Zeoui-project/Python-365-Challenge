# %% [markdown]
# # Generate Sine, Square, Triangle and Sawtooth waveform

# %%
import numpy as np
import matplotlib.pyplot as plt

# Define the signal parameters
T = 1 # Period (Seconds)
fs = 1000 # Sampling Frequency (Hz)
t = np.linspace(0, T, T*fs, endpoint=False)

# Generate sine wave
f_sine = 5 # Frequency (Hz)
sine_wave = np.sin(2*np.pi*f_sine*t)

# Generate Square Wave
f_square = 2 # Frequency (Hz)
duty_cycle = 0.01 # Percentage of the period where the signal is high
square_wave = np.where(np.mod(np.floor(2*duty_cycle*fs*t), 2) == 0, 1, -1)

# Generate Triangle wave
f_triangle = 1 # Frequency (Hz)
triangle_wave = 2*np.abs((10*f_triangle*t) % 2 - 1) - 1

# Generate Sawtooth wave
f_sawtooth = 10  # Frequency (Hz)
sawtooth_wave = 2 * (f_sawtooth*t - np.floor(f_sawtooth*t + 0.5))

# Plot the waves
fig, axs = plt.subplots(4, 1, sharex=True, figsize=(8,8))
axs[0].plot(t, sine_wave)
axs[0].set_title('Sine Wave')
axs[1].plot(t, square_wave)
axs[1].set_title('Square Wave')
axs[2].plot(t, triangle_wave)
axs[2].set_title('Triangle Wave')
axs[3].plot(t, sawtooth_wave)
axs[3].set_title('Sawtooth Wave')
plt.xlabel('Time (s)')
plt.show()
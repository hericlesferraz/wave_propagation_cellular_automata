import numpy as np
import matplotlib.pyplot as plt

def calculate_insertion_loss(N):
    """Calculate the Insertion Loss (IL) based on Fresnel Number (N)."""
    sinh_inverse_1 = np.arcsinh(1)
    
    if N >= 1:
        IL = 10 * np.log10(N) + 13
    elif -0.324 <= N and N < 1:
        IL = 5 + (8 / sinh_inverse_1) * np.arcsinh(abs(N) ** 0.485)
    else:
        IL = 0
    
    return IL


def calculate_fresnel_and_IL(source, observer, wall_top, freq, c=344):
    """
    Calculates Fresnel number (N) and Insertion Loss (IL) for a sound wave with complex barriers.
    """
    A = np.sqrt((source[0] - wall_top[0])**2 + (source[1] - wall_top[1])**2)
    B = np.sqrt((observer[0] - wall_top[0])**2 + (observer[1] - wall_top[1])**2)
    d = np.sqrt((source[0] - observer[0])**2 + (source[1] - observer[1])**2)
    wavelength = c / freq
    N = 2 * ((A + B) - d) / wavelength
    IL = calculate_insertion_loss(N)
    max_IL = max(max_IL, IL)

    return N, max_IL


frequencies = np.arange(0, 2100, 100)
source = (3, 3)  
observer = (5, 1)

wall_configs = {
    "Type 1": (2, 3),
    "Type 2": (2, 4),
    "Type 3": (2, 5),
}

symbols = {
    "Type 1": "s",
    "Type 2": "o",
    "Type 3": "^",
}

results = {}

for wall_type, wall_top in wall_configs.items():
    IL_values = []
    for freq in frequencies:
        _, IL = calculate_fresnel_and_IL(source, observer, wall_top, freq)
        IL_values.append(IL)
    results[wall_type] = IL_values

plt.figure(figsize=(6, 3))
for wall_type, IL_values in results.items():
    plt.plot(frequencies, IL_values, marker=symbols[wall_type], label=wall_type)

plt.ylim(0, 50)
plt.title("Insertion Loss in Relation to Frequency for Different Types of Barriers")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Insertion (IL) [dB]")
plt.legend()
plt.grid(True)
plt.show()

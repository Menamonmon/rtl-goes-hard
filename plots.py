import matplotlib.pyplot as plt
import numpy as np

# Data setup
labels = ['0%', '25%', '50%', '75%']
num_groups = len(labels)
x = np.arange(num_groups)
bar_width = 0.15

# Dummy data (replace with your real values)
A_00 = [
    [1.0, 1.0, 1.0, 1.0],    # Default
    [1.5, 1.15, 0.55, 0.2],  # Highlight
    [0.75, 0.6, 0.4, 0.3],   # Tensaurus
    [0.3, 0.3, 0.3, 0.2]     # NVIDIA 2:4
]

A_25 = [
    [1.0, 1.0, 1.0, 1.0],    # Default
    [1.5, 1.15, 0.55, 0.2],  # Highlight
    [0.75, 0.6, 0.4, 0.3],   # Tensaurus
    [0.3, 0.3, 0.3, 0.2]     # NVIDIA 2:4
]


A_50 = [
    [1.0, 1.0, 1.0, 1.0],    # Default
    [1.5, 1.15, 0.55, 0.2],  # Highlight
    [0.75, 0.6, 0.4, 0.3],   # Tensaurus
    [0.3, 0.3, 0.3, 0.2]     # NVIDIA 2:4
]


A_75 = [
    [1.0, 1.0, 1.0, 1.0],    # Default
    [1.5, 1.15, 0.55, 0.2],  # Highlight
    [0.75, 0.6, 0.4, 0.3],   # Tensaurus
    [0.3, 0.3, 0.3, 0.2]     # NVIDIA 2:4
]


area = [
    [1.0, 1.0, 1.0, 1.0],    # Default
    [1.5, 1.15, 0.55, 0.2],  # Highlight
    [0.75, 0.6, 0.4, 0.3],   # Tensaurus
    [0.3, 0.3, 0.3, 0.2]     # NVIDIA 2:4
]

data = A_00 # TODO: Change to display

colors = ['#1f77b4', '#ff7f0e', '#d62728', '#2ca02c', '#d8c564b']
hatches = ['.', '\\', '*', '-', 'o']
bar_labels = ['Default', 'Highlight', 'Tensaurus', 'NVIDIA 2:4']

fig, ax = plt.subplots(figsize=(6, 4))

# Plot each method with color + hatching
for i in range(len(data)):
    ax.bar(x + i * bar_width, data[i], width=bar_width,
           label=bar_labels[i], color=colors[i], hatch=hatches[i])

# Set up axes, ticks, labels
ax.set_xticks(x + 2 * bar_width)
ax.set_xticklabels(labels)
ax.set_ylabel('Normalized EDP')
ax.set_xlabel('Operand B Sparsity Degrees')
ax.set_ylim(0, 1.2)
ax.set_title('Sparsity')
ax.legend()











# Annotate bar at 1.5
# ax.text(x[0] + bar_width, 1.52, '1.50000000', ha='center', va='bottom', fontsize=10)

# Add "lower is better" rotated annotation
ax.annotate('lower is better', xy=(-0.7, 0.6), xytext=(-1.1, 0.6), rotation=90,
            fontsize=10, color='olive', weight='bold')

plt.tight_layout()
plt.show()
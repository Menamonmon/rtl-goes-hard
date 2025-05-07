import matplotlib.pyplot as plt
import numpy as np

# Data setup
labels = ['100%', '50%', '33%', '25%']
num_groups = len(labels)
x = np.arange(num_groups)
bar_width = 0.15

# Dummy data (replace with your real values)
energy = [
    [248.15, 173.42, 150.30, 137.39],    # STC  (Default)
    [275.15, 186.92, 159.30, 144.54],  # NVIDIA 2:4
    [277.39, 188.04, 160.04, 145.10],   # Highlight
    [283.02, 190.85, 161.92, 146.51]     # Tensaurus
]


edp = [
    [36.6, 12.8, 10.6, 9.19],    # STC  (Default)
    [40.6, 13.8, 11.2, 9.64],  # NVIDIA 2:4
    [40.9, 13.9, 11.2, 9.68],   # Highlight
    [41.7, 14.1, 11.4, 9.77]     # Tensaurus
]


area = [
    [1.0, 1.0, 1.0, 1.0],    # Default
    [1.5, 1.15, 0.55, 0.2],  # NVIDIA 2:4
    [0.75, 0.6, 0.4, 0.3],   # Highlight
    [0.3, 0.3, 0.3, 0.2]     # Tensaurus
]

data = edp



# Statistics

#  Default:
#   Area   = 3.14 mm^2
#   100% Energy | EDP = 248.15 | 3.66e+01
#   50% Energy  | EDP = 173.42 | 1.28e+01
#   33% Energy  | EDP = 150.30 | 1.06e+01
#   25% Energy  | EDP = 137.79 | 9.19e+00
#
#
#  NVIDIA:
#   Area   = 255 um^2
#   Energy = 0.1788 pJ
#   100% Energy | EDP = 275.15 | 4.06e+01
#   50% Energy  | EDP = 186.92 | 1.38e+01
#   33% Energy  | EDP = 159.30 | 1.12e+01
#   25% Energy  | EDP = 144.54 | 9.64e+00
#
#
#
#  Highlight:
#   Area   = 773 um^2
#   Energy = 0.1936 pJ
#   100% Energy | EDP = 277.39 | 4.09e+01
#   50% Energy  | EDP = 188.04 | 1.39e+01
#   33% Energy  | EDP = 160.04 | 1.12e+01
#   25% Energy  | EDP = 145.10 | 9.68e+00
#
#
#  Tensaurus:
#   Area   = 1358 um^2
#   Energy = 0.2309
#   100% Energy | EDP = 283.02 | 4.17e+01
#   50% Energy  | EDP = 190.86 | 1.41e+01
#   33% Energy  | EDP = 161.92 | 1.14e+01
#   25% Energy  | EDP = 146.51 | 9.77e+00
#
#



colors = ['#1f77b4', '#2ca02c', '#ff7f0e', '#d62728', '#8c564b' ]
hatches = ['.', '\\', '*', '-', 'o']
bar_labels = ['Default', 'NVIDIA 2:4', 'Highlight', 'Tensaurus']

fig, ax = plt.subplots(figsize=(6, 4))

# Plot each method with color + hatching
# for i in range(len(data)):
#     ax.bar(x + i * bar_width, data[i], width=bar_width,
#            label=bar_labels[i], color=colors[i], hatch=hatches[i])

for i in range(len(data)):
    ax.bar(x + i * bar_width, data[i], width=bar_width,
           label=bar_labels[i], color=colors[i])

# Set up axes, ticks, labels
ax.set_xticks(x + 2 * bar_width)
ax.set_xticklabels(labels)
ax.set_ylabel('EDP (J*cycle)')
ax.set_xlabel('Input Sparsity')
# ax.set_ylim(0, 1.2)
ax.set_title('Energy Usage on ResNet50')
ax.legend()







# Annotate bar at 1.5
# ax.text(x[0] + bar_width, 1.52, '1.50000000', ha='center', va='bottom', fontsize=10)

# Add "lower is better" rotated annotation
ax.annotate('lower is better', xy=(-0.7, 0.6), xytext=(-1.1, 0.6), rotation=90,
            fontsize=40, color='olive', weight='bold')

plt.tight_layout()
plt.show()
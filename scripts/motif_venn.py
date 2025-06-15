import pandas as pd
from matplotlib import pyplot as plt
from matplotlib_venn import venn3

# Load motif sets
human = set(pd.read_csv("D:/Project/EvoTriplex-Lnc/results/motifs_human.csv")["Motif"])
chimp = set(pd.read_csv("D:/Project/EvoTriplex-Lnc/results/motifs_chimp.csv")["Motif"])
mouse = set(pd.read_csv("D:/Project/EvoTriplex-Lnc/results/motifs_mouse.csv")["Motif"])

# Create Venn diagram
plt.figure(figsize=(8, 6))
venn3([human, chimp, mouse], ('Human', 'Chimp', 'Mouse'))

plt.title("Triplex-like Motif Overlap Across Species")
plt.tight_layout()
plt.savefig("D:/Project/EvoTriplex-Lnc/results/motif_overlap_venn.png")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load motif CSVs
human = pd.read_csv("D:/Project/EvoTriplex-Lnc/results/motifs_human.csv")
chimp = pd.read_csv("D:/Project/EvoTriplex-Lnc/results/motifs_chimp.csv")
mouse = pd.read_csv("D:/Project/EvoTriplex-Lnc/results/motifs_mouse.csv")

# Count unique motifs per species
counts = {
    'Human': len(human["Motif"].unique()),
    'Chimp': len(chimp["Motif"].unique()),
    'Mouse': len(mouse["Motif"].unique())
}

# Plotting
plt.figure(figsize=(6, 5))
plt.bar(counts.keys(), counts.values(), color=['#1f77b4', '#ff7f0e', '#2ca02c'])
plt.title("Number of Unique Triplex-like Motifs per Species")
plt.ylabel("Motif Count")
plt.tight_layout()

# Save
plt.savefig("D:/Project/EvoTriplex-Lnc/results/motif_counts_barplot.png")
plt.show()

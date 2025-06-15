import pandas as pd

# Load CSVs
human_df = pd.read_csv("D:/Project/EvoTriplex-Lnc/results/motifs_human.csv")
chimp_df = pd.read_csv("D:/Project/EvoTriplex-Lnc/results/motifs_chimp.csv")
mouse_df = pd.read_csv("D:/Project/EvoTriplex-Lnc/results/motifs_mouse.csv")

# Extract unique motifs from each species
human_motifs = set(human_df["Motif"])
chimp_motifs = set(chimp_df["Motif"])
mouse_motifs = set(mouse_df["Motif"])

# Find shared and unique motifs
shared_all = human_motifs & chimp_motifs & mouse_motifs
shared_human_chimp = human_motifs & chimp_motifs - mouse_motifs
unique_human = human_motifs - chimp_motifs - mouse_motifs

# Save results (no emojis, utf-8 encoding)
with open("D:/Project/EvoTriplex-Lnc/results/motif_comparison_summary.txt", "w", encoding="utf-8") as f:
    f.write(f"Shared in all 3 species ({len(shared_all)}):\n")
    f.write("\n".join(shared_all) + "\n\n")
    
    f.write(f"Shared between human & chimp only ({len(shared_human_chimp)}):\n")
    f.write("\n".join(shared_human_chimp) + "\n\n")
    
    f.write(f"Unique to human ({len(unique_human)}):\n")
    f.write("\n".join(unique_human) + "\n")

print("✅ Comparison complete! Summary saved to motif_comparison_summary.txt")


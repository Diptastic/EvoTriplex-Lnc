from Bio import SeqIO
import csv
import os

# === Settings ===
# Update this to match your system path if needed
input_file = "D:/Project/EvoTriplex-Lnc/data/chimp_lncrna_sequences.fasta"
output_file = "D:/Project/EvoTriplex-Lnc/results/motifs_chimp.csv"
motif_length = 15
g_content_threshold = 0.7  # 70% G-rich

# === Motif Finder Function ===
def find_triplex_like_motifs(seq, motif_length):
    motifs = []
    for i in range(len(seq) - motif_length + 1):
        sub = seq[i:i+motif_length]
        g_count = sub.upper().count('G')
        if g_count >= motif_length * g_content_threshold:
            motifs.append((i, sub))
    return motifs

# === Scanner Function ===
def scan_fasta(input_fasta, output_csv):
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)

    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Sequence_ID", "Start_Pos", "Motif"])

        for record in SeqIO.parse(input_fasta, "fasta"):
            motifs = find_triplex_like_motifs(str(record.seq), motif_length)
            for start, motif in motifs:
                writer.writerow([record.id, start, motif])

    print(f"✅ Motif scan complete! Output saved to: {output_csv}")

# === Run the Scanner ===
if __name__ == "__main__":
    scan_fasta(input_file, output_file)

# 🧬 EvoTriplex-Lnc: Comparative Analysis of Triplex-Forming DNA Motifs in Long Non-Coding RNAs

**EvoTriplex-Lnc** is a comparative genomics project designed to identify and analyze **triplex-forming DNA motifs** in long non-coding RNAs (lncRNAs) across multiple species—specifically **human**, **chimp**, and **mouse**. The goal is to explore the evolutionary conservation and uniqueness of these regulatory elements and their potential roles in gene regulation.

---

## 📂 Project Structure

EvoTriplex-Lnc/
├── data/
│ ├── human_lncrna_sequences.fasta
│ ├── chimp_lncrna_sequences.fasta
│ └── mouse_lncrna_sequences.fasta
├── scripts/
│ ├── triplex_scanner.py
│ ├── motif_count_checker.py
│ ├── motif_comparator.py
│ ├── motif_venn.py
│ └── motif_barplot.py
├── results/
│ ├── motif_counts_barplot.png
│ ├── motif_overlap_venn.png
│ ├── motifs_human.csv
│ ├── motifs_chimp.csv
│ ├── motifs_mouse.csv
│ └── motif_comparison_summary.txt
├── draft.md
└── EvoTriplex-Lnc.md


---

## 🚀 Features

- 🔍 **Triplex motif scanning** using Python-based analysis
- 📊 **Motif count visualization** with bar plots
- 🔗 **Comparative analysis** across species using Venn diagrams
- 📁 Output in both visual (`.png`) and tabular (`.csv`, `.txt`) formats
- 📝 Includes a structured research-style documentation draft

---

## 🧪 Requirements

- Python 3.x
- Libraries:
  - `pandas`
  - `matplotlib`
  - `itertools`
  - `re`

Install with:
```bash
pip install pandas matplotlib
⚙️ How to Run
Place your .fasta files in the data/ directory.

Run the following scripts in sequence:

python scripts/triplex_scanner.py        # Scan each species' lncRNA for motifs
python scripts/motif_count_checker.py    # Count motifs and generate CSV
python scripts/motif_comparator.py       # Compare motifs across species
python scripts/motif_venn.py             # Create Venn diagram of overlaps
python scripts/motif_barplot.py          # Generate motif count barplot

📈 Sample Outputs
Motif Count Barplot
![motif_counts_barplot](https://github.com/user-attachments/assets/ab80bfaf-52a0-470a-9f27-3e2ae5fad739)



Motif Overlap Venn Diagram

![motif_overlap_venn](https://github.com/user-attachments/assets/b5356f9c-f561-4e47-89c7-9929faea7af6)



🧠 Purpose
This project aims to:

Identify evolutionarily conserved triplex motifs in lncRNAs.

Uncover species-specific regulatory patterns.

Provide a framework for functional motif discovery using comparative genomics.

📌 Citation
Note: This project is part of an upcoming publication. The code and results will be made public after peer-review. Please contact the author for more information.

📜 License
To be added after publication (e.g., MIT or Apache 2.0)
🤝 Contact
Author: [Deepyaman Dalal]
Email: [deepyamandalal@gmail.com]
Institution: Reva University, BSc Bioinformatics,Statistics & Computer Science


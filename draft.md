# Triplex-like Motif Explorer: Comparative Analysis of lncRNA Motifs

## Introduction

Long non-coding RNAs (lncRNAs) are known to regulate gene expression via diverse mechanisms, including the formation of triple helices with DNA. Triplex-forming motifs in lncRNAs have been implicated in epigenetic regulation, genome stability, and disease. This project investigates and compares such motifs across three species: **Human**, **Chimpanzee**, and **Mouse**, with a focus on unique and conserved triplex-like sequence patterns.

## Methods

### 1. Data Collection

- Genomic lncRNA data for each species was obtained in FASTA format.
- Sequences were sourced from public databases like Ensembl and NCBI.

### 2. Motif Identification

- Custom scripts using **Biopython** and **regular expressions** were employed to scan for user-defined triplex-forming motifs.
- Each identified motif was annotated with its species of origin and position within the sequence.

### 3. Analysis

- Motif counts were aggregated for each species.
- Shared and unique motifs across species were computed using set operations.
- Visualizations were generated using **matplotlib** and **matplotlib_venn**.

## Results

### Motif Count Comparison

The total number of unique triplex-like motifs identified per species is shown in the bar chart below:

![Motif Counts per Species](results/motif_counts_barplot.png)

- **Human:** 12 unique motifs
- **Chimpanzee:** 9 unique motifs
- **Mouse:** 3 unique motifs

Humans exhibit the highest number of unique motifs, possibly due to richer lncRNA annotations or evolutionary divergence.

---

### Overlap of Motifs Across Species

The Venn diagram illustrates shared and unique motifs among the three species:

![Motif Overlap Venn Diagram](results/motif_overlap_venn.png)

- 8 motifs are shared between **Human** and **Chimp**.
- 1 motif is common to **all three species**.
- Mouse shares fewer motifs, indicating higher divergence.

---

### Tabular Summary

| Species     | Unique Motif Count |
|-------------|--------------------|
| Human       | 12                 |
| Chimpanzee  | 9                  |
| Mouse       | 3                  |
| Shared (Human–Chimp) | 8        |
| Shared (All)         | 1        |

---

## Discussion

The analysis suggests a high degree of conservation of triplex-like motifs between Human and Chimpanzee, consistent with their evolutionary proximity. Mouse exhibits lower motif overlap and fewer unique motifs, potentially reflecting species-specific lncRNA evolution or sequence availability.

This pattern supports the hypothesis that some regulatory motifs are conserved among primates, while others are lineage-specific.

## Conclusion

- A motif scanner was implemented to identify triplex-like motifs in lncRNAs across species.
- Human and Chimp share a significant number of motifs.
- Mouse shows fewer overlaps, indicating divergence.
- These findings can aid further functional studies on regulatory RNAs and motif evolution.

## Future Work

- Expand analysis to more species (e.g., rat, dog).
- Integrate motif binding affinity prediction.
- Investigate functional annotation of overlapping motifs.

## Acknowledgments

This project was created as part of an undergraduate bioinformatics exploration using Biopython and visualization libraries in Python.

---

## References

- [Biopython Documentation](https://biopython.org/)
- [Matplotlib](https://matplotlib.org/)
- [matplotlib-venn](https://pypi.org/project/matplotlib-venn/)

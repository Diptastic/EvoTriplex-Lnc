import pandas as pd

files = {
    "Human": "results/motifs_human.csv",
    "Chimpanzee": "results/motifs_chimp.csv",
    "Mouse": "results/motifs_mouse.csv"
}

for species, path in files.items():
    try:
        df = pd.read_csv(path)
        total = len(df)
        unique = df['Motif'].nunique()
        print(f"{species}: {total} total motifs, {unique} unique motifs")
    except FileNotFoundError:
        print(f"{species}: File not found at {path}")

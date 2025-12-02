def to_rna(dna_strand):
    replacements = dna_strand.maketrans({"G": "C", "C": "G", "T": "A", "A": "U"})

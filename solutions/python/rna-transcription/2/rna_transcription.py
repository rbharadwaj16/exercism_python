def to_rna(dna_strand):
    #replacements = dna_strand.maketrans({"G": "C", "C": "G", "T": "A", "A": "U"})
    #return dna_strand.translate(replacements)
    #Incorporating code changes per the review
    replacements = dna_strand.maketrans('GCTA','CGAU')
    return dna_strand.translate(replacements)
    
        

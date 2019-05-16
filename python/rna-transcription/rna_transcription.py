def to_rna(dna_strand):
    complement_mapping = str.maketrans('GCTA', 'CGAU')
    return dna_strand.translate(complement_mapping)

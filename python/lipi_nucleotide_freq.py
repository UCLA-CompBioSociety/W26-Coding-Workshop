def nucleotide_freq(seq):
    base_freq = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for base in seq:
        base_freq[base] += 1

    return base_freq

def main():
    dna = "ATCTGATTACCGGGAC"
    print(nucleotide_freq(dna))
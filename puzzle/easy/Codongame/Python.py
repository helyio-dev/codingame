import sys

table = {
    'AUA': 'I', 'AUC': 'I', 'AUU': 'I', 'AUG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T',
    'AAC': 'N', 'AAU': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGU': 'S', 'AGA': 'R', 'AGG': 'R',
    'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',
    'CAC': 'H', 'CAU': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
    'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
    'GAC': 'D', 'GAU': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G',
    'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
    'UUC': 'F', 'UUU': 'F', 'UUA': 'L', 'UUG': 'L',
    'UAC': 'Y', 'UAU': 'Y', 'UGC': 'C', 'UGU': 'C', 'UGG': 'W'
}

stops = {'UAA', 'UAG', 'UGA'}
start = 'AUG'

def translate(rna, start_idx):
    stored_sequences = []
    current_seq = ""
    state = "CLOSED"
    
    for i in range(start_idx, len(rna) - 2, 3):
        codon = rna[i:i+3]
        if state == "CLOSED":
            if codon == start:
                state = "OPENED"
                current_seq += table[codon]
        else:
            if codon in stops:
                stored_sequences.append(current_seq)
                current_seq = ""
                state = "CLOSED"
            else:
                current_seq += table.get(codon, "")
                
    return stored_sequences

n = int(sys.stdin.readline())
for _ in range(n):
    rna = sys.stdin.readline().strip()
    results = []
    for offset in range(3):
        seqs = translate(rna, offset)
        total_len = sum(len(s) for s in seqs)
        results.append((total_len, "-".join(seqs)))
    
    print(max(results, key=lambda x: x[0])[1])
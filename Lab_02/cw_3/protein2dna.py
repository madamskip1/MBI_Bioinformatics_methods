import argparse
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio.Seq import Seq

protein2dna = {
    "A": ["GCA", "GCC", "GCG", "GCT"],
    "C": ["TGC", "TGT"],
    "D": ["GAC", "GAT"],
    "E": ["GAA", "GAG"],
    "F": ["TTC", "TTT"],
    "G": ["GGA", "GGC", "GGG", "GGT"],
    "H": ["CAC", "CAT"],
    "I": ["ATA", "ATC", "ATT"],
    "K": ["AAA", "AAG"],
    "L": ["CTA", "CTC", "CTG", "CTT", "TTA", "TTG"],
    "M": ["ATG"],
    "N": ["AAC", "AAT"],
    "P": ["CCA", "CCC", "CCG", "CCT"],
    "Q": ["CAA", "CAG"],
    "R": ["AGA", "AGG", "CGA", "CGC", "CGG", "CGT"],
    "S": ["AGC", "AGT", "TCA", "TCC", "TCG", "TCT"],
    "T": ["ACA", "ACC", "ACG", "ACT"],
    "V": ["GTA", "GTC", "GTG", "GTT"],
    "W": ["TGG"],
    "Y": ["TAC", "TAT"],
    "X": ["TAA", "TAG", "TGA"]
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    args = parser.parse_args()

    new_records = []

    with open(args.input_file, "r") as f:
        for record in SeqIO.parse(f, "fasta"):
            new_records.append(
                SeqRecord(
                    Seq("".join([protein2dna[x][0] for x in record.seq])),
                    id=record.id,
                    name=record.name,
                    description=record.description,
                )
            )

    SeqIO.write(new_records, args.output_file, "fasta")

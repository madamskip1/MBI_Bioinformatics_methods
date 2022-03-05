import argparse
from Bio import SeqIO

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    total_A = 0
    total_C = 0
    total_G = 0
    total_T = 0

    with open(args.input_file, "r") as f:
        for record in SeqIO.parse(f, "fasta"):
            count_A = record.seq.count("A")
            count_C = record.seq.count("C")
            count_G = record.seq.count("G")
            count_T = record.seq.count("T")

            total_A += count_A
            total_C += count_C
            total_G += count_G
            total_T += count_T

            print("GC-content of", record.name, (count_G + count_C) / (count_A + count_C + count_G + count_T))

    print("GC-content", (total_G + total_C) / (total_A + total_C + total_G + total_T))

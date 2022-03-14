import argparse
from io import StringIO
import pyranges as pr
import pandas as pd
from tqdm import tqdm

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ref_flat_file")
    parser.add_argument("vcf_file")
    args = parser.parse_args()

    with open(args.vcf_file) as f:
        lines = [x for x in f.readlines() if x[0] != "#"]

    vcf = pd.read_csv(StringIO("\n".join(lines)), sep="\t", names=["Chromosome", "POS", "ID", "REF", "ALT", "QUAL", "FILTER", "INFO", "FORMAT", ""])
    ref = pr.PyRanges(pd.read_csv(args.ref_flat_file, sep="\t", names=["GeneName", "Name", "Chromosome", "Strand", "Start", "End", "cdsStart", "cdsEnd", "exonCount", "exonStarts", "exonEnds"]))

    counter = {}

    for _, row in tqdm(vcf.iterrows(), total=len(vcf)):
        idx = row["POS"]

        for _, row2 in ref[idx:idx + 1].df.iterrows():
            gene = row2["Name"]

            if gene in counter:
                counter[gene] += 1
            else:
                counter[gene] = 1

    out = pd.DataFrame(counter.items(), columns=["Gene", "Count"])
    out.to_csv("out.csv", index=False)

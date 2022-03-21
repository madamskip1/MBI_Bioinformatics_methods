import argparse

import pandas as pd
from tqdm import tqdm

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("cnv_file")
    parser.add_argument("dgv_file")
    args = parser.parse_args()

    cnv = pd.read_csv(args.cnv_file)
    dgv = pd.read_csv(args.dgv_file, sep="\t")

    cnv["del_count"] = 0
    cnv["dup_count"] = 0
    cnv["del_dup_80_percent_count"] = 0

    cnv_grouped = [(name.lower(), rows) for name, rows in cnv.groupby("sample_name")]

    for _, row in tqdm(dgv.iterrows(), total=len(dgv)):
        c = row["variantsubtype"]

        if c == "deletion":
            c = "del"
        elif c == "duplication":
            c = "dup"
        else:
            continue

        samples = str(row["samples"]).lower().split(",")
        dgv_start = row["start"]
        dgv_end = row["end"]
        dgv_length = dgv_end - dgv_start

        for name, rows in cnv_grouped:
            if not name in samples:
                continue

            for i, row in rows.iterrows():
                if c != row["cnv"]:
                    continue

                cnv_start = row["st_bp"]
                cnv_end = row["ed_bp"]
                cnv_length = cnv_end - cnv_start

                max_start = max(dgv_start, cnv_start)
                min_end = min(dgv_end, cnv_end)

                if max_start < min_end:
                    intersection_length = min_end - max_start
                    intersection_percent = intersection_length / dgv_length

                    if c == "del":
                        cnv.loc[i, "del_count"] += 1
                    elif c == "dup":
                        cnv.loc[i, "dup_count"] += 1

                    if intersection_percent > 0.8:
                        cnv.loc[i, "del_dup_80_percent_count"] += 1

    cnv[["sample_name", "st_bp", "ed_bp", "cnv", "del_count", "dup_count", "del_dup_80_percent_count"]].to_csv("out.csv", index=False)

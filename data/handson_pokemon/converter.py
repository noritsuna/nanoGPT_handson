import pandas as pd
import os
import argparse
import json
from tqdm import tqdm

def convert_parquet_to_text(parquet_path, output_file):
    """
    Converts all fields from a Parquet file to a text file.
    """

    df = pd.read_parquet(parquet_path)

    with open(output_file, 'w', encoding='utf-8') as f:
        for _, row in df.iterrows():
            for column in df.columns:
                value = row[column]
                if isinstance(value, list):
                    value = ' '.join(value)  # Join list elements with spaces
                f.write(f"{column}: {value}\n")
            f.write('\n')  # Separator between rows

    print(f"Converted Parquet file '{parquet_path}' to text file '{output_file}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert Parquet file to a text file with all fields."
    )
    parser.add_argument(
        "parquet_file",
        type=str,
        help="Path to the Parquet file to convert.",
    )
    parser.add_argument(
        "-o",
        "--output_file",
        type=str,
        default="output.txt",
        help="Path to the output text file.",
    )
    args = parser.parse_args()

    convert_parquet_to_text(args.parquet_file, args.output_file)


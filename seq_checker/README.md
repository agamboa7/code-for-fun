# Sequence Checker

This is a Python script that compares amino acid sequences between two FASTA files. It checks whether each sequence in a target file is also present in a reference file. 

This script was developed to verify the correctness of filtered or processed FASTA files by ensuring that all sequences originate from the original dataset.

## How It Works

- The script ignores header lines (those starting with `>`).
- It compares only the sequences (i.e., the amino acid strings).
- For each sequence in the target file, it prints `True` if that sequence is present in the reference file, and `False` otherwise.

## Sample Files

In this repository, you will find two sample FASTA files to test the script:

- `ref_seqs.fasta`: Contains a set of original sequences.
- `check_seqs.fasta`: Contains sequences to be checked.

These files allow you to try out the script and understand its functionality.

## How to Use

To run the script, use the following command in your terminal:

```bash
python seq_checker.py ref_seqs.fasta check_seqs.fasta
```

Replace `ref_seqs.fasta` and `check_seqs.fasta` with your own file names if needed.

The script will output `True` or `False` for each sequence in the second file, indicating whether it was found in the reference file.

## Requirements

- Python 3.x
- No external libraries are needed to run this script.

## Notes

- This script assumes that sequences are written in single lines (i.e., no line wrapping).
- It is intended for simple validation and debugging purposes.
- You are free to modify or extend it for more complex checks.


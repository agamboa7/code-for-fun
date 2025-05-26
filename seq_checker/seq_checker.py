#!/usr/bin/env python3
# Author: Andrea Arriola Gamboa
# Python version: 3.12.9

"""
seq_checker.py

This script compares the sequences (not headers) in two FASTA files.
It checks if each sequence in the second file exists in the reference file
and prints True or False accordingly.

Usage:
    python seq_checker.py <reference_fasta> <file_to_check>

Example:
    python seq_checker.py all_sequences.fasta filtered_sequences.fasta
"""

from sys import argv

def seq_checker(reference_path, check_path):
    """
    Compare sequences between two FASTA files and print whether
    each sequence in the second file exists in the first.

    Parameters:
        reference_path (str): Path to the reference FASTA file.
        check_path (str): Path to the FASTA file to check.
    """
    # Store reference sequences (ignore headers) in a list
    with open(reference_path, "r") as ref_file:
        reference_sequences = []
        for line in ref_file:
            line = line.strip()
            if line[0] != ">":
                reference_sequences.append(line)

    # Check sequences in the second file
    with open(check_path, "r") as check_file:
        seq_number = 0
        match_count = 0
        for line in check_file:
            line = line.strip()

            if not line or line.startswith(">"):
                continue  # Skip empty or header lines

            if line in reference_sequences:
                seq_number = seq_number + 1
                match_count = match_count + 1
                print(f"Seq {seq_number}: True")
            else:
                seq_number = seq_number + 1
                print(f"Seq {seq_number}: False")
                
        # Print the total number of matches
        print(f"\nTotal matches: {match_count}/{seq_number}")


if __name__ == "__main__":
    if len(argv) != 3:
        print("ERROR: This program takes two FASTA files as arguments.")
        print("Usage: python seq_checker.py <reference_fasta> <file_to_check>")
        exit(1)
    else:
        seq_checker(argv[1], argv[2])

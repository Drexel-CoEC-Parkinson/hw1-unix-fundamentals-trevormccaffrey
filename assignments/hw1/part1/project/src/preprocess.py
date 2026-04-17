#!/usr/bin/env python3
"""Preprocessing script for sensor data."""

import argparse
import csv
import sys

def parse_args():
    parser = argparse.ArgumentParser(description="Preprocess sensor data")
    parser.add_argument("input_file", help="Input CSV file")
    parser.add_argument("-o", "--output", help="Output file", default="processed.csv")
    parser.add_argument("--normalize", action="store_true", help="Normalize readings")
    parser.add_argument("--drop-missing", action="store_true", help="Remove missing values")
    return parser.parse_args()

def main():
    args = parse_args()
    print(f"Preprocessing: {args.input_file}")
    if args.normalize:
        print("  Normalizing readings...")
    if args.drop_missing:
        print("  Dropping rows with missing values...")
    print(f"  Output: {args.output}")
    print("Preprocessing complete.")

if __name__ == "__main__":
    main()

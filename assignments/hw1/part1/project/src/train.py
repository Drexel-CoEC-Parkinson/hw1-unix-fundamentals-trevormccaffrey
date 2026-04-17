#!/usr/bin/env python3
"""Training script for sensor classification model."""

import argparse
import sys

def parse_args():
    parser = argparse.ArgumentParser(description="Train the model")
    parser.add_argument("--epochs", type=int, default=50)
    parser.add_argument("--lr", type=float, default=3e-4)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--data-dir", type=str, default="./data")
    parser.add_argument("--output-dir", type=str, default="./models")
    return parser.parse_args()

def main():
    args = parse_args()
    print(f"Training for {args.epochs} epochs with lr={args.lr}")
    print(f"Data directory: {args.data_dir}")
    print(f"Output directory: {args.output_dir}")
    # ... training logic would go here ...
    print("Training complete.")

if __name__ == "__main__":
    main()

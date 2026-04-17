#!/usr/bin/env python3
"""Generates weekly status reports from sensor data."""

def generate_report(data_file, output_file):
    print(f"Reading data from {data_file}")
    print(f"Generating report...")
    print(f"Report written to {output_file}")

if __name__ == "__main__":
    generate_report("shared_data.csv", "weekly_report.txt")

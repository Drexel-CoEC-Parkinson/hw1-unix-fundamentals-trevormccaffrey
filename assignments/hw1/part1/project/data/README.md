# Sensor Classification Dataset

## Overview
This dataset contains labeled sensor readings for a classification task.
Three CSV files are provided: training, validation, and test splits.

## Format
Each CSV file has the following columns:
- `id` — Unique identifier for the reading
- `timestamp` — ISO 8601 timestamp
- `sensor_id` — Identifier for the sensor
- `reading` — Numeric sensor value
- `unit` — Unit of measurement
- `status` — One of: ok, warn, error, missing

## Splits
- `train.csv` — 35,000 samples (70%)
- `val.csv` — 7,500 samples (15%)
- `test.csv` — 7,500 samples (15%)

## Citation
If you use this dataset, please cite: [internal project, no citation needed]

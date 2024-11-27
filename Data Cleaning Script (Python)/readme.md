# Data Cleaning Script

This is a Python script for cleaning and preprocessing datasets. The script is designed to be flexible, user-friendly, and interactive .

## Features
- Removes duplicate rows.
- Handles missing values:
  - Fills numerical columns with the median value.
  - Fills categorical columns with the most frequent value.
- Removes outliers using the Z-score method.
- Standardizes column names to lowercase with underscores instead of spaces.
- Allows users to interactively specify columns to drop.
- Automatically converts date/time columns to datetime format.
- Saves the cleaned dataset to a user-specified output file.

## Prerequisites
- Python 3.x
- Required libraries: `pandas`, `numpy`, `scipy`


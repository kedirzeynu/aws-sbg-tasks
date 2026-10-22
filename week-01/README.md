# Week 01 — Student Data Processing App

## Overview

This project is a small Python data-processing application.
It loads student records from a CSV file, cleans the data,
calculates statistics using NumPy, and saves the results.

## Features

- Loads CSV data using pandas.
- Standardizes text and department names.
- Converts numeric columns to numeric types.
- Removes duplicate student records.
- Fills missing scores using the median.
- Fills missing ages using the mean.
- Removes records with scores outside 0–100.
- Calculates statistics using NumPy.
- Saves cleaned data and a summary report.

## Technologies

- Python
- NumPy
- pandas
- Jupyter Notebook / Google Colab

## Project Structure

```text
week-01/
├── README.md
├── data/
│   └── students.csv
├── output/
│   ├── cleaned_students.csv
│   └── summary.txt
├── task.py
└── task.ipynb
```

## Setup

From the repository root, create and activate a virtual
environment.

Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run the Python Script

From the repository root:

```bash
python week-01/task.py
```

## Run the Notebook

Open `task.ipynb` in Jupyter Notebook or upload it
to Google Colab. Run all cells from top to bottom.

## Output

The application generates:

- `output/cleaned_students.csv`
- `output/summary.txt`

These files contain the cleaned records and descriptive
statistics.

## Data Cleaning Decisions

Missing scores are replaced with the median of valid
scores. Missing ages are replaced with the mean age.
Duplicate records are identified using student name,
department, score, and age. Scores outside 0–100 are
removed.

## Learning Outcomes

This project demonstrates Python functions, CSV
processing, basic pandas operations, NumPy statistics,
virtual environments, dependency management, and GitHub.
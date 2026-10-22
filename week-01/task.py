from pathlib import Path

import numpy as np
import pandas as pd


# Paths relative to this Python file
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "students.csv"
OUTPUT_DIR = BASE_DIR / "output"


def load_data(file_path):
    """Load a CSV dataset into a pandas DataFrame."""
    return pd.read_csv(file_path)


def clean_text(data):
    """Remove extra spaces and standardize text capitalization."""
    data = data.copy()

    data["name"] = data["name"].str.strip().str.title()
    data["department"] = (
        data["department"]
        .str.strip()
        .str.title()
    )

    return data


def convert_types(data):
    """Convert numeric columns to appropriate numeric types."""
    data = data.copy()

    for column in ["student_id", "score", "age"]:
        data[column] = pd.to_numeric(
            data[column], errors="coerce"
        )

    return data


def remove_duplicates(data):
    """Remove duplicate student records."""
    return data.drop_duplicates(
        subset=["name", "department", "score", "age"],
        keep="first",
    ).copy()


def clean_missing_values(data):
    """Fill missing scores with the median and ages with the mean."""
    data = data.copy()

    valid_scores = data.loc[
        data["score"].between(0, 100), "score"
    ]
    median_score = valid_scores.median()

    if pd.isna(median_score):
        raise ValueError("No valid scores are available.")

    data["score"] = data["score"].fillna(median_score)

    mean_age = data["age"].mean()
    if pd.isna(mean_age):
        raise ValueError("No valid ages are available.")

    data["age"] = data["age"].fillna(round(mean_age))

    return data


def remove_invalid_scores(data):
    """Keep scores between 0 and 100, inclusive."""
    data = data.copy()

    valid = data["score"].between(0, 100)
    return data.loc[valid].copy()


def calculate_statistics(data):
    """Calculate descriptive statistics using NumPy."""
    scores = data["score"].to_numpy(dtype=float)

    if scores.size == 0:
        raise ValueError("Cannot calculate statistics on empty data.")

    return {
        "Number of students": int(scores.size),
        "Mean score": float(np.mean(scores)),
        "Median score": float(np.median(scores)),
        "Standard deviation": float(np.std(scores)),
        "90th percentile": float(np.percentile(scores, 90)),
        "Minimum score": float(np.min(scores)),
        "Maximum score": float(np.max(scores)),
    }


def save_results(data, statistics):
    """Save cleaned records and a text summary."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    cleaned_file = OUTPUT_DIR / "cleaned_students.csv"
    summary_file = OUTPUT_DIR / "summary.txt"

    data.to_csv(cleaned_file, index=False)

    with summary_file.open("w", encoding="utf-8") as file:
        file.write("STUDENT DATA PROCESSING SUMMARY\n")
        file.write("=" * 35 + "\n\n")

        for name, value in statistics.items():
            if isinstance(value, float):
                file.write(f"{name}: {value:.2f}\n")
            else:
                file.write(f"{name}: {value}\n")

    print(f"Cleaned data saved to: {cleaned_file}")
    print(f"Summary saved to: {summary_file}")


def main():
    """Run the complete data-processing workflow."""
    print("STUDENT DATA PROCESSING APP")
    print("=" * 35)

    # Step 1: Load the original dataset.
    data = load_data(DATA_FILE)
    print(f"\nOriginal rows: {len(data)}")

    # Step 2: Clean text and convert numeric columns.
    data = clean_text(data)
    data = convert_types(data)

    # Step 3: Remove duplicate records.
    before = len(data)
    data = remove_duplicates(data)
    print(f"Duplicate records removed: {before - len(data)}")

    # Step 4: Replace missing values.
    data = clean_missing_values(data)

    # Step 5: Remove invalid scores.
    before = len(data)
    data = remove_invalid_scores(data)
    print(f"Invalid-score records removed: {before - len(data)}")

    # Step 6: Calculate statistics using NumPy.
    statistics = calculate_statistics(data)

    print("\nCLEANED DATA")
    print(data.to_string(index=False))

    print("\nSTATISTICS")
    for name, value in statistics.items():
        if isinstance(value, float):
            print(f"{name}: {value:.2f}")
        else:
            print(f"{name}: {value}")

    # Step 7: Save results.
    save_results(data, statistics)


if __name__ == "__main__":
    main()
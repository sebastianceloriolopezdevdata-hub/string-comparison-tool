import pandas as pd


def extract_data():
    """Extracts string pairs from the input CSV file."""
    file_path = "data/raw/input.csv"

    df = pd.read_csv(file_path)

    return list(zip(df["input_one"], df["input_two"]))


def write_output(results):
    """Writes similarity results to the output CSV file."""
    file_path = "data/processed/output.csv"

    df = pd.DataFrame(
        results,
        columns=["input_one", "input_two", "H", "J", "T"]
    )

    df.to_csv(file_path, index=False)
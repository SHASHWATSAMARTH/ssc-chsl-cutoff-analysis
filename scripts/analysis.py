

import pandas as pd
import matplotlib.pyplot as plt


def load_data(filepath):
    """Load cutoff data from CSV file."""
    return pd.read_csv(filepath)


def summarize_by_post(df):
    """Compute average cut-off by post."""
    return df.groupby("post")["cutoff"].mean()


def summarize_by_category(df):
    """Compute average cut-off by category."""
    return df.groupby("category")["cutoff"].mean()


def main():
    data_path = "../data/ssc_chsl_cutoff_data.csv"
    df = load_data(data_path)

    print("Average Cut-off by Post:")
    print(summarize_by_post(df))

    print("\nAverage Cut-off by Category:")
    print(summarize_by_category(df))


if __name__ == "__main__":
    main()

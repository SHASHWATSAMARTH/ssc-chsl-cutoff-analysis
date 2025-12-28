

import pandas as pd
import matplotlib.pyplot as plt


def load_data(filepath):
    return pd.read_csv(filepath)


def plot_cutoff_by_post(df):
    plt.figure()
    for post in df["post"].unique():
        subset = df[df["post"] == post]
        yearly_avg = subset.groupby("year")["cutoff"].mean()
        plt.plot(yearly_avg.index, yearly_avg.values, label=post)

    plt.xlabel("Year")
    plt.ylabel("Cut-off Marks")
    plt.title("Post-wise SSC CHSL Cut-off Trends (2019–2023)")
    plt.legend()
    plt.show()


def plot_cutoff_by_category(df):
    plt.figure()
    for category in df["category"].unique():
        subset = df[df["category"] == category]
        yearly_avg = subset.groupby("year")["cutoff"].mean()
        plt.plot(yearly_avg.index, yearly_avg.values, label=category)

    plt.xlabel("Year")
    plt.ylabel("Cut-off Marks")
    plt.title("Category-wise SSC CHSL Cut-off Trends (2019–2023)")
    plt.legend()
    plt.show()


def plot_crowd_vs_cutoff(df):
    plt.figure()
    plt.scatter(df["candidates"], df["cutoff"])
    plt.xlabel("Number of Candidates")
    plt.ylabel("Cut-off Marks")
    plt.title("Competition Density vs Cut-off")
    plt.show()


def main():
    data_path = "../data/ssc_chsl_cutoff_data.csv"
    df = load_data(data_path)

    plot_cutoff_by_post(df)
    plot_cutoff_by_category(df)
    plot_crowd_vs_cutoff(df)


if __name__ == "__main__":
    main()

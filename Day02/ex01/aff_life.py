from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def main():
    data = load("life_expectancy_years.csv")
    morocco = data[data["country"] == "Morocco"].set_index("country").T
    morocco.columns = ["life expectancy"]
    morocco.index.name = "year"
    morocco = morocco.reset_index()
    morocco["year"] = morocco["year"].astype(int)
    morocco.plot(
        x="year",
        y="life expectancy",
        title="Morocco Life expectancy Projections",
        kind='line',
        xlabel="year",
        ylabel="life expectancy")
    plt.show()



if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"Error: {error}")
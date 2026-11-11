import pandas as pd
from load_csv import load
import matplotlib.pyplot as plt


def main():
    data = load("population_total.csv")
    countries = ["Belgium", "France"]
    selected = data[data["country"].isin(countries)]
    selected = selected.set_index("country").T
    selected.index.name = "year"
    selected = selected.reset_index()
    selected["year"] = selected["year"].astype(int)
    for country in countries:
        selected[country] = (
            selected[country].str.replace("M", "", regex=False)
            .astype(float) * 1_000_000
        )
    selected.plot(
        x="year",
        y=countries,
        title="Population Projections",
        xlabel="Year",
        ylabel="Population"
    )
    plt.xlim(1800, 2050)
    plt.show()

    


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"Error: {error}")
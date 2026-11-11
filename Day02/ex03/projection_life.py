from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def main():
    gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expectancy = load("life_expectancy_years.csv")

    data = pd.merge(
        gdp[["country", "1900"]],
        life_expectancy[["country", "1900"]],
        on="country",
        suffixes=("_gdp", "_life"),
    ).dropna()

    plt.scatter(data["1900_gdp"], data["1900_life"])
    plt.title("1900")
    plt.xlabel("Gross national product")
    plt.ylabel("Life expectancy")
    plt.xscale("log")
    plt.legend(["1900"])
    plt.show()

if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"Error: {error}")

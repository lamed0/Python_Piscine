from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def parse_value(val) -> float:
    """Parse numeric values that might have k/M suffixes."""
    if pd.isna(val):
        return float("nan")
    if isinstance(val, (int, float)):
        return float(val)
    val = str(val).strip()
    if val.endswith("k") or val.endswith("K"):
        return float(val[:-1]) * 1_000
    if val.endswith("M") or val.endswith("m"):
        return float(val[:-1]) * 1_000_000
    return float(val)


def main():
    """Plot GDP vs Life Expectancy for the year 1900."""
    gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expectancy = load("life_expectancy_years (1).csv")

    if gdp is None or life_expectancy is None:
        raise AssertionError("Failed to load dataset.")

    if "1900" not in gdp.columns or "1900" not in life_expectancy.columns:
        raise AssertionError("Year 1900 column missing from dataset.")

    gdp_1900 = gdp[["country", "1900"]].copy()
    gdp_1900["1900"] = gdp_1900["1900"].apply(parse_value)

    life_1900 = life_expectancy[["country", "1900"]].copy()
    life_1900["1900"] = life_1900["1900"].apply(parse_value)

    data = pd.merge(
        gdp_1900,
        life_1900,
        on="country",
        suffixes=("_gdp", "_life"),
    ).dropna()

    plt.scatter(data["1900_gdp"], data["1900_life"])
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")
    plt.xscale("log")
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"Error: {error}")

from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Load life expectancy data and plot projections for Morocco."""
    data = load("life_expectancy_years (1).csv")
    if data is None:
        raise AssertionError("Failed to load dataset.")

    morocco_data = data[data["country"] == "Morocco"]
    if morocco_data.empty:
        raise AssertionError("Country not found in dataset.")

    years = morocco_data.columns[1:].astype(int)
    values = morocco_data.values[0][1:]

    plt.plot(years, values)
    plt.title("Morocco Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.xticks(range(1800, 2101, 40))
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"Error: {error}")

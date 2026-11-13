from load_csv import load
import matplotlib.pyplot as plt


def parse_population(value: str) -> float:
    """Convert population string with suffixes (k, M, B) to float."""
    if isinstance(value, (int, float)):
        return float(value)
    value = str(value).strip()
    if value.endswith("k") or value.endswith("K"):
        return float(value[:-1]) * 1_000
    if value.endswith("M") or value.endswith("m"):
        return float(value[:-1]) * 1_000_000
    if value.endswith("B") or value.endswith("b"):
        return float(value[:-1]) * 1_000_000_000
    return float(value)


def main():
    """Load population data and plot comparison between Morocco and France."""
    data = load("population_total.csv")
    if data is None:
        raise AssertionError("Failed to load dataset.")

    morocco_data = data[data["country"] == "Morocco"]
    spain_data = data[data["country"] == "Spain"]

    if morocco_data.empty or spain_data.empty:
        raise AssertionError("Required country not found in dataset.")

    years = [year for year in data.columns[1:] if 1800 <= int(year) <= 2050]
    years_int = [int(y) for y in years]

    morocco_pop = [parse_population(morocco_data[y].values[0]) for y in years]
    spain_pop = [parse_population(spain_data[y].values[0]) for y in years]

    plt.plot(years_int, morocco_pop, label="Morocco", color="blue")
    plt.plot(years_int, spain_pop, label="Spain", color="green")

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.xlim(1790, 2050)
    plt.xticks(range(1800, 2051, 40))

    max_val = max(max(morocco_pop), max(spain_pop))
    step = 20_000_000
    ticks = list(range(step, int(max_val) + step, step))
    plt.yticks(ticks, [f"{int(t / 1_000_000)}M" for t in ticks])

    plt.legend(loc="lower right")
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"Error: {error}")

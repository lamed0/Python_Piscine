

def ft_tqdm(lst: range) -> None:
    """Yield items while displaying their progress through the iterable."""
    total = len(lst)

    for count, item in enumerate(lst, start=1):
        progress = count / total
        completed = int(progress * 50)
        bar = "=" * completed + ">" + " " * (49 - completed)
        print(
            f"\r{progress:>3.0%}|{bar}| {count}/{total}",
            end="",
        )
        yield item

    print()

import datetime


time = datetime.datetime.now() - datetime.datetime(1970, 1, 1, 0, 0, 0)
seconds = time.total_seconds()
formatted_seconds = format(seconds, ",.4f")
scientific_notation = format(seconds, ".2e")


print(
    "Seconds since January 1, 1970:", formatted_seconds, "or",
    scientific_notation, "in scientific notation"
)

month = datetime.datetime.now()
day = datetime.datetime.now().day
year = datetime.datetime.now().year

print(month.strftime("%b"), end=" ")
print(day, year)

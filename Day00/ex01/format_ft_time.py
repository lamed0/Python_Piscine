import time
from datetime import datetime

current_time = time.time()
now = datetime.now()

print(
    f"Seconds since January 1, 1970: {current_time:,.4f} or "
    f"{current_time:.2e} in scientific notation"
)
print(now.strftime("%b %d %Y"))
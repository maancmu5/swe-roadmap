import csv
import urllib.request
from io import StringIO

URL = "https://stooq.com/q/d/l/?s=%5Espx&i=d"  # S&P 500 daily CSV

def get_latest_and_previous_close():
    with urllib.request.urlopen(URL) as resp:
        text = resp.read().decode("utf-8")

    reader = csv.DictReader(StringIO(text))
    rows = list(reader)

    if len(rows) < 2:
        raise RuntimeError("Not enough data to compare.")

    latest = rows[-1]
    previous = rows[-2]

    latest_date = latest["Date"]
    latest_close = float(latest["Close"])
    previous_close = float(previous["Close"])

    return latest_date, latest_close, previous_close

if __name__ == "__main__":
    date, close, prev_close = get_latest_and_previous_close()

    change = close - prev_close
    percent_change = (change / prev_close) * 100

    direction = "UP 📈" if change >= 0 else "DOWN 📉"

    print(f"S&P 500 (^SPX) close on {date}: {close:,.2f}")
    print(f"Change vs prior close: {change:+.2f} points ({percent_change:+.2f}%) {direction}")

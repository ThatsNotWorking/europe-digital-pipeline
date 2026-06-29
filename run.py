from get import get
from clean import clean
from store import store
from config import countries, indicators

all_rows = []

for country in countries:
    for indicator in indicators:
        url = f"https://api.worldbank.org/v2/country/{country}/indicator/{indicator}?format=json"
        rows = clean(get(url))

        all_rows.extend(rows)

store(all_rows)
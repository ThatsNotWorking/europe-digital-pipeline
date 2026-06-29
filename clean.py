from get import get

def clean(data):
    rows=[]

    for entry in data[1]:
        country = entry["countryiso3code"]
        indicator = entry["indicator"]["id"]
        year = entry["date"]
        value = entry["value"]
        rows.append((country, indicator, year, value))

    return rows

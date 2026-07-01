import sqlite3 as sq
import pandas as pd
import matplotlib.pyplot as plt

def analyze():
    conn = sq.connect("data/data.db")
    df = pd.read_sql_query("select * from indicators where indicator = 'IT.NET.USER.ZS' and value is not null order by year", conn)
    conn.close()

    for country in df["country"].unique():
        subset = df[df["country"] == country]
        plt.plot(subset["year"], subset["value"], label=country)

    plt.legend()
    plt.title("Internet adoption across Europe")
    plt.xlabel("year")
    plt.ylabel("% of population using the internet")
    plt.savefig("outputs/internet_adoption.png")
    plt.show()

def analyze_italy():
    conn = sq.connect("data/data.db")
    df = pd.read_sql_query("select * from indicators where indicator = 'IT.NET.USER.ZS' and value is not null order by year", conn)
    conn.close()

    for country in df["country"].unique():
        subset = df[df["country"] == country]
        if country == "ITA":
            plt.plot(subset["year"], subset["value"], label=country, color="red", linewidth=2.5)
        else:
            plt.plot(subset["year"], subset["value"], color="lightgrey", linewidth=1)

    plt.legend()
    plt.title("Italy's internet catch-up")
    plt.xlabel("year")
    plt.ylabel("% of population using the internet")
    plt.savefig("outputs/italy_internet.png")
    plt.show()

def analyze_tech():
    plt.figure()
    conn = sq.connect("data/data.db")

    rnd = pd.read_sql_query("select country, value from indicators where indicator = 'GB.XPD.RSDV.GD.ZS' and year = 2020", conn)
    tech = pd.read_sql_query("select country, value from indicators where indicator = 'TX.VAL.TECH.MF.ZS' and year = 2020", conn)
    conn.close()

    merged = rnd.merge(tech, on="country", suffixes=("_rnd", "_tech"))

    plt.scatter(merged["value_rnd"], merged["value_tech"])
    for country, x, y in zip(merged["country"], merged["value_rnd"], merged["value_tech"]):
        plt.annotate(country, (x, y))

    plt.title("High-tech exports vs R&D spending (2020)")
    plt.xlabel("R&D expenditure (% of GDP)")
    plt.ylabel("High-tech exports (% of manufactured exports)")
    plt.savefig("outputs/tech_vs_rnd.png")
    plt.show()

analyze()
analyze_italy()
analyze_tech()
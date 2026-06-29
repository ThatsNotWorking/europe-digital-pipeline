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
    plt.title("Italy's internet catch-up vs the rest of Europe")
    plt.xlabel("year")
    plt.ylabel("% of population using the internet")
    plt.savefig("outputs/italy_internet.png")
    plt.show()

analyze()
analyze_italy()
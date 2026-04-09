import requests
import pandas as pd
from pathlib import Path

def get_country_metadata():
    """
    Fetch basic country metadata from REST Countries API and save to CSV.
    Returns a dataframe created by Pandas library
    """
    url = "https://restcountries.com/v3.1/all?fields=name,cca3,region,subregion,population"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    rows = []
    for c in data:
        name = c["name"]["common"]
        cca3 = c.get("cca3")
        region = c.get("region")
        subregion = c.get("subregion")
        population = c.get("population")
        rows.append({
            "Country": name,
            "Country_Code": cca3,
            "Region": region,
            "Sub-region": subregion,
            "Population": population
        })

    df = pd.DataFrame(rows)

    data_dir = Path("data")
    data_dir.mkdir(parents=True, exist_ok=True)
    out_path = data_dir / "country_metadata.csv"
    df.to_csv(out_path, index=False)

    print(f"Saved {len(df)} rows to {out_path}")
    return df
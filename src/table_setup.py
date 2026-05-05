import pandas as pd
from pathlib import Path #AI generated

DATA_DIR = Path("data") #AI generated

def build_merged_dataset() -> pd.DataFrame:
    DATA_DIR.mkdir(exist_ok=True) #AI Generated
    #Import work_hours CSV
    work_path = DATA_DIR / "annual-working-hours-per-worker.csv"
    time_df = pd.read_csv(work_path)
    #Rename Columns
    time_df = time_df.rename(columns={
    "Entity": "country",
    "Year": "year",
    "Working hours per worker": "work_hours"
    })
    time_recent = time_df[time_df["year"] >= 2015].copy()
    work_country = (
        time_recent.groupby("country", as_index=False)["work_hours"].mean()
    )

    #Import world_happiness CSV
    happiness_path = "data/WHR26_Data_Figure_2.1.csv"
    happiness_df = pd.read_csv(happiness_path)
    happiness_df = happiness_df.rename(columns={
        "Country name": "country",
        "Life evaluation (3-year average)": "happiness_score",
    })
    happiness_df = happiness_df[["country", "happiness_score"]]

    #Merge happiness_df with work_country_df
    merged = pd.merge(work_country, happiness_df, on="country", how="inner")

    #Adding country_metadata.csv into the merged dataset
    meta_path = "data/country_metadata.csv"
    meta_df = pd.read_csv(meta_path)
    merged_all = pd.merge(
        merged,
        meta_df,
        left_on="country",
        right_on="Country",
        how="left"
    )

    #save combined dataset
    out_path = "data/merged_work_happiness_countries.csv"
    merged_all.to_csv(out_path, index=False)
    print(f"Saved Merged Dataset to {out_path} with {len(merged_all)} rows")
    return merged_all
from API_Call import get_country_metadata
from DSCI510.DSCI510_Spring2026_Final_Project.analysis import clustering_and_regression
from table_setup import build_merged_dataset
from analysis import load_merged, basic_eda, clustering_and_regression

if __name__ == "__main__":
    print("Running tests for API_Call:")

    table = get_country_metadata()
    print(table)

    build = build_merged_dataset()

    merged_data = load_merged()

    basic_eda(merged_data)

    clustering_and_regression(merged_data)

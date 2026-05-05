# Work–Leisure Balance and Happiness Across Countries

This project explores how the balance between annual working hours and national happiness levels varies across countries.

## Project Introduction

- **Goal:** Investigate how annual working hours per worker relate to life evaluation / happiness scores at the country level.

## Data Sources

| Data Source # | Name / Short Description    | Source URL                                                                 | Type              | List of Fields                                                                                                                                   | Format | Est. Data Size     |
|---------------|----------------------------|----------------------------------------------------------------------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|--------|--------------------|
| 1             | International Time-Use Data | https://ourworldindata.org/grapher/annual-working-hours-per-worker.csv?v=1&csvType=full&useColumnShortNames=false                                      | Webpage w/ File   | country, year, hours_work, hours_leisure, hours_personal_care, hours_sleep                                                                       | CSV    | 500–2,000 rows     |
| 2             | World Happiness Report      | https://files.worldhappiness.report/WHR26_Data_Figure_2.1.xlsx                                        | Webpage w/ File   | Happiness score, gdp (statistics of GDP), healthy_life_expectancy, social_support, freedom, generosity, corruption_perception, positive/negative_affect | CSV/XML | 500–1,000 rows     |
| 3             | Country Metadata            | https://restcountries.com/v3.1/all?fields=name,cca3,region,subregion,population              | API               | name, country_code, region, subregion, population, possibly income_level                                                                         | JSON   | ≈200 countries     

## Analysis

- **Description:** In this project, I combined country‑level data on annual working hours per worker, life‑evaluation scores from the World Happiness Report, and country metadata (region, subregion, population) to study how work time relates to national happiness across countries. After cleaning and merging these sources into a single dataset, I performed exploratory data analysis, starting with scatter plots and correlation measures to assess the overall relationship between working hours and happiness, which showed a generally negative association but with substantial variation. To capture more nuanced patterns, I applied K‑Means clustering to the standardized work‑hours and happiness variables, identifying four distinct “work–happiness profiles,” including low‑work/high‑happiness groups and high‑work/moderately‑high‑happiness groups, and then examined how these clusters differ in average values and regional composition. 

- **Methods:** Data cleaning and merging in Python, exploratory visualizations, correlation analysis, and K-Means clustering to identify work–happiness profiles.

## Results

- **Summary:** Results show that work hours and national happiness are related but not in a simple one‑line way. Overall, countries with higher annual working hours per worker tend to report lower happiness scores, consistent with prior evidence that long working time can reduce life satisfaction on average. However, when I clustered countries using K‑Means on work hours and happiness, I found four distinct profiles: a low‑work, high‑happiness group; a high‑work, moderate‑happiness group; a moderate‑work, low‑happiness group; and a very high‑work, low‑happiness group. A key insight observed the highest happiness in low‑work countries but also a sizable group of high‑work countries that remain relatively happy. Region counts within clusters suggest that these patterns differ across parts of the world (for example, very high‑work, low‑happiness entries are concentrated in Europe and the Americas, while high‑work, moderately high‑happiness entries are more common in Africa and Asia), reinforcing the idea that economic, social, and cultural context moderates how work intensity translates into well‑being.

# How to Run

- This section describes how to reproduce the data fetching, preprocessing, and analysis for the project. You do not need any API keys for these steps; all data sources are public and the REST Countries API is open and keyless.

## Directory structure

```text
src/API_call.py          # Fetches country metadata from REST Countries API and saves CSV
src/setup_data.py        # Loads raw data, merges datasets, saves merged CSV
src/analysis.py          # EDA, clustering, and simple models
data/                  # Local data files (not committed; see .gitignore)
src/tests.py               # Simple script/tests to run API call and inspect data
```

## Setup

Create and activate a virtual environment (optional but recommended), then install dependencies:

```bash
pip install -r requirements.txt
```
## Tests

```bash
python -m src.tests.py
```

Within tests.py functions will be called to do the following

## Fetch API data

Fetch country metadata via REST Countries API and save it as `data/country_metadata.csv`,
Function within:

```bash
python -m src.API_Call.py
```

## Build merged dataset

Make sure the following files are present in `data/` (not tracked by git):

- `annual-working-hours-per-worker.csv` (from Our World in Data)
- `whr_figure2_1.csv` (from World Happiness Report)
- `country_metadata.csv` (generated by API_call.py)

Within tests, run functions from:

```bash
python -m src.setup_data.py
```

This creates `data/merged_work_happiness_countries.csv`.

## Run analysis

To generate EDA and clustering plots. run functions basic_eda() and clustering_and_regression() from:

```bash
python -m src.analysis.py
```

This will:
- Load the merged dataset,
- Produce scatter plots and summary statistics,
- Run K-Means clustering on work_hours and happiness_score,
- Print cluster summaries to the console.

This will call the API for REST Countries url: https://restcountries.com/v3.1/all?fields=name,cca3,region,subregion,population 
and save `data/country_metadata.csv` locally.

# Work–Leisure Balance and Happiness (DSCI 510 Final Project)

This project explores how the balance between work time and leisure time at the country level relates to happiness scores.

## Setup

```bash
pip install -r requirements.txt
```

## Fetch API data

```bash
python -c "from API_call import get_country_metadata; get_country_metadata()"
```

This will call the API for REST Countries url: https://restcountries.com/v3.1/all?fields=name,cca3,region,subregion,population 
and save `data/country_metadata.csv` locally.

## Tests

```bash
python tests.py
```

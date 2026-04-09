# Work–Leisure Balance and Happiness (DSCI 510 Final Project)

This project explores how the balance between work time and leisure time at the country level relates to happiness scores.

## Setup

```bash
pip install -r requirements.txt
```

## Fetch API data

```bash
python -c "from src.data_collection import fetch_country_metadata; fetch_country_metadata()"
```

This will call the REST Countries API and save `data/country_metadata.csv` locally.

## Tests

```bash
python tests.py
```

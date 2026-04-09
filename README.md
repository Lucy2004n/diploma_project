# Diploma Project

Minimal Python project for **market demand analysis** and **automated ad script generation**.

## Project structure

- `main.py` — Reads CSV, calculates scores, finds top trend, prints ad script.
- `market_data.csv` — Example beauty niche market data.
- `requirements.txt` — Dependency list (none required).
- `README.md` — Project documentation.

## CSV format

The CSV file must contain these columns:

- `keyword`
- `search_volume`
- `engagement`
- `sentiment`

## Run

```bash
python main.py
```

## What the program does

1. Reads rows from `market_data.csv`
2. Calculates a score for each row using a simple weighted formula:
   - `score = 0.5 * search_volume + 0.3 * engagement + 0.2 * sentiment`
3. Finds the top trend (highest score)
4. Prints a simple 4-scene advertising script based on that trend

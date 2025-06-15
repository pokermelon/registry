# PokerMelon Registry

This repository stores structured data for poker tournaments, along with YAML schemas used to validate that data. The goal is to maintain a consistent registry of festivals, venues and tournament series in a machine‑readable format.

## Repository layout

```txt
registry/
├── data/       # Data files
│   ├── festivals/
│   ├── series/
│   └── venues/
├── schema/     # Yamale schemas describing the data
├── main.py     # Simple script to validate sample data
└── pyproject.toml
```

### Data directories

- **data/festivals** – Festival schedules including events and structures
- **data/series** – Information about tournament series (name, official URL, etc.)
- **data/venues** – Details about venues such as address and location coordinates

### Schemas

The `schema/` directory defines Yamale schemas for each type of data. These schemas are used to validate the YAML files in `data/`.

## Validating the data

Install the dependency (`yamale`) using `uv` and run the validation script:

```bash
uv sync
uv run main.py
```

The script will load the example data files and ensure they conform to the schemas. Any validation error will result in an exception being raised.

## Python version

The project targets Python 3.13 or newer as specified in `pyproject.toml`.

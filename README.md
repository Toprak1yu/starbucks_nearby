# ☕ Find Starbucks

A simple web app that finds the 5 nearest Starbucks locations based on your current location.

## What it does

- Automatically detects your location using your IP address
- Shows the closest Starbucks stores on an interactive map
- Displays store information in a table with distances

## Technologies

- Python
- Streamlit (for the web interface)
- Folium (for maps)
- Pandas (for data handling)

## How to run

1. Clone this repo:
```bash
git clone https://github.com/yourusername/find_starbucks.git
cd find_starbucks
```

2. Install dependencies:
```bash
pip install streamlit folium streamlit-folium pandas requests
```

3. Run the app:
```bash
streamlit run find_starbucks/__init__.py
```

## How it works

1. Gets your location using `ipinfo.io` API
2. Downloads Starbucks location data from GitHub
3. Calculates distances and finds the 5 closest ones
4. Shows everything on a map with markers

## Files

- `functions.py` - Contains the main functions for location detection and data processing
- `__init__.py` - The Streamlit web app

## Data Source

Starbucks data comes from: https://github.com/mmcloughlin/starbucks

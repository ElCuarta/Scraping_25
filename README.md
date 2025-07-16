# Scraping_25

This repository contains a simple script to fetch recent Google News results for the term **"Gabriel Boric"**.

## Usage

Install the required dependencies:

```bash
pip install requests beautifulsoup4
```

Run the scraper specifying how many past days you want to search (default: 1 day):

```bash
python scrape_gabriel_boric.py --days 3
```

The script prints the news titles and links found on Google News.

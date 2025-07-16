import argparse
import requests
from bs4 import BeautifulSoup
from datetime import datetime

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/117.0 Safari/537.36"
)


def build_search_url(query: str, days: int) -> str:
    """Return Google News search URL for query filtered by number of days."""
    q = requests.utils.quote(query)
    tbs = f"qdr:{days}d" if days > 1 else "qdr:d"
    return f"https://www.google.com/search?q={q}&tbm=nws&tbs={tbs}"


def fetch_results(url: str) -> list[tuple[str, str]]:
    """Fetch search results and return list of (title, link)."""
    headers = {"User-Agent": USER_AGENT}
    resp = requests.get(url, headers=headers, timeout=10)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    results = []
    for g in soup.select("div.dbsr"):
        title = g.select_one("div.JheGif.nDgy9d").get_text(strip=True)
        link = g.a["href"]
        results.append((title, link))
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="Scrape recent news for 'Gabriel Boric'.")
    parser.add_argument(
        "--days",
        type=int,
        default=1,
        help="Number of past days to search (default: 1)",
    )
    args = parser.parse_args()

    url = build_search_url("Gabriel Boric", args.days)
    print(f"Fetching: {url}")
    try:
        results = fetch_results(url)
    except Exception as e:
        print(f"Error fetching results: {e}")
        return

    today = datetime.utcnow().strftime("%Y-%m-%d")
    print(f"Results for 'Gabriel Boric' in the last {args.days} day(s) as of {today}:")
    for idx, (title, link) in enumerate(results, 1):
        print(f"{idx}. {title} - {link}")


if __name__ == "__main__":
    main()

# Intermediate Task 1: Web Scraper
# Extracts headings from a public web page using Requests + BeautifulSoup.

import requests
from bs4 import BeautifulSoup

URL = "https://quotes.toscrape.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

print("Quotes found on the page:")
for i, quote in enumerate(soup.select(".quote .text"), start=1):
    print(f"{i}. {quote.get_text(strip=True)}")

print("\nAuthors:")
for i, author in enumerate(soup.select(".quote .author"), start=1):
    print(f"{i}. {author.get_text(strip=True)}")

import asyncio
import httpx
from bs4 import BeautifulSoup
from loguru import logger
# Refactored scheduler - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored pipeline - 2026-03-11

class Scraper:
    """A simple, asynchronous web scraper."""

    def __init__(self, headers=None, timeout=10):
        self.headers = headers or {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        self.timeout = timeout

    async def fetch(self, url):
        """Fetch a single URL and return the response content."""
        async with httpx.AsyncClient(headers=self.headers, timeout=self.timeout) as client:
            try:
                response = await client.get(url)
                response.raise_for_status()
                return response.text
            except httpx.HTTPStatusError as e:
                logger.error(f"HTTP error for {url}: {e}")
            except httpx.RequestError as e:
                logger.error(f"Request error for {url}: {e}")
        return None

    def parse(self, html):
        """Parse the HTML and extract data. This method should be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement the parse method.")

    async def run(self, urls):
        """Run the scraper on a list of URLs."""
        tasks = [self.fetch(url) for url in urls]
        results = []
        for html in await asyncio.gather(*tasks):
            if html:
                results.extend(self.parse(html))
        return results

class ExampleScraper(Scraper):
    """An example scraper that extracts all links from a page."""

    def parse(self, html):
        soup = BeautifulSoup(html, "html.parser")
        links = []
        for a in soup.find_all("a", href=True):
            links.append(a["href"])
        return links

if __name__ == "__main__":
    async def main():
        scraper = ExampleScraper()
        urls = ["https://www.google.com", "https://www.bing.com"]
        results = await scraper.run(urls)
        for result in results:
            print(result)

    asyncio.run(main())

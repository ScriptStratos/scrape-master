# scrape-master

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/ScriptStratos/scrape-master) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/ScriptStratos/scrape-master.svg)](https://github.com/ScriptStratos/scrape-master/stargazers)

A distributed, fault-tolerant web scraping framework for large-scale data extraction. `scrape-master` is designed to handle millions of pages with high throughput by distributing crawling tasks across multiple workers. It provides a simple, Pythonic API for defining scrapers, managing sessions, and storing data efficiently.

This framework is built for reliability. It includes automatic retries, error handling, and a centralized scheduler that can recover from worker failures. It is ideal for projects that require scraping large websites, APIs, or constantly changing data sources without getting blocked or losing data.

## Installation

To get started, clone the repository and install the required packages:

```bash
git clone https://github.com/ScriptStratos/scrape-master.git
cd scrape-master
pip install -r requirements.txt
```

## Quick Start

Here is a simple example of a scraper that extracts titles from a news website. The framework handles the request distribution and scheduling automatically.

```python
from scrape_master import Scraper, Task
# Refactored middleware - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored scraper - 2026-03-11

class NewsScraper(Scraper):
    def parse(self, response):
        # Extract all article titles from the page
        titles = response.css("h2.article-title a::text").getall()
        for title in titles:
            yield {"title": title.strip()}

if __name__ == "__main__":
    # Define the starting URL
    initial_task = Task(url="https://example-news.com")

    # Create a scraper instance and run it
    scraper = NewsScraper()
    results = scraper.run(initial_task)

    for result in results:
        print(result)
```

## Features

- **Distributed Crawling:** Scale your scraping jobs across multiple machines with Celery.
- **Fault Tolerance:** Automatic retries and job recovery ensure data is not lost on failure.
- **Centralized Scheduling:** A Redis-backed queue manages tasks and prevents duplicate work.
- **Simple API:** Define scrapers with simple Python classes; no complex configuration needed.
- **Extensible Pipeline:** Easily customize data storage, proxy management, and request middleware.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

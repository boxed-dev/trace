# Trace

High-performance async web scraper with parallel processing.

## Features

- **Asynchronous Architecture:** Built on `asyncio` for high concurrency
- **Hybrid Scraping:** Intelligently switches between `httpx` for fast static content and `Playwright` for JavaScript-rendered pages
- **Multiple Modes:** Supports single page scraping, recursive crawling, sitemap parsing, and URL lists
- **Robust:** Built-in rate limiting, retries, and anti-bot detection bypass
- **Content Processing:** Automatic HTML cleaning, content deduplication, and PDF extraction support
- **Type Safe:** Full type annotations with `py.typed` marker

## Requirements

- Python 3.11 or higher

## Installation

```bash
pip install trace-scraper
```

Or install from source:

```bash
pip install .
```

Install Playwright browsers:

```bash
playwright install
```

## CLI Usage

```bash
# Scrape a single page
trace https://example.com --mode single

# Recursively crawl a website
trace https://docs.example.com --mode recursive --max-pages 100

# Parse a sitemap
trace https://example.com/sitemap.xml --mode sitemap

# Save output to JSON
trace https://example.com --output results.json
```

### Options

| Option | Short | Default | Description |
| :--- | :--- | :--- | :--- |
| `--mode` | `-m` | `single` | Scraping mode: `single`, `recursive`, `sitemap` |
| `--output` | `-o` | - | Output JSON file path |
| `--concurrency` | `-c` | `10` | Maximum concurrent pages |
| `--timeout` | `-t` | `30.0` | Page timeout in seconds |
| `--retries` | `-r` | `3` | Maximum retries per page |
| `--delay` | `-d` | `0.1` | Delay between requests in seconds |
| `--max-pages` | - | - | Maximum number of pages to scrape |
| `--scroll` | - | - | Enable page scrolling for dynamic content |
| `--browser` | - | - | Use browser for all pages |
| `--headed` | - | - | Run browser in visible mode |
| `--verbose` | `-v` | - | Enable verbose logging |

## Library Usage

### Single Page

```python
import asyncio
from trace_scraper import WebScraper, ScrapeMode

async def main():
    async with WebScraper() as scraper:
        async for doc in scraper.scrape("https://example.com", mode=ScrapeMode.SINGLE):
            print(f"Title: {doc.semantic_identifier}")
            print(f"Content: {doc.sections[0].text[:100]}...")

if __name__ == "__main__":
    asyncio.run(main())
```

### Custom Configuration

```python
from trace_scraper import WebScraper, ScraperConfig

config = ScraperConfig(
    max_concurrent_pages=20,
    page_timeout=15.0,
    extract_pdfs=True,
    scroll_pages=True,
    headless=True
)

async with WebScraper(config) as scraper:
    async for doc in scraper.scrape("https://example.com", mode=ScrapeMode.RECURSIVE):
        print(doc.semantic_identifier)
```

### Configuration Options

| Option | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `max_concurrent_pages` | `int` | `10` | Maximum pages to scrape in parallel |
| `max_concurrent_browsers` | `int` | `3` | Maximum browser contexts |
| `page_timeout` | `float` | `30.0` | Page load timeout in seconds |
| `request_timeout` | `float` | `10.0` | HTTP request timeout in seconds |
| `max_retries` | `int` | `3` | Retry attempts for failed requests |
| `delay_between_requests` | `float` | `0.1` | Rate limiting delay in seconds |
| `scroll_pages` | `bool` | `False` | Scroll to trigger lazy-loading |
| `extract_pdfs` | `bool` | `True` | Extract text from PDF files |
| `deduplicate_content` | `bool` | `True` | Skip duplicate content |
| `use_browser_for_all` | `bool` | `False` | Use Playwright for all pages |

## Development

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run linter
ruff check .

# Run type checker
mypy trace_scraper
```

## License

MIT

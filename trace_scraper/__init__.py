"""
Trace: High-performance async web scraper.
"""

from .models import Document, ScrapedPage, TextSection
from .scraper import ScrapeMode, ScraperConfig, WebScraper

__version__ = "1.0.0"
__all__ = [
    "WebScraper",
    "ScraperConfig",
    "ScrapeMode",
    "Document",
    "TextSection",
    "ScrapedPage",
]

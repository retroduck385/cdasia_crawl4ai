import asyncio
import os
import json
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, LLMConfig, JsonCssExtractionStrategy
from crawl4ai.extraction_strategy import JsonXPathExtractionStrategy
from dotenv import load_dotenv

load_dotenv()
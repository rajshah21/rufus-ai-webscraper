import os
from .scrape import scrape_nested_text, split_dom_content
from .parse import parse_with_ollama
from dotenv import load_dotenv

class RufusClient:
    def __init__(self):
        pass

    def scrape(self, url: str, prompt: str, scraper_key:str):
        """
        Scrapes and parses a webpage with nested links till max_depth=1.

        :param url: The URL of the webpage to scrape.
        :param prompt: The prompt describing the content to extract.
        :param scraper_key: Scraper Key for remote web-scraping instance. 
        :return: Extracted and parsed text content with Llama LLM.
        """
        # Step 1: Scrape the webpage
        print(f"Scraping URL: {url}")
        scraped_text = scrape_nested_text(url, scraper_key=scraper_key, max_depth=1)

        if not scraped_text:
            raise ValueError(f"No content could be scraped from {url}.")

        # Step 2: Split content into manageable chunks
        print("Splitting scraped content into chunks...")
        dom_chunks = split_dom_content(" ".join(scraped_text))

        # Step 3: Parse content using the provided prompt
        print(f"Extracting Information from scraped content for promt: {prompt}")
        parsed_content = parse_with_ollama(dom_chunks, prompt)

        return parsed_content
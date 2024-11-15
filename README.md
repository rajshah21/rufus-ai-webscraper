# Rufus Scraper

**rufus-web-scraper** is a Python package for web scraping and content parsing. It combines the power of **Selenium**, **BeautifulSoup**, and **LangChain Ollama** to extract and process data from web pages efficiently.

---

## Features
- **Scrape Websites**: Fetch content from webpages, including nested links.
- **Clean HTML Content**: Extract meaningful text by removing scripts, styles, and unnecessary elements.
- **Parse with AI**: Use AI models like Ollama locally to parse scraped content based on custom prompts.
- **Customizable Depth**: Scrape nested links up to a specified depth. (currently max_depth=1)

---

## Installation

Install Rufus Web Scraper with pip:

```bash
pip install rufus-web-scraper
```

## Setting Up before Use

1) Selenium Crawler API key:
Create a Selenium Remote API key to crawl the website by visiting this site: https://brightdata.com/
Sign-up and create free account.
Navigate to "Proxies and Scraping"> click "Add" > Select "Scraping Browser" to generate a web-crawling API key and save it.

2) Download Llama model to run locally:
Visit https://ollama.com/download and download OLlama for your pc.
Run the downloaded setup file
Open Command Prompt or Terminal and run "ollama" command.
Download Llama3.1 model locally
```bash 
ollama pull llama3.1
```
Run the Downloaded Llama model
```bash
ollama run llama3.1
```

## Example Usage

```bash
import rufus-web-scraper
from rufus-web-scraper import RufusClient

client = RufusClient()
documents = client.scrape(url,scraper_key,prompt)
print(document)
```



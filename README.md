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

## Setting Up Before Use
### Selenium Crawler API Key
To enable the Selenium crawler, you need to create a Remote API key for crawling websites:

  1) Visit https://brightdata.com/.
  2) Sign up for a free account.
  3) Navigate to Proxies and Scraping > Click Add > Select Scraping Browser.
  4) Generate a web-crawling API key and save the Selenium API.
  5) Pass the API key directly in the ".scrape" function.

### Download the Llama Model Locally
To use the Llama model for parsing:

  1) Visit https://ollama.com/download.
  2) Download the Ollama setup for your platform and install it.
  3) Open Command Prompt (Windows) or Terminal (Mac/Linux).
  4) Run the following command to ensure Ollama is installed:
  ```bash
  ollama
  ```
  5) Download the Llama3.1 model locally:
  ```bash
  ollama pull llama3.1
  ```

## Example Usage

```bash
import rufus-web-scraper
from rufus-web-scraper import RufusClient

client = RufusClient()
documents = client.scrape(url,scraper_key,prompt)
print(document)
```



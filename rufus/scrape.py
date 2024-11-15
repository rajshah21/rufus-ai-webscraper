from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from urllib.parse import urljoin
import os
import time

load_dotenv
# Configuration
NAVIGATION_LIMIT = 10
BASE_DELAY = 50  # Base delay in seconds between navigations

def scrape_text_content(driver, url):
    """
    Scrapes and extracts text content from a given URL.
    
    :param driver: WebDriver instance.
    :param url: URL to scrape.
    :return: Text content of the URL.
    """
    try:
        print(f"Navigating to {url}")
        driver.get(url)
        time.sleep(BASE_DELAY)
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, "html.parser")

        # Remove scripts and styles
        for script_or_style in soup(["script", "style"]):
            script_or_style.extract()

        # Extract text and clean up
        text = soup.get_text(separator="\n")
        cleaned_text = "\n".join(
            line.strip() for line in text.splitlines() if line.strip()
        )
        return cleaned_text
    except Exception as e:
        print(f"Failed to scrape text content from {url}: {e}")
        return None

def scrape_nested_text(base_url, scraper_key, max_depth=1):
    """
    Scrapes the base URL and its nested links up to the specified depth for text content.
    
    :param base_url: URL of the website to start scraping.
    :param sbr_connection: Chromium remote connection instance.
    :param max_depth: Maximum depth of nested links to scrape.
    :return: Dictionary with URLs as keys and their text content as values.
    """
    print("Connecting to scraping browser...")
    options = ChromeOptions()
    sbr_connection = ChromiumRemoteConnection(scraper_key, "goog", "chrome")
    scraped_text = {}
    visited_links = set()
    to_visit = [(base_url, 0)]  # Stack of URLs to visit with their depth level
    navigation_count = 1
    driver = None
    
    try:
        
        while to_visit:
            print("Creating new Driver.")
            driver = Remote(sbr_connection, options=options)
            
            current_url, depth = to_visit.pop(0)
            if current_url in visited_links or depth > max_depth:
                continue
            
            text_content = scrape_text_content(driver, current_url)
            if text_content:
                scraped_text[current_url] = text_content
                visited_links.add(current_url)
                navigation_count += 1
                
                # Only look for links if we haven't reached the maximum depth
                if depth < max_depth:
                    soup = BeautifulSoup(driver.page_source, "html.parser")
                    links = soup.find_all("a", href=True)
                    
                    for link in links[:5]:
                        link_url = urljoin(current_url, link["href"])
                        if link_url not in visited_links:
                            to_visit.append((link_url, depth + 1))
            else:
                print(f"Skipping {current_url} due to failed text extraction.")
            driver.quit()
            time.sleep(50)
    except Exception as e:
        print(e)

    return scraped_text.values()


def split_dom_content(dom_content, max_length=6000):
    return [
        list(dom_content)[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]


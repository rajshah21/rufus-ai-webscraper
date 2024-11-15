import unittest
from rufus.client import RufusClient
from dotenv import load_dotenv
import os


load_dotenv()

class TestRufusClient(unittest.TestCase):
    def test_scrape(self):
        # Mocking URL and prompt
        url = "https://hashedin.com/"
        prompt = "Extract all headings."
        key = os.getenv("SBR_WEBDRIVER")

        client = RufusClient()

        # Test scrape functionality
        try:
            result = client.scrape(url, prompt=prompt, scraper_key=key)
            self.assertIsInstance(result, str)
            print(result)
        except Exception as e:
            self.fail(f"RufusClient.scrape raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()
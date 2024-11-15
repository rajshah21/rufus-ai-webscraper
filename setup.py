from setuptools import setup, find_packages

setup(
    name="rufus-web-scraper",
    version="1.0.3",
    description="A Python package for web scraping and parsing using Selenium, BeautifulSoup, and Llama LLM.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Raj Shah",
    author_email="shahraj2100@gmail.com",
    url="https://github.com/rajshah21/rufus-ai-webscraper",  # Update with your repository URL
    packages=find_packages(),
    install_requires=[
        "selenium>=4.0.0",            # For web automation
        "beautifulsoup4>=4.10.0",     # For HTML parsing
        "python-dotenv>=1.0.0",       # For environment variable management
        "langchain-ollama>=0.1.0",    # For parsing with AI model
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",          # Ensures compatibility with Python 3.7 and later
    entry_points={
        "console_scripts": [
            "rufus=rufus.client:RufusClient",  # Optional CLI entry point
        ],
    },
)

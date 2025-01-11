import requests
from bs4 import BeautifulSoup

def scrape_titles_and_prices(url):
    # Fetch the website's content
    response = requests.get(url)
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all products on the page
    products = soup.find_all('article', class_='product_pod')
    scraped_data = []

    for product in products:
        # Extract the title and price
        title = product.h3.a['title']
        price = product.find('p', class_='price_color').text
        scraped_data.append((title, price))

    return scraped_data

def print_scraped_data(scraped_data):
    print("Scraped Products:")
    print("-----------------")
    for title, price in scraped_data:
        print(f"Title: {title}\nPrice: {price}\n")

if __name__ == "__main__":
    # URL of the website to scrape
    url = "http://books.toscrape.com"
    scraped_data = scrape_titles_and_prices(url)
    print_scraped_data(scraped_data)

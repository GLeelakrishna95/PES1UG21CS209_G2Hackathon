import requests
from bs4 import BeautifulSoup

def scrape_product_data(urls):
    product_data = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract product name
            product_name_element = soup.find('h1')
            if product_name_element:
                product_name = product_name_element.text.strip()
            else:
                product_name = None

            # Extract product description
            product_description_element = soup.find('div', {'class': 'product-description'})
            if product_description_element:
                product_description = product_description_element.text.strip()
            else:
                product_description = None

            # Add product data to the list
            product_data.append({
                'name': product_name,
                'description': product_description
            })
        except Exception as e:
            # Log the error and continue with the next URL
            print(f"Error scraping data from URL: {url}")
            print("Error:", e)
            continue

    return product_data
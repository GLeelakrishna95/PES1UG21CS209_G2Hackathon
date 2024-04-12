import web_scraper
import nlp_processor
import database_integrator

def main():
    # URLs to scrape
    urls = [
        'https://www.telesign.com/products/trust-engine',
        'https://www.litzia.com/professional-it-services/',
        'https://www.chattechnologies.com/',
        'https://inita.com/',
        'https://aim-agency.com/'
    ]

    # Step 1: Scrape product data
    product_data = []
    for url in urls:
        try:
            scraped_data = web_scraper.scrape_product_data([url])
            product_data.extend(scraped_data)
        except Exception as e:
            print(f"Failed to retrieve URL: {url}")
            print("Error:", e)

    # Step 2: Process product descriptions
    processed_data = nlp_processor.generate_description(product_data)

    # Step 3: Update the database with processed data
    database_integrator.update_product_descriptions(processed_data)

if __name__ == "__main__":
    main()
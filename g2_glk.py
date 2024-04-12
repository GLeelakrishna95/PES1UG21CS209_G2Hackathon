import os
import spacy
import requests
import urllib3
from bs4 import BeautifulSoup
import mysql.connector

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Define a list of URLs to fetch descriptions from
urls = [
    
    "https://www.litzia.com/professional-it-services/",
    "https://www.chattechnologies.com/",
    "https://inita.com/",
    "https://aim-agency.com/"
]

def fetch_webpage_content(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://www.google.com/'  # Add a referer to mimic a browser request
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.content.decode('utf-8')
    except (requests.exceptions.RequestException, urllib3.exceptions.HTTPError, urllib3.exceptions.LocationParseError) as e:
        print(f"Error fetching webpage content for {url}: {e}")
        return None


# Rest of the code remains the same

def extract_meaningful_text(html_content):
    try:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Extract relevant text (e.g., paragraphs) from the HTML content
        text = " ".join([p.get_text() for p in soup.find_all('p')])
        return text
    except Exception as e:
        print(f"Error extracting meaningful text: {e}")
        return None

def generate_product_description(url):
    try:
        # Fetch webpage content
        html_content = fetch_webpage_content(url)
        if html_content:
            # Extract meaningful text from the webpage
            meaningful_text = extract_meaningful_text(html_content)
            if meaningful_text:
                # Process the text using spaCy
                doc = nlp(meaningful_text)
                
                # Extract relevant sentences or phrases for the description
                description = " ".join(sent.text for sent in doc.sents)
                return description
    except Exception as e:
        print(f"Error generating description for {url}: {e}")
        return None
    
def update_database():
    try:
        # Connect to MySQL database
        conn = mysql.connector.connect(
            host='localhost',
            user='LEEELAKRISHNA86',
            password='Leeela@55',
            database='g2_lk'
        )
        cursor = conn.cursor()

        # Create table if not exists
        cursor.execute('''CREATE TABLE IF NOT EXISTS products
                          (url VARCHAR(255) PRIMARY KEY, description TEXT)''')

        # Iterate over URLs and fetch/update descriptions in database
        for url in urls:
            description = generate_product_description(url)
            if description:
                # Insert or update description in the database
                cursor.execute('''INSERT INTO products (url, description) VALUES (%s, %s)
                                  ON DUPLICATE KEY UPDATE description=%s''', (url, description, description))

        # Commit changes and close connection
        conn.commit()
        print("Product descriptions updated successfully!")
    except Exception as e:
        print(f"Error updating database: {e}")
    finally:
        # Close database connection
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    update_database()

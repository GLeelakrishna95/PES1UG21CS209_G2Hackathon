import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download NLTK data if needed
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    """
    Tokenizes the text, removes stopwords, and performs other preprocessing.
    """
    if text:
        tokens = word_tokenize(text.lower())  # Tokenize text
        filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]  # Remove stopwords
        # Join tokens to form processed text
        processed_text = ' '.join(filtered_tokens)
        return processed_text
    else:
        return ''

def generate_description(product_data):
    """
    Generates concise descriptions for product data.
    """
    descriptions = []
    for product in product_data:
        preprocessed_text = preprocess_text(product['description'])
        # Generate a concise description using NLTK's sentence tokenization
        sentences = sent_tokenize(preprocessed_text)
        concise_description = ' '.join(sentences[:2])  # Take the first two sentences as a concise description
        descriptions.append({
            'name': product['name'],
            'description': concise_description
        })
    return descriptions

if __name__ == "__main__":
    # Sample product data (from web scraping or any source)
    sample_product_data = [
        {
            'name': 'Telesign Trust Engine',
            'description': 'Telesign\'s Trust Engine provides reliable, real-time fraud prevention and account security solutions for businesses, ensuring safe online interactions.'
        },
        {
            'name': 'Litzia Professional IT Services',
            'description': 'Litzia offers comprehensive and tailored IT services to businesses, helping them streamline operations and enhance efficiency.'
        },
        {
            'name': 'Chat Technologies',
            'description': 'Chat Technologies provides cutting-edge communication solutions, enabling seamless and efficient interactions across platforms.'
        },
        {
            'name': 'Inita',
            'description': 'Inita offers innovative digital solutions to businesses, empowering them to succeed in the digital landscape with customized strategies.'
        },
        {
            'name': 'AIM Agency',
            'description': 'AIM Agency specializes in digital marketing solutions, helping businesses reach their target audience and achieve marketing goals.'
        }
    ]

    processed_descriptions = generate_description(sample_product_data)
    for product in processed_descriptions:
        print("Product Name:", product['name'])
        print("Generated Description:", product['description'])
        print("=" * 50)

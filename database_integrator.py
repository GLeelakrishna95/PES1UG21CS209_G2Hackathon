import mysql.connector

def connect_to_database():
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="LEEELAKRISHNA86",
        password="Leeela@55",
        database="lk"
    )
    return conn

def update_product_descriptions(product_descriptions):
    conn = connect_to_database()
    cursor = conn.cursor()

    for product in product_descriptions:
        try:
            # Check if the product already exists in the database
            cursor.execute("SELECT * FROM products WHERE name = %s", (product['name'],))
            existing_product = cursor.fetchone()

            if existing_product:
                # Update the existing product description
                cursor.execute("UPDATE products SET description = %s WHERE name = %s", (product['description'], product['name']))
            else:
                # Insert the new product
                cursor.execute("INSERT INTO products (name, description) VALUES (%s, %s)", (product['name'], product['description']))

        except mysql.connector.Error as err:
            print("Error updating product:", err)
            conn.rollback()  # Rollback changes in case of error

    conn.commit()
    conn.close()

def main():
    # Sample product descriptions from nlp_processor.py
    product_descriptions = [
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

    update_product_descriptions(product_descriptions)
    print("Product descriptions updated in the database.")

if __name__ == "__main__":
    main()

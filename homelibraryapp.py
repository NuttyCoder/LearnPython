import isbnlib

def fetch_book_details(isbn):
    try:
        book = isbnlib.meta(isbn)
        if book:
            return {
                'Title': book['Title'],
                'Authors': book['Authors'],
                'Publisher': book['Publisher'],
                'Year': book['Year']
            }
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

isbn = "9780134190440"  # Sample ISBN
details = fetch_book_details(isbn)

if details:
    for key, value in details.items():
        print(f"{key}: {value}")
else:
    print("No details found for this ISBN.")

import requests  # To handle HTTP requests
from bs4 import BeautifulSoup  # For parsing HTML content

def fetch_article_content(url):
    """
    Fetches the article content from a given URL.

    Parameters:
    url (str): The URL of the article to fetch.

    Returns:
    str: The extracted article content, or None if an error occurs.
    """
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        
        # Parse the response HTML with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Try to find the content using different class names
        content_classes = [
            'entry-content',  # Common class name for article content
            'article-hero',   # Another possible class name
            'wp-block-post-content'  # Yet another possible class name
        ]
        
        # Loop through each class name to find the article content
        for class_name in content_classes:
            content = soup.find('div', class_=class_name)
            if content:
                return content.get_text(strip=True)  # Return the text content without extra whitespace
        
        # If no content found, print the full HTML for inspection
        print("Could not find the article content. Here's the full HTML:")
        print(soup.prettify())  # Pretty print the HTML for easier reading
        return None

    except requests.RequestException as e:
        # Handle any errors that occur during the request
        print(f"An error occurred: {e}")
        return None

# URL of the TechCrunch article
url = "https://techcrunch.com/2024/04/30/sams-clubs-ai-powered-exit-tech-reaches-20-of-stores/"

# Fetch and print the article content
article_content = fetch_article_content(url)

if article_content:
    print("Article content:")
    print(article_content)  # Print the extracted article content
else:
    print("Failed to retrieve the article content.")

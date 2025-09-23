import requests
import os
from urllib.parse import urlparse
import hashlib

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Ask user for one or multiple URLs (comma separated)
    urls = input("Please enter the image URL(s) (separate multiple with commas): ")
    urls = [u.strip() for u in urls.split(",") if u.strip()]

    # Create directory if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)

    for url in urls:
        try:
            # Fetch the image
            response = requests.get(url, timeout=10, headers={"User-Agent": "UbuntuFetcher/1.0"})
            response.raise_for_status()  # Raise exception for bad status codes

            # Extract filename from URL
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)

            # If no filename in URL, generate one using hash
            if not filename:
                filename = f"image_{hashlib.md5(url.encode()).hexdigest()[:8]}.jpg"

            filepath = os.path.join("Fetched_Images", filename)

            # Prevent duplicates
            if os.path.exists(filepath):
                print(f"⚠ Skipping duplicate: {filename}")
                continue

            # Check Content-Type header
            content_type = response.headers.get("Content-Type", "")
            if not content_type.startswith("image/"):
                print(f"✗ Skipping {url} - not an image (Content-Type: {content_type})")
                continue

            # Save the image
            with open(filepath, 'wb') as f:
                f.write(response.content)

            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}\n")

        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error with {url}: {e}")
        except Exception as e:
            print(f"✗ An error occurred with {url}: {e}")

    print("Connection strengthened. Community enriched.")

if __name__ == "__main__":
    main()

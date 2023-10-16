import requests
import os

def download_image(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)

def synchronous_download():
    urls = [
        'https://example.com/image1.jpg',
        'https://example.com/image2.jpg',
        # ... (добавьте еще 8 URL-адресов)
    ]

    for i, url in enumerate(urls):
        download_image(url, f'image_{i+1}.jpg')

if __name__ == "__main__":
    synchronous_download()

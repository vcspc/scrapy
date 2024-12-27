import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def scrape_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança uma exceção para erros HTTP
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join([p.get_text() for p in paragraphs])
        return text
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")
        return ""

def find_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        links = []
        for a in soup.find_all('a', href=True):
            link = urljoin(url, a['href'])
            if urlparse(link).netloc == urlparse(url).netloc:
                links.append(link)
        return links
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")
        return []

def main():
    start_url = "https://www.example.com"  # Substitua pela URL do site que você quer raspar
    visited_urls = set()
    urls_to_visit = [start_url]

    with open("output.txt", "w", encoding="utf-8") as f:
        while urls_to_visit:
            url = urls_to_visit.pop(0)
            if url in visited_urls:
                continue
            visited_urls.add(url)
            text = scrape_page(url)
            f.write(f"URL: {url}\n")
            f.write(text + "\n\n")
            links = find_links(url)
            urls_to_visit.extend(links)
    print("Web scraping concluído. Os dados foram salvos em output.txt")

if __name__ == "__main__":
    main()

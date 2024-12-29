import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def scrape_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extrai texto de parágrafos
        paragraphs = soup.find_all('p')
        text = '\n\n'.join([p.get_text() for p in paragraphs])
        
        # Extrai blocos de código com tags
        code_blocks = soup.find_all(['code', 'pre'])
        code_text = '\n\n'.join([f'```\n{code.get_text()}\n```' for code in code_blocks])
        
        # Extrai o título da página
        title = soup.title.text if soup.title else ""
        
        # Extrai elementos de destaque com tags
        highlight_blocks = soup.find_all(['strong', 'em'])
        highlight_text = ' '.join([f'**{highlight.get_text()}**' if highlight.name == 'strong' else f'*{highlight.get_text()}*' for highlight in highlight_blocks])
        
        return f"# {title}\n\n" + text + "\n\n" + code_text + "\n\n" + highlight_text
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
    start_url = input("Insira a URL do site para raspar: ")
    visited_urls = set()
    urls_to_visit = [start_url]
    file_count = 1
    link_count = 0

    while urls_to_visit:
        url = urls_to_visit.pop(0)
        if url in visited_urls:
            continue
        visited_urls.add(url)
        text = scrape_page(url)
        
        with open(f"output_{file_count}.txt", "a", encoding="utf-8") as f:
            f.write(f"URL: {url}\n")
            f.write(text + "\n\n")
        
        link_count += 1
        if link_count % 50 == 0:
            file_count += 1
        
        links = find_links(url)
        urls_to_visit.extend(links)
    print("Web scraping concluído. Os dados foram salvos em arquivos output_*.txt")

if __name__ == "__main__":
    main()

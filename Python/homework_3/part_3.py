import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    """
    Получает HTML с веб-сайта и парсит его с помощью BeautifulSoup.
    :param url: str - URL веб-сайта.
    :return: None
    """
    try:
        # Получаем HTML-страницу
        response = requests.get(url)
        response.raise_for_status()  # Проверяем на успешный ответ
        
        # Парсим HTML-код
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Получаем заголовок страницы
        title = soup.title.string if soup.title else "Заголовок не найден"
        print(f"Заголовок страницы: {title}")
        
        # Пример: Получение цитат и их авторов
        print("\nЦитаты на странице:")
        quotes = soup.find_all('div', class_='quote')
        for quote in quotes:
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            print(f"\"{text}\" - {author}")
        
        # Пример: Получение всех тегов на странице
        print("\nТеги на странице:")
        tags = {tag.get_text() for tag in soup.find_all('a', class_='tag')}
        print(", ".join(tags))
    
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении данных: {e}")

# URL для парсинга
url = "https://quotes.toscrape.com"

# Выполнение функции
scrape_website(url)

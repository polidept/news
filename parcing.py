from config import NEWS_API_KEY
import requests

def get_archive_news(year, month):
    URL = f"https://api.nytimes.com/svc/archive/v1/{year}/{month}.json"
    params={'api-key': NEWS_API_KEY}

    try:
        response = requests.get(URL, params = params)
        response.raise_for_status()
        data = response.json()

        if 'response' in data and 'docs' in data['response']:
            articles = data['response']['docs']
            formatted_articles = []

            for article in articles:
                title = article['headline']['main']
                description = article['snippet']
                url = article['web_url']
                
                formatted_article = {
                    'title': title,
                    'description': description,
                    'url': url
                }
                formatted_articles.append(formatted_article)

            return formatted_articles
        else:
            return None
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def get_popular_news(period):
    URL = f"https://api.nytimes.com/svc/mostpopular/v2/viewed/{period}.json"
    params={'api-key': NEWS_API_KEY}
    
    try:
        response = requests.get(URL, params = params)
        response.raise_for_status()
        data = response.json()
        
        if 'results' in data:
            articles = data['results']
            formatted_articles = []

            for article in articles:
                title = article['title']
                description = article['abstract']
                url = article['url']

                formatted_article = {
                    'title': title,
                    'description': description,
                    'url': url 
                }
                formatted_articles.append(formatted_article)
            return formatted_articles
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def get_top_stories(section):
    URL = f"https://api.nytimes.com/svc/topstories/v2/{section}.json"
    params={'api-key': NEWS_API_KEY}

    try:
        response = requests.get(URL, params = params)
        response.raise_for_status()
        data = response.json()
        
        if 'results' in data:
            articles = data['results']
            formatted_articles = []

            for article in articles:
                title = article['title']
                description = article['abstract']
                url = article['url']

                formatted_article = {
                    'title': title,
                    'description': description,
                    'url': url 
                }
                formatted_articles.append(formatted_article)
            return formatted_articles
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def get_times_newswire(source, section):
    URL = f"https://api.nytimes.com/svc/news/v3/content/{source}/{section}.json"
    params={'api-key': NEWS_API_KEY}

    try:
        response = requests.get(URL, params = params)
        response.raise_for_status()
        data = response.json()

        if 'results' in data:
            articles = data['results']
            formatted_articles = []

            for article in articles:
                title = article['title']
                description = article['abstract']
                url = article['url']

                formatted_article = {
                    'title': title,
                    'description': description,
                    'url': url 
                }
                formatted_articles.append(formatted_article)
            return formatted_articles
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def get_search_news(topic):
    URL = f"https://api.nytimes.com/svc/search/v2/articlesearch.json?q={topic}"
    params={'api-key': NEWS_API_KEY}

    try:
        response = requests.get(URL, params = params)
        response.raise_for_status()
        data = response.json()

        if 'response' in data and 'docs' in data['response']:
            articles = data['response']['docs']
            formatted_articles = []

            for article in articles:
                title = article['headline']['main']
                description = article['snippet']
                url = article['web_url']
                
                formatted_article = {
                    'title': title,
                    'description': description,
                    'url': url
                }
                formatted_articles.append(formatted_article)

            return formatted_articles
        else:
            return None
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
           

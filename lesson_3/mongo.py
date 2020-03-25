from pymongo import MongoClient
from lesson3 import HEADERS, URL, BASE_URL, get_next_page, get_post_url, get_page, get_post_data


if __name__ == '__main__':
    client = MongoClient('mongodb://localhost:27017/')
    db = client['habr_mongo']

    data = get_page(URL)

    for soap in get_page(URL):
        posts = get_post_url(soap)
        for url in posts:
            data = get_post_data(url)

            db['posts'].insert_one(data)

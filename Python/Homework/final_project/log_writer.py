# log_writer.py
# Save search queries to MongoDB

from pymongo import MongoClient
from datetime import datetime


def connect_mongo():
    """Connect to MongoDB
    Input: None
    Output: MongoDB collection object or raises error"""
    try:
        client = MongoClient(
            "mongodb://ich_editor:verystrongpassword"
            "@mongo.itcareerhub.de/?readPreference=primary"
            "&ssl=false&authMechanism=DEFAULT&authSource=ich_edit",
            connect=True
        )
        db = client["ich_edit"]
        collection = db["final_project_210225ptm_Platonova"]
        return collection
    except Exception as e:
        raise Exception(f"Cannot connect to MongoDB: {e}")
    # В pymongo 4.x подключение к MongoDB может быть отложенным (lazy connection).
    # Это означает, что MongoClient не проверяет подключение сразу при создании объекта,
    # а делает это только при первом запросе к базе данных
    # (например, при вызове collection.insert_one в log_search).


def log_search(search_type: str, params: dict, results_count: int):
    """Save search query to MongoDB.
    Input:
        search_type (str): Type of search ('keyword' or 'genre_year')
        params (dict): Search parameters
        results_count (int): Number of results
    Output: None
    """
    try:
        collection = connect_mongo()
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "search_type": search_type,
            "params": params,
            "results_count": results_count
        }
        collection.insert_one(log_entry)
        #print("\033[93minsert log (query of searching) to MongoDB... \033[0m")
    except Exception as e:
        print(f"\033[91mError saving to MongoDB: {e}\033[0m")
    #print("\033[93mDone! \033[0m")

    # Example doc in MongoDB :
    # {
    #  "timestamp": "2025-05-01T15:34:00",
    #  "search_type": "keyword",
    #  "params": {
    #  "keyword": "matrix"
    #  },
    #  "results_count": 3
    # }
# log_stats.py
# Get popular and recent searches from MongoDB

from log_writer import connect_mongo


def get_popular_searches():
    """Get top 5 popular searches.

    Input: None
    Output: List of dicts with search_type, params, count
    """
    print("\033[93mStart printing statistic...\033[0m")
    collection = connect_mongo()
    pipeline = [
        {"$group": {
            "_id": {"search_type": "$search_type", "params": "$params"},
            "count": {"$sum": 1}
        }},
        {"$sort": {"count": -1}},
        {"$limit": 5}
    ]

    doc_results = list(collection.aggregate(pipeline)) # list of dicts
    # example doc (dict) in doc_results: {
    #    { "_id": {"search_type": "keyword", "params": {"keyword": "age"}},
    #     "count": 4
    #   }
    return [
        {
            "search_type": doc["_id"]["search_type"],
            "params": doc["_id"]["params"],
            "count": doc["count"]
        } for doc in doc_results
    ]
    #example return:
    # [ {'search_type': 'keyword', 'params': {'keyword': 'age'}, 'count': 15},
    # {'search_type':'genre_year','params':{'genre':'New','year_from':1990,'year_to': 2025}{},{}...]


def get_recent_searches():
    """Get last 5 unique searches.

    Input: None
    Output: List of dicts with search_type, params, timestamp
    """
    print("\033[93mstart printing statistic...\033[0m")
    collection = connect_mongo()
    pipeline = [
        {"$sort": {"timestamp": -1}}, # сортируем по времени (необязательно, но важно для точного $first)
        {"$group": {
            "_id": {"search_type": "$search_type", "params": "$params"},
            "timestamp": {"$first": "$timestamp"} # берем первое значение поля timestamp из каждой группы
        }},
        {"$sort": {"timestamp": -1}},
        {"$limit": 5}
    ]
    doc_results = list(collection.aggregate(pipeline))
    return [
        {
            "search_type": doc["_id"]["search_type"],
            "params": doc["_id"]["params"],
            "timestamp": doc["timestamp"]
        } for doc in doc_results
    ]
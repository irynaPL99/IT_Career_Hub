# formatter.py
# Format output as tables

from datetime import datetime

def print_films_table(films):       # films = result
    """Print movies as lines.

    Input: films (list of tuples): List of (title, release_year, genre)
    Output: None (prints lines)"""
    if not films:
        print("\033[91mNo films found!\033[90m")
        return

    print("\nSearch results (only 10 per page):")
    print(f"* title - release_year - genre")
    print(40*"-")
    for i, (title, release_year, genre) in enumerate(films, start=1):
        #print(f"{i}. {title} - {release_year} - {genre}")
        print(f"* {title} - {release_year} - {genre}")


def print_genres_with_details(genres):
    """Print genres with year range and film count.

    Input: genres (list of tuples): List of (genre, min_year, max_year, film_count)
    Output: None (prints lines)
    """
    if not genres:
        print("\033[91mNo genres found.\033[0m")
        return

    print("\nAVAILABLE GENRES:")
    print(60 * "=")
    print("Genre: \tMin - Max release year:  \tCount of films:")
    print(60 * "-")
    for row in genres:
        min_year = str(row[1]) if row[1] is not None else "N/A"
        max_year = str(row[2]) if row[2] is not None else "N/A"
        print(f"* {row[0]}:\t{min_year} - {max_year} \t\tCount of films: {row[3]}")


def print_searches_table(searches, title):
    """Print searches as lines with

    Input:
        searches (list of dicts): List with search_type, params, count/timestamp
        title (str): Title for table
    Output: None (prints lines)
    """
    if not searches:
        print("\033[93mNo searches found! Exit to statistics menu...\033[0m")
        return

    rows = []
    # searches (list of dicts): List with search_type, params(dict), count/timestamp
    # search = {"search_type": "keyword", "params": {"keyword": "age"}, "timestamp": "2025-07-25T21:34:49.147597"}
    for search in searches:
        #params = ", ".join(f"{type_s}: '{key}'" for type_s, key in search["params"].items())
        params = ", ".join(f"'{key}'" for type_s, key in search["params"].items())
        details = search.get("count", search.get("timestamp", ""))
        # пытаемся получить значение по ключу "count" из словаря search.
        # если ключ "count" отсутствует, тогда попытаться получить "timestamp".
        # Если и "timestamp" нет, тогда вернуть "" (пусто).
        rows.append([search["search_type"], params, str(details)])

    # Print title and rows
    print(f"\n{title}:")
    print(70 * "=")
    #print(f"search_type - params of searching \t-> \t(count of query's or date(time)):")
    header = "search_type: (request_count) - search_params" if "POPULAR" in title else \
        "search_type: \t\t(date_time) \t\t\t- search_params "
    print(header)
    print(70 * "-")

    for search in searches:
        search_type = search["search_type"]
        params = search["params"]
        details = search.get("count", search.get("timestamp", ""))

        if "POPULAR" not in title and details:
            try:
                dt = datetime.fromisoformat(details)
                details = dt.strftime("%Y-%m-%d %H:%M:%S.%f")[:-4]
            except ValueError:
                pass

        if search_type == "keyword":
            #params_str = f"keyword: {params.get('keyword', '')}"
            params_str = f"'{params.get('keyword', '')}'"
        elif search_type == "genre_year":
            params_str = f"'{params.get('genre', '')}', {params.get('year_from', '')}-{params.get('year_to', '')}"
        else:
            params_str = str(params)

        #print(f"{search_type} \t- {params_str} \t\t\t\t ({details})")
        print(f"{search_type}:\t\t({details}) \t- {params_str}")
    print("\033[93mDone ...Exit to statistics menu...\033[0m")



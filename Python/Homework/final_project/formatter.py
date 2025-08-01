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
    print(50 * "=")
    print(f"{'genre':<12} {'release year':<12}     {'title'}")
    print(50*"-")
    for i, (title, release_year, genre) in enumerate(films, start=1):
        print(f"* {genre:<12}   {str(release_year):<12} {title} ")


def print_genres_with_details(genres):
    """Print genres with year range and film count.

    Input: genres (list of tuples): List of (genre, min_year, max_year, film_count)
    Output: None (prints lines)
    """
    if not genres:
        print("\033[91mNo genres found.\033[0m")
        return

    print("\nAVAILABLE GENRES:")
    print(50 * "=")
    print(f"{'Genre':<16} {'Min - Max year':<16} Count of films")
    print(50 * "-")
    for row in genres:
        min_year = str(row[1]) if row[1] is not None else "N/A"
        max_year = str(row[2]) if row[2] is not None else "N/A"
        print(f"* {row[0]:<16} {min_year + ' - ' + max_year:<16}  ({row[3]})")

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

    # Print title and rows
    print(f"\n{title}:")
    print(60 * "=")
    header = f"{'search_type':<16} {'request_count':<24}  search_params" if "POPULAR" in title else \
        f"{'search_type':<16} {'date_time':<24}  search_params"

    print(header)
    print(60 * "-")

    for search in searches:
        search_type = search["search_type"]
        params = search["params"]
        details = search.get("count", search.get("timestamp", ""))
        # Переменная details содержит либо count (для популярных поисков),
        # либо timestamp (для последних поисков).
        if "POPULAR" not in title and details:
            try:
                dt = datetime.fromisoformat(details) #->dt станет объектом datetime(2025, 7, 30, 21, 16)
                details = dt.strftime("%Y-%m-%d %H:%M:%S.%f")[:-4] # обрезает последние 4 символа msec
            except ValueError:
                # pass    # Пустая инструкция, которая игнорирует ошибку и оставляет details без изменений.
                print(f"\033[93mWarning: Invalid timestamp format in details: {details}\033[0m")

        if search_type == "keyword":
            #params_str = f"keyword: {params.get('keyword', '')}"
            params_str = f"'{params.get('keyword', '')}'"
        elif search_type == "genre_year":
            params_str = f"'{params.get('genre', '')}', {params.get('year_from', '')}-{params.get('year_to', '')}"
        else:
            params_str = str(params)

        print(f"{search_type:<16} {details:<24}  {params_str}")
    print("\033[93mDone! Exit to statistics menu...\033[0m")



# main.py
# Console menu for movie search App

import mysql_connector
import formatter
import log_writer
import log_stats

def show_menu():
    """Show menu options to user.

    Input: None
    Output: None (prints menu)
    """
    print()
    print(50*"=")
    print("main menu: \t********* MOVIE SEARCH: *********")
    print(50*"=")
    print("1. Search by KEYWORD")
    print("2. Search by GENRE and YEAR")
    print("3. Show POPULAR or RECENT searches")
    print(50 * "-")
    print("0. Exit")

def show_stats_submenu():
    """Show submenu for statistics type.

    Input: None
    Output: String (user's choice: '0', '1', or '2')
    """
    print("\nChoose please STATISTICS TYPE:")
    print(50 * "=")
    print("1. Show POPULAR searches")
    print("2. Show RECENT searches")
    print(50 * "-")
    print("0. Exit to main menu")
    return input("\033[92mEnter choice (1-2) or '0' for exit to main menu: \033[0m")

def main():
    """Main function to run the app.

    Input: None
    Output: None (runs program loop)
    """
    while True:
        show_menu()
        choice = input("\033[92mEnter your choice (1-3 or '0' for exit): \033[0m")

        try:
            choice = int(choice)
            if choice == 1:
                keyword = input("\033[92mYour choice is 'Search by KEYWORD'. Enter keyword: \033[0m").strip().lower() # MySQL не чувствительный к регистру
                if not keyword:
                    print("\033[91mKeyword cannot be empty!\033[0m")
                    continue
                print("\033[93mStart searching...\033[0m")
                offset = 0  # --> for mysql_connector.search_by_keyword
                # Get total count of films for logging to MongoDB:
                total_count = mysql_connector.count_by_keyword(keyword)
                while True:
                    try:
                        results = mysql_connector.search_by_keyword(keyword, offset)
                        if not results:
                            print("\033[93mNo more results found! Exit to main menu...\033[0m")
                            break

                        # print table (title - release_year - genre):
                        formatter.print_films_table(results)

                        # Log to MogoDB only after the first query
                        if offset == 0:
                            log_writer.log_search("keyword", {"keyword": keyword}, total_count)

                        more = input("\033[92mShow next 10 results? "
                                     "('y'/'Y' - continue, another - exit to main menu...): \033[0m").lower()
                        if more.lower() != 'y':
                            print("\033[93mYour choice is 'exit to main menu'...\033[0m")
                            break
                        offset += 10
                    except Exception as e:
                        print(f"\033[91mDatabase error: {e}\033[0m")
                        break

            elif choice == 2:
                print(f"\033[92mYour choice is 'Search by GENRE and YEAR'...\033[90m")
                try:
                    # def return List of tuples (genre, min_year, max_year, film_count):
                    genres_data = mysql_connector.get_genres_with_details()
                    # expample genres_data:[('Action', 1990, 2025, 64), ('Animation', 1990, 2025, 66), ...]
                    if not genres_data:
                        print("\033[91mError: Cannot load genres!\033[0m")
                        continue

                    # print table genres with details(min_year, max_year, film_count)
                    formatter.print_genres_with_details(genres_data)

                    # input genre (insensitive - below):
                    genre = input("\033[92mEnter genre (insensitive): \033[0m").strip()
                    if not genre:
                        print("\033[91mError: Genre cannot be empty!\033[0m")
                        continue

                    # Get valid genres (insensitive) from
                    # genres_data (List of tuples (genre, min_year, max_year, film_count):
                    valid_genres = [row[0] for row in genres_data]
                    genre_lower = genre.lower()     # insensitive (action, Action, ACTION)
                    if genre_lower not in [g.lower() for g in valid_genres]:
                        print("\033[91mError: Invalid genre! "
                              "Repeat input genre as text (insensitive) in table!\033[0m")
                        continue

                    # Find the original genre (case-sensitive) for further use:
                    # находит кортеж жанра из genres_data (list(genre, min_year, max_year, film_count)),
                    # соответствующий введенному жанру (сравнение в нижнем регистре)
                    selected_genre = next(row for row in genres_data if row[0].lower() == genre_lower)
                    #next - возвращает первый элемент из итерируемого объекта, удовлетворяющий заданному условию

                    genre = selected_genre[0]  # Use original name genre case for logging and search
                    min_year, max_year = selected_genre[1], selected_genre[2]
                    if min_year is None or max_year is None:
                        print("\033[91mError: No valid year range for this genre!\033[0m")
                        continue

                    year_from = input("\033[92mEnter start year (or press Enter for min release year): \033[0m").strip()
                    year_to = input("\033[92mEnter end year (or press Enter for for max release year): \033[0m").strip()

                    # Convert input to int or set to default (min_year/max_year):
                    year_from = int(year_from) if year_from.isdigit() else min_year
                    year_to = int(year_to) if year_to.isdigit() else max_year

                    # input Errors:
                    if year_from and (year_from < min_year or year_from > max_year):
                        print(f"\033[91mError: Start year must be between {min_year} and {max_year}!\033[0m")
                        continue
                    if year_to and (year_to < min_year or year_to > max_year):
                        print(f"\033[91mError: End year must be between {min_year} and {max_year}!\033[0m")
                        continue
                    if year_from and year_to and year_from > year_to:
                        print("\033[91mError: Start year cannot be greater than end year!\033[0m")
                        continue
                    print("\033[93mStart searching...\033[0m")

                    offset = 0
                    # Get total count of films for logging to MongoDB:
                    total_count = mysql_connector.count_by_genre_and_year(genre, year_from, year_to)

                    while True:
                        try:
                            # Get list of tuples(title film, release_year, genre)
                            results = mysql_connector.search_by_genre_and_year(
                                genre, year_from, year_to, offset
                            )
                            if not results:
                                print("\033[93mNo more results found! Exit to main menu...\033[0m")
                                break

                            # print table (title film, release_year, genre):
                            formatter.print_films_table(results)

                            # Log to MogoDB only after the first query
                            if offset == 0:
                                log_writer.log_search(
                                    "genre_year",
                                    {"genre": genre, "year_from": year_from, "year_to": year_to},
                                    total_count
                                )
                            more = input("\033[92mShow next 10 results? "
                                         "('y'/'Y' - continue, another - exit to main menu...): \033[0m").lower()
                            if more.lower() != 'y':
                                print("\033[93mYour choice is 'exit to main menu'...\033[0m")
                                break
                            offset += 10
                            print("\033[93mSearching next 10 results...\033[0m")
                        except Exception as e:
                            print(f"\033[91mDatabase error: {e}\033[0m")
                            break
                except Exception as e:
                    print(f"\033[91mDatabase error: {e}\033[0m")
                    continue

            elif choice == 3:
                while True:
                    stats_choice = show_stats_submenu() # return str
                    try:
                        stats_choice = int(stats_choice)
                        if stats_choice == 1:   #1. Show popular searches
                            try:
                                #Get list (limit 5) of dicts with search_type, params, count:
                                # [{'search_type': 'keyword', 'params': {'keyword': 'age'}, 'count': 15},
                                # {'search_type':'genre_year','params':{'genre':'New','year_from':1990,'year_to': 2025}{},{}...]
                                searches = log_stats.get_popular_searches()
                                #print(searches)
                                # print top 5 popular searches:
                                formatter.print_searches_table(searches, "TOP 5 POPULAR SEARCHES")
                            except Exception as e:
                                print(f"\033[91mDatabase error: {e}\033[0m")

                        elif stats_choice == 2:
                            try:
                                #get list of dicts - last 5 unique searches
                                # [{'search_type': 'genre_year', 'params': {'genre': 'Travel', 'year_from': None, 'year_to': None}, 'timestamp': '2025-07-27T19:37:51.161715'},
                                # {'search_type': 'genre_year', 'params': {'genre': 'New', 'year_from': 1990, 'year_to': 2025}, 'timestamp': '2025-07-27T19:36:28.535526'},
                                # {'search_type': 'keyword', 'params': {'keyword': 'lion'}, 'timestamp': '2025-07-27T19:19:20.494505'},...]
                                searches = log_stats.get_recent_searches()
                                #print(searches)
                                # print 5 unique searches:
                                formatter.print_searches_table(searches, "LAST UNIQUE SEACHES")
                            except Exception as e:
                                print(f"\033[91mDatabase error: {e}\033[0m")
                        elif stats_choice == 0:
                            break  # Exit to main menu
                        else:
                            print("\033[91mError: Invalid type of statistic choice! "
                                  "Choose 1-2 or '0' for exit to main menu.\033[0m")
                    except ValueError:
                        print("\033[91mError: Please enter a number for statistic type!\033[0m")
                    except Exception as e:
                        print(f"\033[91mDatabase error: {e}\033[0m")
            elif choice == 0:
                print("\033[93mYour choice is 'Exit'... Goodbye!\033[0m")
                break
            else:
                print("\033[91mInvalid choice! Choose: 1-3 or '0' for exit\033[0m")

        except ValueError:
            print("\033[91mPlease enter a number!\033[0m")
        except Exception as e:
            print(f"\033[1mError: {e}\033[0m")


if __name__ == '__main__':
    main()



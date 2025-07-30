# Movie Search App

## Project Goal

This is a console application for searching movies in the Sakila MySQL database. It allows users to:

- Search movies by keyword in the title (e.g., "age").
- Search movies by genre (case-insensitive, e.g., "Action", "action") and year range.
- View the top 5 popular or last 5 unique searches stored in MongoDB.
- All searches are logged in MongoDB with the total number of matching films, ensuring logging happens only once per search.

## Requirements

- Python 3.8+
- MySQL with Sakila database
- MongoDB
- Python libraries: `mysql-connector-python`, `pymongo`

## Installation

1. Install Python libraries:

   ```bash
   pip install mysql-connector-python pymongo
   ```
2. Set up MySQL and MongoDB:
   - Install MySQL and load the Sakila database.
   - Install MongoDB and ensure it is running.
3. 
4. Run the app:

   ```bash
   python main.py
   ```

## Usage

- **Main Menu**: Choose options 0-3.
  - **Option 1**: Search by keyword (e.g., "age"). Logs the total number of matching films (e.g., 13).
  - **Option 2**: Search by genre (case-insensitive, e.g., "Action", "action") and year range. 
  After selecting a genre from the displayed table, enter years or press Enter to use the genre's full year range. 
  Logs the total number of matching films (e.g., 64 for Action).
  - **Option 3**: View popular (top 5 by request count) or recent (last 5 unique) searches in a submenu. 
  Stay in the submenu until choosing "Exit to main menu" (0).
  - **Option 0**: Exit the program.
- **Pagination**: Press 'y'(or 'Y') to see the next 10 results per page; any other input exits to the main menu.
- **Case Insensitivity**: Genre searches are case-insensitive (e.g., "Action", "action", or "ACTION" are treated the same).
- **Logging**: Each search is logged in MongoDB once with the total number of matching films, regardless of pagination.

## Notes

- The Sakila database contains genres like `Action`, `Sci-Fi`, etc., with films primarily from 2006. 
If the database is modified to include genres like `New` or years like `1990`, the app will handle them correctly.
- Search results are displayed in pages of 10 films.
- Popular searches show the request count; recent searches show timestamps in `YYYY-MM-DD HH:MM:SS.XX` format.
- Errors (e.g., invalid genre, empty keyword, or database connection issues) are displayed in red.

## Example Output

```
main menu: ********* MOVIE SEARCH: *********
======================================================================
1. Search by KEYWORD (Выполнить поиск по ключевому слову)
2. Search by GENRE and YEAR (Выполнить поиск по жанру и диапазону годов)
3. Show POPULAR or RECENT searches (Посмотреть популярные или последние запросы)
----------------------------------------------------------------------
0. Exit
Enter your choice (1-3 or '0' for exit): 1

Your choice is 'Search by KEYWORD'. Enter keyword: age
Start searching...

Search results (only 10 per page):
* title - release_year - genre
----------------------------------------
* AGENT TRUMAN - 2023 - Foreign
* ARMAGEDDON LOST - 2012 - Sci-Fi
* BERETS AGENT - 1998 - Action
* BIRDCAGE CASPER - 2022 - Music
* DAISY MENAGERIE - 2002 - Sci-Fi
* DOLLS RAGE - 2016 - Sci-Fi
* GENTLEMEN STAGE - 2020 - Foreign
* GRINCH MASSAGE - 2023 - Games
* HOOSIERS BIRDCAGE - 2022 - Foreign
* HOURS RAGE - 2007 - New
Show next 10 results? ('y'/'Y' - continue, another - exit to main menu...): n
Your choice is 'exit to main menu'...

main menu: ********* MOVIE SEARCH: *********
======================================================================
1. Search by KEYWORD (Выполнить поиск по ключевому слову)
2. Search by GENRE and YEAR (Выполнить поиск по жанру и диапазону годов)
3. Show POPULAR or RECENT searches (Посмотреть популярные или последние запросы)
----------------------------------------------------------------------
0. Exit
Enter your choice (1-3 or '0' for exit): 2

AVAILABLE GENRES:
============================================================
Genre: 	Min - Max release year:  	Count of films:
------------------------------------------------------------
* Action:	1990 - 2025 		Count of films: 64
* Animation:	1990 - 2025 		Count of films: 66
* Children:	1990 - 2025 		Count of films: 60
* Classics:	1990 - 2025 		Count of films: 57
* Comedy:	1990 - 2024 		Count of films: 58
* Documentary:	1990 - 2025 		Count of films: 68
* Drama:	1990 - 2025 		Count of films: 62
...
Enter genre (insensitive): action
Enter start year (or press Enter for min release year): 
Enter end year (or press Enter for max release year): 
Starting search...

Search results (only 10 per page):
* title - release_year - genre
----------------------------------------
* AMADEUS HOLY - 1994 - Action
* AMERICAN CIRCUS - 1994 - Action
* ANTITRUST TOMATOES - 1998 - Action
...
Show next 10 results? ('y'/'Y' - continue, another - exit to main menu...): y
Searching next 10 results...

Search results (only 10 per page):
* title - release_year - genre
----------------------------------------
* CASUALTIES ENCINO - 2007 - Action
* CELEBRITY HORN - 2021 - Action
* CLUELESS BUCKET - 1991 - Action
...
Show next 10 results? ('y'/'Y' - continue, another - exit to main menu...):  n
Your choice is 'exit to main menu'...

main menu: ********* MOVIE SEARCH: *********
======================================================================
1. Search by KEYWORD (Выполнить поиск по ключевому слову)
2. Search by GENRE and YEAR (Выполнить поиск по жанру и диапазону годов)
3. Show POPULAR or RECENT searches (Посмотреть популярные или последние запросы)
----------------------------------------------------------------------
0. Exit
Enter your choice (1-3 or '0' for exit): 3

Choose please STATISTICS TYPE:
============================================================
1. Show POPULAR searches (Посмотреть популярные запросы)
2. Show RECENT searches (Посмотреть последние запросы)
------------------------------------------------------------
0. Exit to main menu (Выход в основное меню)
Enter choice (1-2) or '0' for exit to main menu:  2

LAST UNIQUE SEARCHES (последние уникальные запросы):
======================================================================
search_type: 		(date_time) 		- search_params 
----------------------------------------------------------------------
genre_year:		(2025-07-30 18:03:21.58) 	- 'Action', 1990-2025
keyword:		(2025-07-30 17:00:03.58) 	- 'mill'
keyword:		(2025-07-30 16:57:34.39) 	- 'lion'
genre_year:		(2025-07-30 16:42:58.31) 	- 'New', 1990-2025
Done ...Exiting to statistics menu...

Choose please STATISTICS TYPE:
============================================================
1. Show POPULAR searches (Посмотреть популярные запросы)
2. Show RECENT searches (Посмотреть последние запросы)
------------------------------------------------------------
0. Exit to main menu (Выход в основное меню)
Enter choice (1-2) or '0' for exit to main menu: 1

TOP 5 POPULAR SEARCHES (популярные запросы):
======================================================================
search_type: (request_count) - search_params
----------------------------------------------------------------------
keyword:		(4) 	- 'age'
genre_year:		(3) 	- 'New', 1990-1990
genre_year:		(2) 	- 'New', 1990-2025
keyword:		(1) 	- 'mill'
keyword:		(1) 	- 'lion'
Done ...Exit to statistics menu...

Choose please STATISTICS TYPE:
============================================================
1. Show POPULAR searches (Посмотреть популярные запросы)
2. Show RECENT searches (Посмотреть последние запросы)
------------------------------------------------------------
0. Exit to main menu (Выход в основное меню)
Enter choice (1-2) or '0' for exit to main menu: 0

======================================================================
main menu: 	********* MOVIE SEARCH: *********
======================================================================
1. Search by KEYWORD (Выполнить поиск по ключевому слову)
2. Search by GENRE and YEAR (Выполнить поиск по жанру и диапазону годов)
3. Show POPULAR or RECENT searches (Посмотреть популярные или последние запросы)
----------------------------------------------------------------------
0. Exit
Enter your choice (1-3 or '0' for exit):0

Your choice is 'Exit'...Goodbye!
```
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

3. The file structure of the project:
movie_search_app/
├── formatter.py
├── log_stats.py
├── log_writer.py
├── main.py
├── mysql_connector.py
└── README.md

+ formatter.py:
Python file to show data as tables.
Prints movies, genres, and search stats (popular or recent).
Makes output easy to read with headers and formatting.

+ log_stats.py:
Python file to get search stats from MongoDB.
Shows top 5 popular searches and last 5 unique searches.

+ log_writer.py:
Python file to save search queries to MongoDB.
Logs search type, parameters, and total number of matching movies.

+ main.py:
Python file with the main program.
Shows menu, handles user input, and runs searches.
Calls other files to search, log, and show results.

+ mysql_connector.py:
Python file to connect to MySQL (Sakila database).
Searches movies by keyword or genre/year and counts total matches.

+ README.md:
Markdown file with project info.
Explains how to install, use, and what the app does.
Includes example output and setup steps.

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
===================================================
1. Search by KEYWORD
2. Search by GENRE and YEAR
3. Show POPULAR or RECENT searches
---------------------------------------------------
0. Exit
Enter your choice (1-3 or '0' for exit): 1

Your choice is 'Search by KEYWORD'. Enter keyword: age
Start searching...

Search results (only 10 per page):
==================================================
genre        release year     title
--------------------------------------------------
* Foreign        2023         AGENT TRUMAN 
* Sci-Fi         2012         ARMAGEDDON LOST 
* Action         1998         BERETS AGENT 
* Music          2022         BIRDCAGE CASPER 
* Sci-Fi         2002         DAISY MENAGERIE 
* Sci-Fi         2016         DOLLS RAGE 
* Foreign        2020         GENTLEMEN STAGE 
* Games          2023         GRINCH MASSAGE 
* Foreign        2022         HOOSIERS BIRDCAGE 
* New            2007         HOURS RAGE 
Show next 10 results? ('y'/'Y' - continue, another - exit to main menu...): n
Your choice is 'exit to main menu'...

main menu: ********* MOVIE SEARCH: *********
==================================================
1. Search by KEYWORD
2. Search by GENRE and YEAR
3. Show POPULAR or RECENT searches
--------------------------------------------------
0. Exit
Enter your choice (1-3 or '0' for exit): 2

AVAILABLE GENRES:
==================================================
Genre            Min - Max year   Count of films
--------------------------------------------------
* Action           1990 - 2025       (64)
* Animation        1990 - 2025       (66)
* Children         1990 - 2025       (60)
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
==================================================
genre        release year     title
--------------------------------------------------
* Action         1994         AMADEUS HOLY 
* Action         1994         AMERICAN CIRCUS 
* Action         1998         ANTITRUST TOMATOES 
* Action         2011         ARK RIDGEMONT 
...
Show next 10 results? ('y'/'Y' - continue, another - exit to main menu...):  n
Your choice is 'exit to main menu'...

main menu: ********* MOVIE SEARCH: *********
=====================================================
1. Search by KEYWORD 
2. Search by GENRE and YEAR 
3. Show POPULAR or RECENT searches
-----------------------------------------------------
0. Exit
Enter your choice (1-3 or '0' for exit): 3

Choose please STATISTICS TYPE:
======================================================
1. Show POPULAR searches 
2. Show RECENT searches
------------------------------------------------------
0. Exit to main menu
Enter choice (1-2) or '0' for exit to main menu:  2

LAST UNIQUE SEARCHES:
======================================================================
search_type: 		(date_time) 		- search_params 
----------------------------------------------------------------------
genre_year:		(2025-07-30 18:03:21.58) 	- 'Action', 1990-2025
keyword:		(2025-07-30 17:00:03.58) 	- 'mill'
keyword:		(2025-07-30 16:57:34.39) 	- 'lion'
genre_year:		(2025-07-30 16:42:58.31) 	- 'New', 1990-2025
Done! Exiting to statistics menu...

Choose please STATISTICS TYPE:
============================================================
1. Show POPULAR searches 
2. Show RECENT searches 
------------------------------------------------------------
0. Exit to main menu 
Enter choice (1-2) or '0' for exit to main menu: 1

TOP 5 POPULAR SEARCHES:
======================================================================
search_type: (request_count) - search_params
----------------------------------------------------------------------
keyword:		(4) 	- 'age'
genre_year:		(3) 	- 'New', 1990-1990
genre_year:		(2) 	- 'New', 1990-2025
keyword:		(1) 	- 'mill'
keyword:		(1) 	- 'lion'
Done! Exit to statistics menu...

Choose please STATISTICS TYPE:
============================================================
1. Show POPULAR searches
2. Show RECENT searches
------------------------------------------------------------
0. Exit to main menu
Enter choice (1-2) or '0' for exit to main menu: 0

==========================================================
main menu: 	********* MOVIE SEARCH: *********
==========================================================
1. Search by KEYWORD
2. Search by GENRE and YEAR
3. Show POPULAR or RECENT searches
----------------------------------------------------------
0. Exit
Enter your choice (1-3 or '0' for exit):0

Your choice is 'Exit'...Goodbye!
```
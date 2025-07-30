# Connect to MySQL and search movies

import mysql.connector
from mysql.connector import Error


#from env import HOST_NAME
def connect_db():
    """Connect to MySQL database.

    Input: None
    Output: MySQL connection object or raises error
    """
    try:
        conn = mysql.connector.connect(
            host="ich-db.edu.itcareerhub.de",
            user="ich1",
            password="password",
            database="sakila"
            )
        return conn # connection to My SQL
    except Error as e:
        raise Exception(f"\033[91mCannot connect to MySQL: {e}\033[0m")



def search_by_keyword(keyword, offset):
    """Search movies by keyword in title.

    Input:
        keyword (str): Word to search in title
        offset (int): Number of results to skip
    Output: List of tuples (title, year, genre)
    """
    conn = connect_db()     # connection to BD
    cursor = conn.cursor(dictionary=False)
    query = """
        SELECT f.title, f.release_year, c.name 
        FROM film AS f
        JOIN film_category AS fc ON f.film_id = fc.film_id
        JOIN category AS c ON fc.category_id = c.category_id
        WHERE f.title LIKE %s
        LIMIT 10 OFFSET %s
    """
    cursor.execute(query, (f"%{keyword}%", offset)) # MySQL не чувствительный к регистру (иначе keyword.lower())
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def count_by_keyword(keyword):
    """Count total movies matching keyword in title.
    Input:
        keyword (str): Word to search in title
    Output: Integer (total number of matching films)
    """
    conn = connect_db()
    cursor = conn.cursor()
    query = """
        SELECT COUNT(*)
        FROM film AS f
        JOIN film_category AS fc ON f.film_id = fc.film_id
        JOIN category AS c ON fc.category_id = c.category_id
        WHERE f.title LIKE %s
    """
    cursor.execute(query, (f"%{keyword}%",))
    total = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return total

def get_genres_with_details():
    """Get all genres with their year range and film count.

    Input: None
    Output: List of tuples (genre, min_year, max_year, film_count)
    """
    conn = connect_db()
    cursor = conn.cursor()
    query = """
        SELECT
            c.name,
            MIN(f.release_year),
            MAX(f.release_year),
            COUNT(*) AS film_count
        FROM film f
        JOIN film_category fc ON f.film_id = fc.film_id
        JOIN category c ON fc.category_id = c.category_id
        GROUP BY c.name
        ORDER BY c.name
    """
    cursor.execute(query)
    results = cursor.fetchall()  # Returns list of tuples (genre, min_year, max_year, film_count)
    cursor.close()
    conn.close()
    # Convert min_year and max_year to int, handle None
    return [(row[0],
             int(row[1]) if row[1] is not None else None,
             int(row[2]) if row[2] is not None else None,
             row[3]) for row in results]


def search_by_genre_and_year(genre, year_from, year_to, offset):
    """Search movies by genre and year range.

    Input:
        genre (str): Genre name to search
        year_from (int or None): Start year or None
        year_to (int or None): End year or None
        offset (int): Number of results to skip
    Output: List of tuples (title, year, genre)
    """
    conn = connect_db()
    cursor = conn.cursor()  # (dictionary=False)
    query = """
        SELECT f.title, f.release_year, c.name
        FROM film AS f
        JOIN film_category AS fc ON f.film_id = fc.film_id
        JOIN category AS c ON fc.category_id = c.category_id
        WHERE c.name = %s
    """
    params = [genre]    # %s=[genre, year_from, year_to]
    if year_from:       # if user input
        query += " AND f.release_year >= %s"    # (add film.release_year to query als %s)
        params.append(year_from)
    if year_to:         # if user input
        query += " AND f.release_year <= %s"
        params.append(year_to)
    query += " LIMIT 10 OFFSET %s"
    params.append(offset)
    cursor.execute(query, params)
    results = cursor.fetchall()  # Returns list of tuples
    cursor.close()
    conn.close()
    return results

def count_by_genre_and_year(genre, year_from, year_to):
    """Count total movies matching genre and year range.
    Input:
        genre (str): Genre name to search
        year_from (int or None): Start year or None
        year_to (int or None): End year or None
    Output: Integer (total number of matching films)
    """
    conn = connect_db()
    cursor = conn.cursor()
    query = """
        SELECT COUNT(*)
        FROM film AS f
        JOIN film_category AS fc ON f.film_id = fc.film_id
        JOIN category AS c ON fc.category_id = c.category_id
        WHERE c.name = %s
    """
    params = [genre]
    if year_from:
        query += " AND f.release_year >= %s"
        params.append(year_from)
    if year_to:
        query += " AND f.release_year <= %s"
        params.append(year_to)
    cursor.execute(query, params)
    total = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return total
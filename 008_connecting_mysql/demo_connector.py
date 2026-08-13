import os
import mysql.connector
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

def main():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", 3306)),
        user=os.getenv("DB_USER", "root"),
        passwd=os.getenv("DB_PASSWORD", ""),
        db=os.getenv("DB_NAME", "sakila")
    )

    cursor = conn.cursor()

    print("[fetchall] Top 5 Longest films in Sakila")

    query_longest_films = '''
        SELECT title, length, rental_rate
        FROM film
        ORDER BY length DESC
        LIMIT 5;
    '''

    cursor.execute(query_longest_films)

    longest_films = cursor.fetchall()

    # print(longest_films)

    for line in longest_films:
        print(f'- Film: {line[0]} | Duration: {line[1]} mins | Rental Rate: ${line[2]}')


    print(f'\n\n[fetchone] Retrieve a specific film details:')

    query_specific_film = '''
        SELECT title, description, release_year, rating
        FROM film
        WHERE title = %s;
    '''

    cursor.execute(query_specific_film, ("ACADEMY DINOSAUR",))

    film_details = cursor.fetchone()

    if film_details:
        print(f' - Title: {film_details[0]}')
        print(f' - Description: {film_details[1]}')
        print(f' - Year: {film_details[2]} | Rating: {film_details[3]}')
    else:
        print("Film not found")


    print(f'\n\n[fetchmany] Fetching actors in batches of 5:')
    cursor.execute('SELECT first_name, last_name FROM actor LIMIT 20')

    page = 1
    while True:
        batch = cursor.fetchmany(5)
        # batch = cursor.fetchone()
        if not batch:
            break
        print(f' - Batch #{page}:')
        for actor in batch:
            print(f"    * {actor[0].title()} {actor[1].title()}")
        # print(f"    * {batch[0].title()} {batch[1].title()}")
        page += 1

    print(f'[dictionary=True] Top 3 customers by total spending')

    query_top_spenders = '''
        SELECT c.first_name, c.last_name, SUM(p.amount) AS total_spent
        FROM customer c
        JOIN payment p ON c.customer_id = p.customer_id
        GROUP BY c.customer_id
        ORDER BY total_spent DESC
        LIMIT 3;
    '''

    dict_cursor = conn.cursor(dictionary=True)
    dict_cursor.execute(query_top_spenders)
    top_spenders = dict_cursor.fetchall()

    for customer in top_spenders:
        print(f' - Customer: {customer['first_name']} {customer['last_name']} | Total Spent: ${customer['total_spent']:.2f}')

    dict_cursor.close()

    print(f'\n\n[pandas dataframe integration] Loading SQL results into Pandas')

    quert_category_counts = '''
        SELECT c.name AS category_name, COUNT(fc.film_id) AS film_count
        FROM category c
        JOIN film_category fc ON c.category_id = fc.category_id
        GROUP BY c.category_id
        ORDER BY film_count DESC;
    '''

    df = pd.read_sql(quert_category_counts, conn)
    print(df.head(5))

    print(f'Total films: {df['film_count'].sum()}')

    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()
#!/usr/bin/python
 
import psycopg2
from configcust import config
 
 
def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE currency (
            	cur_id INTEGER PRIMARY KEY,
            	cur_name VARCHAR(255) NOT NULL,
		cur_sym VARCHAR(255) NOT NULL,
		web_slg VARCHAR(255) NOT NULL,
		rank INTEGER NOT NULL,
		last_updated INTEGER NOT NULL
        )
        """,
        """ CREATE TABLE supply (
                cur_id INTEGER PRIMARY KEY,
                circulating_supply real NOT NULL,
		total_supply real NOT NULL,
		max_supply real NOT NULL,
		FOREIGN KEY (cur_id)
                    REFERENCES currency (cur_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE quotes (
		quote_id SERIAL NOT NULL,
                cur_id INTEGER NOT NULL,
                quote_name VARCHAR(255) NOT NULL,
                PRIMARY KEY (cur_id, quote_id),
		FOREIGN KEY (cur_id)
                    REFERENCES currency (cur_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE quote_info (
                quote_id INTEGER NOT NULL,
                cur_id INTEGER NOT NULL,
		price real NOT NULL,
		volume real NOT NULL,
		market_cap real NOT NULL,
		percent_change_1h real NOT NULL,
		percent_change_24h real NOT NULL,
		percent_change_7d real NOT NULL,
                PRIMARY KEY (cur_id , quote_id),
                FOREIGN KEY (cur_id, quote_id)
                    REFERENCES quotes (cur_id, quote_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
 
if __name__ == '__main__':
    create_tables()


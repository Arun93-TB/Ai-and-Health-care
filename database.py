import mysql.connector
from mysql.connector import Error
from config import HOST, USER, PASSWORD, DATABASE


def get_connection():

    try:

        connection = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )

        if connection.is_connected():

            print("===================================")
            print("✅ MySQL Connected Successfully!")
            print("Database :", DATABASE)
            print("User     :", USER)
            print("===================================")

            return connection

    except Error as e:

        print("===================================")
        print("❌ MySQL Connection Failed")
        print("Error :", e)
        print("===================================")

        return None


def close_connection(connection):

    if connection is not None and connection.is_connected():

        connection.close()

        print("✅ Connection Closed")


if __name__ == "__main__":

    conn = get_connection()

    if conn:
        close_connection(conn)
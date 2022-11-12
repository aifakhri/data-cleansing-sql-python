import sqlite3

from sqlite3 import Error



def open_connection():
    """
    This function is used to create connection to the database

    Return Value:
    connection object if the connection is establisehd
    Otherwise None
    """
    connection = None
    try:
        connection = sqlite3.connect("olist.db")
        print("Connection is successful")
        return connection
    except Error as e:
        print("Connection failed")
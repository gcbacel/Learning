###################################################################################
##   Python sample code to handle database connections, queries and migrations   ##
##   Author: Gunther Bacellar                                                    ##
##   Email: gcbacel@hotmail.com                                                  ##
###################################################################################

from sqlalchemy import create_engine
import mysql.connector as msql

# code 1: Function to migrate a dataframe to a database using sqlalchemy and mysql libraries
def migrate_df_to_db(DATA_FRAME, DB_TABLE, ACTION, DB_HOST, DB_NAME, DB_USER, DB_PASS, DB_DRIVER = 'mysql+pymysql'):
    # url format: dialect[+driver]://user:password@host/dbname[?key=value..]
    # dialect is a database name such as 'mysql', 'oracle', 'postgresql' and driver is the name of a DBAPI, such as 'pymysql', 'psycopg2', 'pyodbc', 'cx_oracle'
    # DB_HOST, DB_NAME, DB_USER, DB_PASS: Database host, name, user and password
    # action: {'fail', 'replace', 'append'}.  How to behave if the table already exists
    url = DB_DRIVER + f"://{DB_USER}:{DB_PASS}@{DB_HOST}:3306/{DB_NAME}"
    conn = msql.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
    engine = create_engine(url)
    DATA_FRAME.to_sql(DB_TABLE, con = engine, if_exists = ACTION, chunksize = 1000,index=False)


# code 2: create a connection to a mysql database and make queries
import pymysql
class DB:
    def __init__(self, **params):
        params.setdefault("charset", "utf8mb4")
        params.setdefault("cursorclass", pymysql.cursors.DictCursor)
        self.mysql = pymysql.connect(**params)
    def close(self):
        with self.mysql.cursor() as cursor:
            return cursor.close()
    def query(self, sql, *id):
        with self.mysql.cursor() as cursor:
            if id:
                cursor.execute(sql, id)
                return cursor.fetchone()
            else:    
                cursor.execute(sql)
                sql = sql.lower()
                if ('insert' in sql) or ('create' in sql) or ('delete' in sql) or ('drop' in sql): 
                    return self.mysql.commit()
                else: 
                    return cursor.fetchall()

# Examples using Python to run SQL requires in a database
DB_HOST='<enter here the host connection to mysql>'
DB_USER='<enter here your user>'
DB_PASS='<enter here your password>'
DB_NAME='<enter here your database name>'
db = DB(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DB_NAME)
db.query('CREATE DATABASE MWdb')   # create database mydb
db.query("CREATE TABLE mydb.customers (id INT NOT NULL, hero VARCHAR(50), name VARCHAR(50), city VARCHAR(50), age INT, PRIMARY KEY (id))") # create a table
db.query("INSERT INTO mydb(id, name, city, age) VALUES (1, 'Ana', 'Fortaleza', 56)")  # insert a new row
db.query("SELECT MAX(id) AS Max_Id FROM customers") # find the max id of table customers
id = 1
db.query("SELECT id, hero, power, name, xp, color FROM heros WHERE id=%s", (id,))  # select row with id = 1
db.query("DELETE FROM customers WHERE id>25")  # delete rows of table customers
db.query("DROP TABLE mydb.customers"  # drop the table customers in the database mydb

import sqlite3
from sqlite3 import Error

class DataBase():
    def create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return conn

    def add(self, conn, sql):
        """ Execute sql
        :param conn: Connection object
        :param sql: a SQL script
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(sql)
            conn.commit() 
            conn.close()
            return 
        except Error as e:
            print(e)


if __name__ == "__main__":

   create_projects_sql = """
   -- projects table
   CREATE TABLE IF NOT EXISTS projects (
      id integer PRIMARY KEY,
      nazwa text NOT NULL,
      start_date text,
      end_date text
   );
   """

   create_tasks_sql = """
   -- zadanie table
   CREATE TABLE IF NOT EXISTS tasks (
      id integer PRIMARY KEY,
      projekt_id integer NOT NULL,
      nazwa VARCHAR(250) NOT NULL,
      opis TEXT,
      status VARCHAR(15) NOT NULL,
      start_date text NOT NULL,
      end_date text NOT NULL,
      FOREIGN KEY (projekt_id) REFERENCES projects (id)
   );
   """
project =  """INSERT INTO projects (id, nazwa, start_date, end_date)
            VALUES (1,
           "Zrób zadania",
           "2020-05-08 00:00:00",
           "2020-05-10 00:00:00")"""

task =  """INSERT INTO tasks (projekt_id, nazwa, opis, status, start_date, end_date)
            VALUES (2,
           "Task_2",
           "Umyj zeby",
           "To do",
           "2020-05-08 00:00:00",
           "2020-05-10 00:00:00")"""


db_file = "database1.db"

db = DataBase()

conn = db.create_connection(db_file)
if conn is not None:
    task_id = db.add(conn, task)
      



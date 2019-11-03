import os
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print("...DB Connection Ready...")
        return conn
    except Error as e:
        print(e)

def create_table(conn, create_table_sql, table_name):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :param table_name: name of table
    :return: None
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print("{} Table is created".format(table_name))
    except Error as e:
        print(e)

def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn: sql connection object
    :param project: contains project details
    :return: project id
    """
    sql_query = ''' INSERT INTO projects(name, begin_date, end_date)
                    VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql_query, project)
    print("...Inserted in Project Table..")
    return cur.lastrowid

def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
 
    sql_query = ''' INSERT INTO tasks(name, priority, status_id,
                project_id,begin_date,end_date)
                VALUES(?, ?, ?, ?, ?, ?) '''
    cur = conn.cursor()
    cur.execute(sql_query, task)
    print("....Inserted in Task Table....")
    return cur.lastrowid

def update_task(conn, task):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE tasks
              SET priority = ? ,
                  begin_date = ? ,
                  end_date = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    print("...Task Table updated..")

def delete_task(conn, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM tasks WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    print("...Task entry deleted...")

def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    rows = cur.fetchall() 
    for row in rows:
        print("Each entry in task table is ", row)
 
def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
    rows = cur.fetchall()
    for row in rows:
        print("Each entry in Task table by Prriority is ",row)

def start_db(db_file_pth):
    sql_create_projects_table = """CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    );"""
 
    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""
 
    # create a database connection
    conn = create_connection(db_file_pth)
    if conn:
        # create projects table
        create_table(conn, sql_create_projects_table, "Projects")
        # create tasks table
        create_table(conn, sql_create_tasks_table, "Tasks")
        with conn:
            project = ('Cool App with SQLite & Python', '2019-11-03', '2019-11-30');
            project_id = create_project(conn, project)
            print("Project id is", project_id)
    
            # tasks
            task_1 = ('Analyze the requirements of the app', 1, 1, project_id,
                      '2019-11-03', '2019-11-06')
            task_2 = ('Confirm with user about the top requirements', 1, 1, project_id,
                      '2019-11-07', '2019-11-08')
            task_3 = ('Designing UI', 2, 1, 1, '2019-11-08', '2019-11-08')
            task_4 = ('Wireframing of Design', 2, 1, 1, '2019-11-08', '2019-11-09')
            task_5 = ('Testing UI on BrowserStack', 3, 1, 1, '2019-11-09', '2019-11-09')
            # create tasks
            create_task(conn, task_1)
            create_task(conn, task_2)
            create_task(conn, task_3)
            create_task(conn, task_4)
            create_task(conn, task_5)

            print("1. Query task by priority:")
            select_task_by_priority(conn,3)
            print("2. Query all tasks")
            select_all_tasks(conn)
            update_task(conn, (5, '2019-11-12', '2019-11-13',2))
            select_all_tasks(conn)
            delete_task(conn, 2)
            select_all_tasks(conn)
    else:
        print("Error! cannot create the database connection.")

 
if __name__ == "__main__":

    abs_path = os.path.dirname(os.path.basename(__file__))
    db_name = "project_managment.db"
    db_path = os.path.join(abs_path, db_name)
    start_db(db_path)
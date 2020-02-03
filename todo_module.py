import sqlite3
import time
from datetime import datetime


class Table:

    def __init__(self, name, database):
        self.database = database
        self.name = name

        self.conn = sqlite3.connect(self.database)
        self.c = self.conn.cursor()

        self.c.execute("CREATE TABLE IF NOT EXISTS {}(id REAL, \
            time_stamp TEXT, \
            task TEXT, \
            description TEXT, \
            timer REAL, \
            completed BIT)".format(self.name))


    def add_task(self, task):
        """
        Add task to Table

        Arguments:
        task(instance): Instance of Task class to be added to table
        """
        vals = (task.id,
            task.time_stamp, 
            task.task_name, 
            task.description,
            task.timer,
            task.completed)

        self.c.execute("INSERT INTO {} VALUES(?, ?, ?, ?, ?, ?)".format(self.name), vals)
        self.conn.commit()
        self.c.close()
        self.conn.close()

    def edit_task(self, update_val, update_col, index_val, index_col='id'):
        self.c.execute("UPDATE {} SET {} = {} WHERE {} = {}".format(self.name, update_col, update_val, index_col, index_val))
        self.conn.commit()
        self.c.close()
        self.conn.close()

    def del_task(self, index_val, index_col='id'):
        """
        Deletes task from table by indexing with col

        Arguments:
        index_col(str): Column name to index by as string
        index_val: value column is filtered for
        """
        self.c.execute("DELETE FROM {} WHERE {} = {}".format(self.name, index_col, index_val))
        self.conn.commit()
        self.c.close()
        self.conn.close()

    def display(self):
        """
        Displays tasks that need to be done i.e. incomplete tasks
        """
        self.c.execute("SELECT * FROM {} WHERE complete = 0".format(self.name))
        self.conn.commit()
        self.c.close()
        self.conn.close()

    def display_all(self):
        """
        Displays all tasks, complete and incomplete
        """
        self.c.execute("SELECT * FROM {}".format(self.name))
        self.conn.commit()
        self.c.close()
        self.conn.close()


        

class Task:

    ids = []
    n = 1

    def __init__(self, task_name, description='', timer=0):
        """
        Changes task to complete in SQL table representing task completion

        Arguments:
        task_name(str): string corresponding to task name
        description(str): description of task
        timer(int, 0-2): encoding representing type of timer for task:
            0 = None
            1 = Deadline, user sets time to be reminded
            2 = Countdown, user sets interval from time of entry 
        """
        unix = int(time.time())
        self.time_stamp = datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S')

        self.task_name = task_name
        self.description = description
        self.timer = timer  
        self.completed = 0

        if Task.n in Task.ids:
            Task.n = max(ids) + 1           
        self.id = Task.n
        Task.ids.append(self.id)
        Task.n += 1

    def complete(self):
        """
        Changes instance attribute completed to 1, representing task completion
        """
        self.completed = 1


t = Table('todo1','todo1.db')
#task1 = Task('Commit to Git', 'Do it.', '0')
#t.add_task(task1)
t.edit_task('eat shit', 'task', 1.0, 'id')


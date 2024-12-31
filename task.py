import sqlite3
import logging

# Define the Task class
class Task:
    _id_counter = 1

    def __init__(self, title, status, brain_id):
        self.id = Task._id_counter
        Task._id_counter += 1
        self.title = title
        self.status = status
        self.brain_id = brain_id
        logging.info(f"Task created: {self.title} with status {self.status}")

        # Assuming the database and table already exist
        self.db_connection = sqlite3.connect('brain.db')  # Connect to the SQLite DB
        self.db_cursor = self.db_connection.cursor()

    def _execute_query(self, query, params=()):
        """ Helper method to execute database queries """
        self.db_cursor.execute(query, params)
        self.db_connection.commit()

    def create_task(self):
        """ Method to create a task in the database """
        query = "INSERT INTO Task (title, status, brain_id) VALUES (?, ?, ?)"
        params = (self.title, self.status, self.brain_id)
        self._execute_query(query, params)
        logging.info(f"Task '{self.title}' created in the database.")

    def get_task_by_id(self, task_id):
        """ Method to retrieve a task by its ID """
        query = "SELECT * FROM Task WHERE id = ?"
        self.db_cursor.execute(query, (task_id,))
        task = self.db_cursor.fetchone()
        logging.info(f"Retrieved task: {task}")
        return task

    def update_status(self, task_id, new_status):
        """ Method to update the status of a task """
        query = "UPDATE Task SET status = ? WHERE id = ?"
        params = (new_status, task_id)
        self._execute_query(query, params)
        logging.info(f"Task {task_id} status updated to {new_status}")

    def delete_task(self, task_id):
        """ Method to delete a task from the database """
        query = "DELETE FROM Task WHERE id = ?"
        self._execute_query(query, (task_id,))
        logging.info(f"Task {task_id} deleted from the database.")

    def __repr__(self):
        return f"Task({self.title}, {self.status})"

    def close_connection(self):
        """ Method to close the database connection """
        self.db_cursor.close()
        self.db_connection.close()


# Example Usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Example: Creating a new task
    task1 = Task(title="Complete Brain Model", status="In Progress", brain_id=1)
    task1.create_task()

    # Example: Get task by ID
    task = task1.get_task_by_id(1)
    print(task)

    # Example: Update task status
    task1.update_status(1, "Completed")

    # Example: Delete a task
    task1.delete_task(1)

    # Close connection to the database
    task1.close_connection()


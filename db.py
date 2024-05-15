import mysql.connector


class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user='root',
            password="0173276",
            database="student_management"
        )
        self.cursor = self.connection.cursor()

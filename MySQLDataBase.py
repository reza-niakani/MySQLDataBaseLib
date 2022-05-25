import mysql.connector


class MySQLDataBase:
    def __init__(self, host: str, user: str, password: str) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database = None
        self.cursor = None
        self.connect()

    def connect(self):
        """ Connect to mysql server
        """
        self.database = mysql.connector.connect(
            host="localhost",
            user="reza",
            passwd="2050776837"
        )
        self.cursor = self.database.cursor()

    def execute(self, query: str) -> list:
        """Execute a sql query

        Args:
            query (str): sql query

        Returns:
            list: sql query result
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        """ Close the mysql server connection
        """
        self.database.close()

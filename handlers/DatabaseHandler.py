from database.Connection import Connection
from config.Config import Config
from infrastructure.FileReader import FileReader

conn = Connection
config = Config


class DatabaseHandler:
    @staticmethod
    def execute(statement):
        connection = None

        try:
            connection = conn.get_connection()
            connection.autocommit = True
            cursor = connection.cursor()
            cursor.execute(statement)

            data = cursor.fetchall()

            cursor.close()

            return data

        except Exception as e:
            print(e)
            return False

        finally:
            if connection:
                connection.close()

    @staticmethod
    def execute_non_query(statement):
        connection = None

        try:
            connection = conn.get_connection()
            connection.autocommit = True
            cursor = connection.cursor()
            cursor.execute(statement)

            cursor.close()

        except Exception as e:
            print(e)
            return False

        finally:

            connection.commit()
            if connection:
                connection.close()

    @staticmethod
    def execute_multiple_statements(statements):
        connection = None

        try:
            connection = conn.get_connection()
            connection.autocommit = True
            cursor = connection.cursor()

            for statement in statements:
                cursor.execute(statement)

            cursor.close()

        except Exception as e:
            print(e)
            return False

        finally:

            connection.commit()
            if connection:
                connection.close()

import configparser
import psycopg2


class CleanMigrations:
    connection = 0
    cursor = 0

    def __init__(self):
        config = configparser.ConfigParser()
        config.read("settings.ini")
        self.connection = psycopg2.connect(
            dbname=config["postgres"]["dbname"],
            user=config["postgres"]["user"],
            password=config["postgres"]["password"],
            host=config["postgres"]["host"]
        )
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()
        self.cursor.close()

    def coursesTable(self):
        self.cursor.execute(
            "TRUNCATE TABLE course;"
        )
        self.connection.commit()

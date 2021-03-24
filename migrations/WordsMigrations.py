import configparser
import psycopg2


class WordsMigrations:
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
        self.cursor.close()
        self.connection.close()

    def courseKeywordsTable(self):
        self.cursor.execute(
            "CREATE TABLE courses_keyword ("
            "id              SERIAL PRIMARY KEY,"
            "name            TEXT NOT NULL UNIQUE,"
            "frequency       BIGINT);"
        )
        self.connection.commit()

    def categoriesKeywordsTable(self):
        self.cursor.execute(
            "CREATE TABLE categories_keyword ("
            "id              SERIAL PRIMARY KEY,"
            "name            TEXT NOT NULL UNIQUE,"
            "frequency       BIGINT);"
        )
        self.connection.commit()
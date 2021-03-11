import configparser
import psycopg2


class CoursesMigrations:
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

    def coursesCountTable(self):
        self.cursor.execute(
            "CREATE TABLE courses_count ("
            "id              SERIAL PRIMARY KEY,"
            "platform        VARCHAR(100) NOT NULL,"
            "courses_count   BIGINT);"
        )
        self.connection.commit()

    def coursesTable(self):
        self.cursor.execute(
            "CREATE TABLE course ("
            "id              SERIAL PRIMARY KEY,"
            "name            VARCHAR(255) NOT NULL,"
            "category_id     BIGINT,"
            "platform        VARCHAR(255) NOT NULL,"
            "link            VARCHAR(255) NOT NULL,"
            "description     TEXT,"
            "content         TEXT,"
            "sphere         VARCHAR(255),"
            "FOREIGN KEY (category_id) REFERENCES category (id));"
        )
        self.connection.commit()

    def categoriesTable(self):
        self.cursor.execute(
            "CREATE TABLE category ("
            "id                  SERIAL PRIMARY KEY,"
            "name                VARCHAR(100) NOT NULL,"
            "okso_number         BIGINT NOT NULL,"
            "okso_group_number  BIGINT NOT NULL);"
        )
        self.connection.commit()

    def categoriesGroupsTable(self):
        self.cursor.execute(
            "CREATE TABLE categories_group ("
            "id                  SERIAL PRIMARY KEY,"
            "name                VARCHAR(100) NOT NULL,"
            "okso_number         BIGINT NOT NULL,"
            "okso_sphere_number  BIGINT NOT NULL);"
        )
        self.connection.commit()

    def educationSpheresTable(self):
        self.cursor.execute(
            "CREATE TABLE education_sphere ("
            "id                  SERIAL PRIMARY KEY,"
            "name                VARCHAR(100) NOT NULL,"
            "okso_number         BIGINT NOT NULL);"
        )
        self.connection.commit()

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
            "categories      TEXT,"
            "platform        VARCHAR(255) NOT NULL,"
            "link            VARCHAR(255) NOT NULL UNIQUE,"
            "description     TEXT,"
            "content         TEXT,"
            "sphere          VARCHAR(255),"
            "keywords        TEXT);"
        )
        self.connection.commit()

    def categoriesTable(self):
        self.cursor.execute(
            "CREATE TABLE category ("
            "id                  SERIAL PRIMARY KEY,"
            "name                VARCHAR(100) NOT NULL,"
            "okso_number         BIGINT NOT NULL,"
            "okso_group_number   BIGINT NOT NULL);"
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

    def courseCategoryRelation(self):
        self.cursor.execute(
            "CREATE TABLE course_category_relation ("
            "id                  SERIAL PRIMARY KEY,"
            "course_id           BIGINT NOT NULL,"
            "category_id         BIGINT NOT NULL)"
            "FOREIGN KEY (course_id) REFERENCES course (id));"
            "FOREIGN KEY (category_id) REFERENCES category (id));"
        )
        self.connection.commit()

    def coursesRelation(self):
        self.cursor.execute(
            "CREATE TABLE courses_relation ("
            "id                         SERIAL PRIMARY KEY,"
            "left_course_id             BIGINT NOT NULL,"
            "right_course_id            BIGINT NOT NULL,"
            "estimation                 DOUBLE PRECISION,"
            "FOREIGN KEY (left_course_id) REFERENCES course (id),"
            "FOREIGN KEY (right_course_id) REFERENCES course (id),"
            "UNIQUE(left_course_id, right_course_id));"
        )
        self.connection.commit()
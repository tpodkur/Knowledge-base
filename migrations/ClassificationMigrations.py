import configparser
import psycopg2


class ClassificationMigrations:
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

    def firstLevelClassificationTable(self):
        self.cursor.execute(
            "CREATE TABLE classification_first_level ("
            "id              SERIAL PRIMARY KEY,"
            "name            TEXT NOT NULL,"
            "grnti_number    BIGINT NOT NULL UNIQUE);"
        )
        self.connection.commit()

    def secondLevelClassificationTable(self):
        self.cursor.execute(
            "CREATE TABLE classification_second_level ("
            "id                   SERIAL PRIMARY KEY,"
            "name                 TEXT NOT NULL,"
            "grnti_number         BIGINT NOT NULL,"
            "parent_grnti_number  BIGINT NOT NULL,"
            "keywords             TEXT,"
            "UNIQUE(grnti_number, parent_grnti_number));"
        )
        self.connection.commit()

    def thirdLevelClassificationTable(self):
        self.cursor.execute(
            "CREATE TABLE classification_third_level ("
            "id                          SERIAL PRIMARY KEY,"
            "name                        TEXT NOT NULL,"
            "grnti_number                BIGINT NOT NULL,"
            "parent_grnti_number         BIGINT NOT NULL,"
            "parent_parent_grnti_number  BIGINT NOT NULL,"
            "UNIQUE(grnti_number, parent_grnti_number, parent_parent_grnti_number));"
        )
        self.connection.commit()

    def courseSecondLevelRelation(self):
        self.cursor.execute(
            "CREATE TABLE course_second_level_relation ("
            "id                         SERIAL PRIMARY KEY,"
            "course_id                  BIGINT NOT NULL,"
            "category_id                BIGINT NOT NULL,"
            "keywords_intersection      TEXT,"
            "number_of_common_keywords  BIGINT,"
            "estimation                 DOUBLE PRECISION,"
            "FOREIGN KEY (course_id) REFERENCES course (id),"
            "FOREIGN KEY (category_id) REFERENCES classification_second_level (id),"
            "UNIQUE(course_id, category_id));"
        )
        self.connection.commit()

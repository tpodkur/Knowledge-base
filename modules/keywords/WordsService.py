import configparser
import psycopg2
import string


class WordsService:
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

    def getAllCourses(self):
        self.cursor.execute(
            "SELECT * FROM course;"
        )
        return self.cursor.fetchall()

    def insertKeywordsToCourse(self, keywords: string, id: int):
        print(keywords)
        self.cursor.execute(
            "UPDATE course "
            "SET keywords = %s "
            "WHERE id = %s;",
            (keywords, id)
        )
        self.connection.commit()

    def completeKeywordsFromCourses(self):
        courses = self.getAllCourses()

        for course in courses:
            keywords = course[8]
            keywords = keywords.split(',')

            for word in keywords:
                try:
                    self.cursor.execute(
                        "INSERT INTO keyword (name) "
                        "VALUES (%s);",
                        (word, )
                    )
                    self.connection.commit()
                except psycopg2.errors.UniqueViolation:
                    self.connection.commit()
                    continue

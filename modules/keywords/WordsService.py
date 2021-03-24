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

    def getAllKeywords(self):
        self.cursor.execute(
            "SELECT * FROM keyword;"
        )
        return self.cursor.fetchall()

    def insertKeywordsToCourse(self, keywords: string, courseId: int):
        self.cursor.execute(
            "UPDATE course "
            "SET keywords = %s "
            "WHERE id = %s;",
            (keywords, courseId)
        )
        self.connection.commit()

    def insertKeyword(self, word):
        try:
            self.cursor.execute(
                "INSERT INTO keyword (name) "
                "VALUES (%s);",
                (word, )
            )
            self.connection.commit()
        except psycopg2.errors.UniqueViolation:
            self.connection.commit()

    def updateKeywordFrequency(self, frequency: int, keywordId: int):
        self.cursor.execute(
            "UPDATE keyword "       
            "SET frequency = %s "   
            "WHERE id = %s;",
            (frequency, keywordId)
        )
        self.connection.commit()

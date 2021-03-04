import configparser
import psycopg2
import string


class ParserService:
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

    # def __del__(self):
    #     self.connection.close()
    #     self.cursor.close()

    def insertCoursesCount(self, platform: string, count: int):
        self.cursor.execute(
            "INSERT INTO courses_count (courses_count, platform) "
            "VALUES (%s, %s);",
            (count, platform)
        )
        self.connection.commit()

    def getCoursesCount(self, platform: string):
        self.cursor.execute(
            "SELECT courses_count FROM courses_count "
            "WHERE platform = %s ", (platform, )
        )
        res = self.cursor.fetchall()
        return res[0][0]

    # def insertCoursesInformation(self, name: string, category: string, description: string, content: string):

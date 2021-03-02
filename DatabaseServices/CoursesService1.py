import string
import psycopg2


class CoursesService:
    connection = 0
    cursor = 0

    def __init__(self):
        self.connection = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='postgres',
            host='localhost'
        )
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()
        self.cursor.close()

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

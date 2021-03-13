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

    def insertCourseInformation(
            self,
            name: string,
            category: string,
            platform: string,
            link: string,
            description: string,
            content: string,
            sphere: string
    ):
        self.cursor.execute(
            "INSERT INTO course (name, categories, platform, link, description, content, sphere) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s);",
            (name, category, platform, link, description, content, sphere)
        )
        self.connection.commit()

    # возвращение id только что созданной записи
        self.cursor.execute(
            "SELECT id FROM course "
            "WHERE name = %s ", (name,)
        )
        res = self.cursor.fetchall()
        return res[0][0]

    def insertCategoryInformation(self, name: string, code: string):
        codeArr = code.split('.')
        okso_number = int(codeArr[2])
        okso_group_number = int(codeArr[0])

        self.cursor.execute(
            "SELECT (name, okso_number, okso_group_number) FROM category "
            "WHERE name = %s AND okso_number = %s AND okso_group_number = %s ", (name, okso_number, okso_group_number)
        )
        res = self.cursor.fetchall()

        if not res:
            self.cursor.execute(
                "INSERT INTO category (name, okso_number, okso_group_number) "
                "VALUES (%s, %s, %s);",
                (name, okso_number, okso_group_number)
            )
            self.connection.commit()
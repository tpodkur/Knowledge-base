import configparser
import psycopg2
import string


class WordsService:

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

    def getAllCoursesKeywords(self):
        self.cursor.execute(
            "SELECT * FROM courses_keyword;"
        )
        return self.cursor.fetchall()

    def getAllCategoriesKeywords(self):
        self.cursor.execute(
            "SELECT * FROM categories_keyword;"
        )
        return self.cursor.fetchall()

    def getAllSecondLevelCategories(self):
        self.cursor.execute(
            "SELECT * FROM classification_second_level;"
        )
        return self.cursor.fetchall()

    def getThirdLevelCategoriesByParent(self, parentNumber: int):
        self.cursor.execute(
            "SELECT * "
            "FROM classification_third_level "
            "WHERE parent_grnti_number = %s", (parentNumber,)
        )
        return self.cursor.fetchall()

    def updateCourseKeywords(self, keywords: string, courseId: int):
        self.cursor.execute(
            "UPDATE course "
            "SET keywords = %s "
            "WHERE id = %s;",
            (keywords, courseId)
        )
        self.connection.commit()

    def updateSecondLevelCategoryKeywords(self, keywords: string, categoryId: int):
        self.cursor.execute(
            "UPDATE classification_second_level "
            "SET keywords = %s "
            "WHERE id = %s;",
            (keywords, categoryId)
        )
        self.connection.commit()

    def insertCourseKeyword(self, word):
        try:
            self.cursor.execute(
                "INSERT INTO courses_keyword (name) "
                "VALUES (%s);",
                (word, )
            )
            self.connection.commit()
        except psycopg2.errors.UniqueViolation:
            self.connection.commit()

    def insertCategoryKeyword(self, word):
        try:
            self.cursor.execute(
                "INSERT INTO categories_keyword (name) "
                "VALUES (%s);",
                (word, )
            )
            self.connection.commit()
        except psycopg2.errors.UniqueViolation:
            self.connection.commit()

    def updateCoursesKeywordFrequency(self, frequency: int, keywordId: int):
        self.cursor.execute(
            "UPDATE courses_keyword "       
            "SET frequency = %s "   
            "WHERE id = %s;",
            (frequency, keywordId)
        )
        self.connection.commit()

    def updateCategoriesKeywordFrequency(self, frequency: int, keywordId: int):
        self.cursor.execute(
            "UPDATE categories_keyword "       
            "SET frequency = %s "   
            "WHERE id = %s;",
            (frequency, keywordId)
        )
        self.connection.commit()

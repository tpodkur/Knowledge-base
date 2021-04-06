import configparser
import psycopg2
import string


class ClassificationService:

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

    def getAllSecondLevelCategories(self):
        self.cursor.execute(
            "SELECT * FROM classification_second_level;"
        )
        return self.cursor.fetchall()

    def insertCourseSecondLevelRelation(self, courseId, categoryIg, keywordsIntersection, numberOfCommonKeywords, estimation):
        try:
            self.cursor.execute(
                "INSERT INTO course_second_level_relation (course_id, category_id, keywords_intersection, number_of_common_keywords, estimation) "
                "VALUES (%s, %s, %s, %s, %s);",
                (courseId, categoryIg, keywordsIntersection, numberOfCommonKeywords, estimation)
            )
            self.connection.commit()
        except psycopg2.errors.UniqueViolation:
            self.connection.commit()

    def getCourseSecondLevelRelation(self):
        self.cursor.execute(
            "SELECT "
            "c.name, c.link, "
            "cl.name, "
            "r.number_of_common_keywords "
            "FROM course_second_level_relation AS r "
            "INNER JOIN course AS c "
            "ON r.course_id = c.id "
            "INNER JOIN classification_second_level AS cl "
            "ON r.category_id = cl.id "
        )
        return self.cursor.fetchall()

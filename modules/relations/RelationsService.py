import configparser
import psycopg2


class  RelationsService:

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

    def getCourseSecondLevelRelations(self, courseId):
        self.cursor.execute(
            "SELECT "
            "c.id, c.name, c.link, "
            "cl.name, cl.id, "
            "r.number_of_common_keywords, r.estimation "
            "FROM course_second_level_relation AS r "
            "LEFT JOIN course AS c "
            "ON r.course_id = c.id "
            "LEFT JOIN classification_second_level AS cl "
            "ON r.category_id = cl.id "
        )

        allRelations = self.cursor.fetchall()
        courseRelations = []
        for relation in allRelations:
            if relation[0] == courseId:
                courseRelations.append(relation)

        return courseRelations

    def insertCoursesRelation(self, leftCourseId, rightCourseId, estimation):
        try:
            self.cursor.execute(
                "INSERT INTO courses_relation (left_course_id, right_course_id, estimation) "
                "VALUES (%s, %s, %s);",
                (leftCourseId, rightCourseId, estimation)
            )
            self.connection.commit()
        except psycopg2.errors.UniqueViolation:
            self.connection.commit()
import psycopg2

class CoursesMigrations:
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

    def coursesCountTable(self):
        self.cursor.execute(
            "CREATE TABLE courses_count ("
            "id              SERIAL PRIMARY KEY,"
            "platform        VARCHAR(100) NOT NULL,"
            "courses_count   BIGINT);"
        )
        self.connection.commit()

    # def categoriesTable(self):
    #     self.cursor.execute(
    #         "CREATE TABLE category ("
    #         "id              SERIAL PRIMARY KEY,"
    #         "name            VARCHAR(100) NOT NULL,"
    #         "number          VARCHAR(100) NOT NULL);"
    #     )
    #     self.connection.commit()

    def coursesTable(self):
        self.cursor.execute(
            "CREATE TABLE course ("
            "id              SERIAL PRIMARY KEY,"
            "name            VARCHAR(100) NOT NULL,"
            "platform        VARCHAR(100) NOT NULL,"
            "link            VARCHAR(255) NOT NULL,"
            "description     TEXT,"
            "content         TEXT,"
            "sphere         VARCHAR(100));"
        )
        self.connection.commit()

import configparser
import psycopg2
import string


class ClassificationService:
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

    def insertFirstLevelCategory(self, name: string, grnti_number: int):
        self.cursor.execute(
            "INSERT INTO classification_first_level (name, grnti_number) "
            "VALUES (%s, %s);",
            (name, grnti_number)
        )
        self.connection.commit()

    def insertSecondLevelCategory(self, name: string, grnti_number: int, parent_grnti_number: int):
        self.cursor.execute(
            "INSERT INTO classification_first_level (name, grnti_number, parent_grnti_number) "
            "VALUES (%s, %s, %s);",
            (name, grnti_number, parent_grnti_number)
        )
        self.connection.commit()

    def insertSecondLevelCategory(self, name: string, grnti_number: int, parent_grnti_number: int, parent_parent_grnti_number: int):
        self.cursor.execute(
            "INSERT INTO classification_first_level (name, grnti_number, parent_grnti_number, parent_parent_grnti_number) "
            "VALUES (%s, %s, %s);",
            (name, grnti_number, parent_grnti_number, parent_parent_grnti_number)
        )
        self.connection.commit()
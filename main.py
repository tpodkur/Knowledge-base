from migrations.CoursesMigrations import CoursesMigrations
from migrations.InitializationMigrations import InitializationMigrations
from migrations.CleanMigrations import CleanMigrations
from modules.parser.PagesSaverComponent import PagesSaverComponent
from modules.parser.ParserComponent import ParserComponent
from modules.parser.ClassificationSaverComponent import ClassificationSaverComponent
from modules.parser.ClassificationParserComponent import ClassifivationParserComponent
import configparser


def migrate():
    m = CoursesMigrations()
    # m.educationSpheresTable()
    # m.categoriesGroupsTable()
    # m.categoriesTable()
    m.coursesTable()

    # k = InitializationMigrations()
    # k.insertCategoriesGroups()
    # k.insertEducationSpheres()

    # t = CleanMigrations()
    # t.coursesTable()

def courses(config):


    baseUrl = config["urls"]["aggregatorUrl"]
    stepikCoursesUrl = config["urls"]["stepikCourses"]
    courseraCoursesUrl = config["urls"]["courseraCourses"]
    openEduCoursesUrl = config["urls"]["openEduCourses"]

    stepik = config["platforms"]["stepik"]
    coursera = config["platforms"]["coursera"]
    openEdu = config["platforms"]["openEdu"]

    # migrate()

    saver = PagesSaverComponent()
    parser = ParserComponent()

    # saver.loadCoursesListPages(baseUrl + stepikCoursesUrl, stepik)
    # parser.getCoursesLinksFromPages(stepik)
    # saver.loadCoursesPages(baseUrl, stepik)
    parser.completeCourseInformation(stepik)

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read("settings.ini")

    classificationUrl = config["urls"]["classification"]

    classifivationSaver = ClassificationSaverComponent()
    classifivationParser = ClassifivationParserComponent()

    # classifivationSaver.loadClassificationFirstLevel(classificationUrl)
    # classifivationParser.getSecondLevelLinksFromPage()
    # classifivationSaver.loadClassificationLevel(2, classificationUrl)
    classifivationParser.getSecondLevelLinksFromPage()




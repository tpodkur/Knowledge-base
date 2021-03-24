from migrations.CleanMigrations import CleanMigrations
from migrations.CoursesMigrations import CoursesMigrations
from migrations.WordsMigrations import WordsMigrations
from modules.parser.components.courses.PagesSaverComponent import PagesSaverComponent
from modules.parser.components.courses.ParserComponent import ParserComponent
from modules.parser.components.classification.ClassificationSaverComponent import ClassificationSaverComponent
from modules.parser.components.classification.ClassificationParserComponent import ClassifikationParserComponent
from modules.keywords.WordsComponent import WordsComponent
from modules.keywords.WordsService import WordsService
import configparser


def migrate():
    # m = CoursesMigrations()
    # m.educationSpheresTable()
    # m.categoriesGroupsTable()
    # m.categoriesTable()
    # m.coursesTable()

    # l = ClassificationMigrations()
    # l.firstLevelClassificationTable()
    # l.secondLevelClassificationTable()
    # l.thirdLevelClassificationTable()

    # k = InitializationMigrations()
    # k.insertCategoriesGroups()
    # k.insertEducationSpheres()

    g = WordsMigrations()
    g.keywordsTable()

    # t = CleanMigrations()
    # t.coursesTable()
    # t.classificationFirstLevelTable()
    # t.classificationSecondLevelTable()
    # t.classificationThirdLevelTable()
    # t.keywordsTable()

def courses(config):
    baseUrl = config["urls"]["aggregatorUrl"]
    stepikCoursesUrl = config["urls"]["stepikCourses"]
    courseraCoursesUrl = config["urls"]["courseraCourses"]
    openEduCoursesUrl = config["urls"]["openEduCourses"]

    stepik = config["platforms"]["stepik"]
    coursera = config["platforms"]["coursera"]
    openEdu = config["platforms"]["openEdu"]

    saver = PagesSaverComponent()
    parser = ParserComponent()

    # saver.loadCoursesListPages(baseUrl + stepikCoursesUrl, stepik)
    # parser.getCoursesLinksFromPages(stepik)
    # saver.loadCoursesPages(baseUrl, stepik)
    parser.completeCourseInformation(stepik)

def parseClassification(config):
    classificationUrl = config["urls"]["classification"]

    classifikationSaver = ClassificationSaverComponent()
    classifikationParser = ClassifikationParserComponent()

    # migrate()

    # classifikationSaver.loadClassificationFirstLevel(classificationUrl)
    # classifikationParser.getFirstLevelNamesFromPage()

    # classifikationParser.getSecondLevelLinksFromPage()
    # classifikationSaver.loadClassificationSecondLevels(classificationUrl)
    # classifikationParser.getSecondLevelNamesFromPage()

    # classifikationParser.getThirdLevelLinksFromPage()
    # classifikationSaver.loadClassificationThirdLevels(classificationUrl)
    # classifikationParser.getThirdLevelNamesFromPage()

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read("settings.ini")

    wordsComponent = WordsComponent()
    wordsService = WordsService()

    wordsComponent.extractKeywordsForCourses()
    # wordsComponent.completeKeywordsFromCourses()
    wordsComponent.completeKeywordsFrequency()



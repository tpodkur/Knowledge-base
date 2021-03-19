from migrations.CleanMigrations import CleanMigrations
from modules.parser.components.courses.PagesSaverComponent import PagesSaverComponent
from modules.parser.components.courses.ParserComponent import ParserComponent
from modules.parser.components.classification.ClassificationSaverComponent import ClassificationSaverComponent
from modules.parser.components.classification.ClassificationParserComponent import ClassifikationParserComponent
from modules.keywords.WordsComponent import WordsComponent
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

    t = CleanMigrations()
    # t.coursesTable()
    # t.classificationFirstLevelTable()
    t.classificationSecondLevelTable()
    # t.classificationThirdLevelTable()

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
    wordsComponent.getKeywords('за два месяца, на которые рассчитан курс, слушатели ознакомятся с некоторыми разделами дискретной математики. это линейная алгебра, комбинаторика, теория графов и дискретная вероятность. курс является очень вводным, базовым. он приоткроет дверь в прекрасный и удивительный мир дискретной математики, для более подробного знакомства с которым вам возможно потребуется более серьезные курсы. курс предназначен для школьников, которые хотят стать программистами, поступить на программистские кафедры и понять, какую математику им там предстоит изучать. а еще для тех, кто хочет поступить в магистратуру, или бакалавриат спбау, или в computer science центр. таким людям курс поможет успешно пройти собеседование.')
    # wordsComponent.getDescriptor('программныe')

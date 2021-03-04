from migrations.CoursesMigrations import CoursesMigrations
from modules.parser.PagesSaverComponent import PagesSaverComponent
from modules.parser.ParserComponent import ParserComponent
import configparser


def migrate():
    m = CoursesMigrations()
    m.coursesTable()

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read("settings.ini")

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
    parser.getCourseInformation(stepik)

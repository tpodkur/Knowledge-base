from Parser.PagesSaver import PagesSaver
from Migrations.CoursesMigrations import CoursesMigrations


def migrate():
    m = CoursesMigrations()
    m.coursesTable()

if __name__ == '__main__':

    baseUrl = "https://online.edu.ru"
    stepikCoursesUrl = "/public/courses?faces-redirect=true&pid=2919"
    courseraCoursesUrl = "/public/courses?faces-redirect=true&pid=11042928"
    openEdu = "/public/courses?faces-redirect=true&pid=3114"

    # migrate()

    saver = PagesSaver()
    # saver.loadCoursesListPages(baseUrl + stepikCoursesUrl, "Stepik")
    # saver.loadCoursesListPages(baseUrl + courseraCoursesUrl, "Coursera")
    # saver.loadCoursesListPages(baseUrl + openEdu, "OpenEdu")

    saver.run()

    # saver.getCoursesLinksFromPages("Stepik")
    # saver.getCoursesLinksFromPages("Coursera")
    # saver.getCoursesLinksFromPages("OpenEdu")

    # saver.loadCoursesPages(baseUrl, "Stepik")
    # saver.loadCoursesPages(baseUrl, "Coursera")
    # saver.loadCoursesPages(baseUrl, "OpenEdu")

    # saver.parseCourseInformation("Stepik")

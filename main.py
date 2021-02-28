from Parser.PagesSaver import PagesSaver


if __name__ == '__main__':

    baseUrl = "https://online.edu.ru"
    stepikCoursesUrl = "/public/courses?faces-redirect=true&pid=2919"
    courseraCoursesUrl = "/public/courses?faces-redirect=true&pid=11042928"
    openEdu = "/public/courses?faces-redirect=true&pid=3114"

    saver = PagesSaver()
    # saver.loadCoursesListPages(baseUrl + stepikCoursesUrl, "Stepik")
    # saver.loadCoursesListPages(baseUrl + courseraCoursesUrl, "Coursera")
    # saver.loadCoursesListPages(baseUrl + openEdu, "OpenEdu")

    # saver.run()

    saver.getCoursesLinksFromPages("Stepik")
    saver.getCoursesLinksFromPages("Coursera")
    saver.getCoursesLinksFromPages("OpenEdu")


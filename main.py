from Parser.PagesSaver import PagesSaver


if __name__ == '__main__':

    baseUrl = "https://online.edu.ru"
    stepikCoursesUrl = "/public/courses?faces-redirect=true&pid=2919"
    courseraCoursesUrl = "/public/courses?faces-redirect=true&pid=11042928"
    openEdu = "/public/courses?faces-redirect=true&pid=3114"

    coursera_parser = PagesSaver()
    coursera_parser.loadCoursesPages(baseUrl + stepikCoursesUrl, "Stepik")
    coursera_parser.loadCoursesPages(baseUrl + courseraCoursesUrl, "Coursera")
    coursera_parser.loadCoursesPages(baseUrl + openEdu, "OpenEdu")
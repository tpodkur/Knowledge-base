from modules.parser.ParserService import ParserService
from lxml import html
from bs4 import BeautifulSoup
import string


class ParserComponent:
    url: str = "https://online.edu.ru/public/courses?faces-redirect=true&pid=2919"
    service: ParserService

    def __init__(self):
        self.service = ParserService()

    def getCoursesLinksFromPages(self, platform: string):
        fileToWrite = open("pages/courses-links/" + platform + ".txt", "w")
        for i in range(20):
            root = html.parse("pages/courses-list-pages/" + platform + "/page" + str(i) + ".html").getroot()
            elements = root.find_class("card course-card")

            links = ""
            for element in elements:
                links = links + str(element[1][0][0].get('href')) + "\n"

            fileToWrite.write(links)
        fileToWrite.close()

    def completeCourseInformation(self, platform: string):
        fileWithCoursesLinks = open("pages/courses-links/" + platform + ".txt", 'r')
        links: [string] = fileWithCoursesLinks.read().splitlines()

        for i in range(len(links)):
            filePath = "pages/courses-pages/" + platform + "/course" + str(i) + ".html"
            root = html.parse(filePath).getroot()
            try:
                courseName = root.find_class("course-name")
                courseCategory = root.get_element_by_id("j_idt136")
                courseLink = root.get_element_by_id("j_idt84:j_idt85")
                courseContent = root.get_element_by_id("j_idt131")
                courseSphere = root.get_element_by_id("j_idt141")
            except KeyError:
                courseCategory = html.Element("div")
                courseCategory.text = ""
                continue

            cName = courseName[0].text_content().lower()
            cCategories = self.prepareCategories(courseCategory.text_content())
            cPlatform = platform
            cLink = self.prepareCourseLink(courseLink.get("onclick"))
            cContent = courseContent.text_content().lower()
            cSphere = courseSphere.text_content().lower()

            html_doc = open(filePath)
            soup = BeautifulSoup(html_doc, "lxml")
            cDescription = str(soup.find('div', id='course-view-about'))

            course_id = self.service.insertCourseInformation(cName, cCategories, cPlatform, cLink, cDescription, cContent, cSphere)

    def prepareCourseLink(self, link: string):
        return link.removeprefix("window.open('").removesuffix("','_self')").replace("\/", "/")

    def prepareCategories(self, categories: string):
        categoriesArr = categories.split('\n')
        categoriesStr = ''
        for category in categoriesArr:
            categoriesStr = categoriesStr + category.lstrip() + ','
        return categoriesStr[:categoriesStr.rfind(",,")]

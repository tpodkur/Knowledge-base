from modules.parser.ParserService import ParserService
from lxml import html
import string


class ParserComponent:
    url: str = "https://online.edu.ru/public/courses?faces-redirect=true&pid=2919"
    service: ParserService

    def __init__(self):
        self.service = ParserService()

    def getCoursesLinksFromPages(self, platform: string):
        for i in range(20):
            root = html.parse("pages/courses-list-pages/" + platform + "/page" + str(i) + ".html").getroot()
            elements = root.find_class("card course-card")

            links = ""
            for element in elements:
                links = links + str(element[1][0][0].get('href')) + "\n"

            fileToWrite = open("pages/courses-links/" + platform + ".txt", "w")
            fileToWrite.write("%s" % links)
            fileToWrite.close()

    def getCourseInformation(self, platform: string):
        fileWithCoursesLinks = open("pages/courses-links/" + platform + ".txt", 'r')
        links: [string] = fileWithCoursesLinks.read().splitlines()

        for i in range(len(links)):
            root = html.parse("pages/courses-pages/" + platform + "/course" + str(i) + ".html").getroot()
            try:
                courseName = root.find_class("course-name")
                courseCategory = root.get_element_by_id("j_idt136")
                courseLink = root.get_element_by_id("j_idt84:j_idt85")
                courseDescription = root.get_element_by_id("course-view-about")
                courseContent = root.get_element_by_id("j_idt131")
                courseSphere = root.get_element_by_id("j_idt141")
            except KeyError:
                courseCategory = html.Element("div")
                courseCategory.text = ""

            print(courseName[0].text_content())
            print(courseCategory.text_content())
            print(courseLink.get("onclick"))
            # print(courseDescription[1].text_content())
            print(courseContent.text_content())
            print(courseSphere.text_content())
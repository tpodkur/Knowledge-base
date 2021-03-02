from lxml import html
import requests
import string
from DatabaseServices.CoursesService1 import CoursesService


class PagesSaver:
    url: str = "https://online.edu.ru/public/courses?faces-redirect=true&pid=2919"
    service: CoursesService

    def __init__(self):
        self.service = CoursesService()

    def run(self):
        i = 0
        platform = "Stepik"
        root = html.parse("CoursesPages/" + platform + "/course" + str(i) + ".html").getroot()
        courseName = root.find_class("course-name")
        courseCategory = root.get_element_by_id("j_idt136")
        courseLink = root.get_element_by_id("j_idt84:j_idt85")
        courseDescription = root.get_element_by_id("course-view-about")
        courseContent = root.get_element_by_id("j_idt131")
        courseSphere = root.get_element_by_id("j_idt141")


        print(courseName[0].text)
        print(courseCategory.text)
        print(courseLink.get("onclick"))
        # print(courseDescription)
        print(courseContent.text)
        print(courseSphere.text)


    def loadCoursesListPages(self, url: string, platform: string):
        for pageNumber in range(20):
            page = requests.get(url + "&page=" + str(pageNumber))
            fileToWrite = open("CoursesListPages/" + platform + "/page" + str(pageNumber) + ".html", "w")
            fileToWrite.write(page.text)
            fileToWrite.close()

    def getCoursesLinksFromPages(self, platform: string):
        for i in range(20):
            root = html.parse("CoursesListPages/" + platform + "/page" + str(i) + ".html").getroot()
            elements = root.find_class("card course-card")

            # links = []
            links = ""
            for element in elements:
                # links.append(element[1][0][0].get('href'))
                links = links + str(element[1][0][0].get('href')) + "\n"

            fileToWrite = open("CoursesLinks/" + platform + ".txt", "w")
            # fileToWrite.writelines(links)
            fileToWrite.write(links)
            fileToWrite.close()

    def loadCoursesPages(self, url: string, platform: string):
        fileToRead = open("CoursesLinks/" + platform + ".txt", 'r')
        links: [string] = fileToRead.read().splitlines()
        for i in range(len(links)):
            page = requests.get(url + links[i])
            fileToWrite = open("CoursesPages/" + platform + "/course" + str(i) + ".html", "w")
            fileToWrite.write(page.text)
            fileToWrite.close()

        self.service.insertCoursesCount(platform, len(links))

    def parseCourseInformation(self, platform: string):
        coursesCount = self.service.getCoursesCount(platform)

        for i in range(coursesCount):
            root = html.parse("CoursesPages/" + platform + "/course" + str(i) + ".html").getroot()
            courseName = root.find_class("course-name")
            courseCategory = root.get_element_by_id("j_idt136")
            courseLink = root.get_element_by_id("j_idt84:j_idt85")
#           courseDescription = root.get_element_by_id("course-view-about")
            courseContent = root.get_element_by_id("j_idt131")
            courseSphere = root.get_element_by_id("j_idt141")


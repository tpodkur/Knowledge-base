import string
from lxml import html
import requests


class PagesSaver:
    url: str = "https://online.edu.ru/public/courses?faces-redirect=true&pid=2919"
    SCROLL_PAUSE_TIME = 5

    def __init__(self):
        self.driver = None

    def run(self):
        pageNumber = 1
        url = "https://online.edu.ru/public/courses?faces-redirect=true&pid=2919"
        platform = "Stepik"
        page = requests.get(url + "&page=" + str(pageNumber))
        tree = html.fromstring(page.content)

        root = html.parse("CoursesListPages/Stepik/page0.html").getroot()
        elements = root.find_class("card course-card")
        for element in elements:
            print(element[1][0][0].get('href'))

        fileToWrite = open("CoursesListPages/" + str(platform) + "/page" + str(pageNumber) + ".html", "w")
        # fileToWrite.write(tree)
        fileToWrite.close()

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

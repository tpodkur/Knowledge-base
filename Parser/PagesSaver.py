import string
import requests


class PagesSaver:
    url: str = "https://online.edu.ru/public/courses?faces-redirect=true&pid=2919"
    SCROLL_PAUSE_TIME = 5

    def __init__(self):
        self.driver = None

    def run(self):
        return True

    def loadCoursesPages(self, url: string, platform: string):
        for pageNumber in range(20):
            page = requests.get(url + "&page=" + str(pageNumber))
            fileToWrite = open("CoursesPages/" + str(platform) + "/page" + str(pageNumber) + ".html", "w")
            fileToWrite.write(page.text)
            fileToWrite.close()
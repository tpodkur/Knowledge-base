from modules.parser.ParserService import ParserService
import requests
import string


class PagesSaverComponent:
    service: ParserService

    def __init__(self):
        self.service = ParserService()

    def loadCoursesListPages(self, url: string, platform: string):
        for pageNumber in range(20):
            page = requests.get(url + "&page=" + str(pageNumber))
            fileToWrite = open("pages/courses-list-pages/" + platform + "/page" + str(pageNumber) + ".html", "w")
            fileToWrite.write(page.text)
            fileToWrite.close()

    def loadCoursesPages(self, url: string, platform: string):
        fileToRead = open("pages/courses-links/" + platform + ".txt", "r")
        links: [string] = fileToRead.read().splitlines()
        for i in range(len(links)):
            page = requests.get(url + links[i])
            fileToWrite = open("pages/courses-pages/" + platform + "/course" + str(i) + ".html", "w")
            fileToWrite.write(page.text)
            fileToWrite.close()

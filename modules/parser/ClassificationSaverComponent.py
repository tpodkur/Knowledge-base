from modules.parser.ParserService import ParserService
import requests
import string


class ClassificationSaverComponent:
    service: ParserService

    def __init__(self):
        self.service = ParserService()

    def loadClassificationFirstLevel(self, baseUrl: string):
        page = requests.get(baseUrl)
        fileToWrite = open("pages/classification/first-level/first-level.html", "w")
        fileToWrite.write(page.text)
        fileToWrite.close()

    def loadClassificationSecondLevels(self, baseUrl: string):
        fileToRead = open("pages/classification/second-level/links.txt", "r")
        links: [string] = fileToRead.read().splitlines()
        for i in range(len(links)):
            page = requests.get(baseUrl + links[i])
            fileToWrite = open("pages/classification/second-level/second-level" + str(i) + ".html", "w")
            fileToWrite.write(page.text)
            fileToWrite.close()

    def loadClassificationThirdLevels(self, baseUrl: string):
        fileToRead = open("pages/classification/third-level/links.txt", "r")
        links: [string] = fileToRead.read().splitlines()
        for i in range(len(links)):
            page = requests.get(baseUrl + links[i])
            fileToWrite = open("pages/classification/third-level/third-level" + str(i) + ".html", "w")
            fileToWrite.write(page.text)
            fileToWrite.close()
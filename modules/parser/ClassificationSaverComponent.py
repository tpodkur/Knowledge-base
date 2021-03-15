from modules.parser.ParserService import ParserService
import requests
import string


class ClassificationSaverComponent:
    service: ParserService
    nestingLevel = {
        2: "second",
        3: "third"
    }

    def __init__(self):
        self.service = ParserService()

    def loadClassificationFirstLevel(self, baseUrl: string):
        page = requests.get(baseUrl)
        fileToWrite = open("pages/classification/first-level/first-level.html", "w")
        fileToWrite.write(page.text)
        fileToWrite.close()

    def loadClassificationLevel(self, nestingLevel: int, baseUrl: string):
        level = self.nestingLevel[nestingLevel]
        fileToRead = open("pages/classification/" + level + "-level/links.txt", "r")
        links: [string] = fileToRead.read().splitlines()
        for i in range(len(links)):
            page = requests.get(baseUrl + links[i])
            fileToWrite = open("pages/classification/" + level + "-level/" + level + "-level" + str(i) + ".html", "w")
            fileToWrite.write(page.text)
            fileToWrite.close()

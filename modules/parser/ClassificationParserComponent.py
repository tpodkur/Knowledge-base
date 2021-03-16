from modules.parser.ParserService import ParserService
from lxml import html
import string


class ClassifikationParserComponent:
    service: ParserService

    def __init__(self):
        self.service = ParserService()

    def getSecondLevelLinksFromPage(self):
        root = html.parse("pages/classification/first-level/first-level.html").getroot()
        grnt_list = root.find_class("grnt_list")

        fileToWrite = open("pages/classification/second-level/links.txt", "w")
        links = ""
        for listItem in grnt_list[0]:
            links = links + str(listItem[0].get('href')) + "\n"
        fileToWrite.write(links)
        fileToWrite.close()

    def getThirdLevelLinksFromPage(self):
        fileToRead = open("pages/classification/second-level/links.txt", "r")
        secondLevelLinks: [string] = fileToRead.read().splitlines()
        fileToWrite = open("pages/classification/third-level/links.txt", "w")
        links = ""
        for i in range(len(secondLevelLinks)):
            root = html.parse("pages/classification/second-level/second-level" + str(i) + ".html").getroot()
            grnt_list = root.find_class("grnt_list")

            for listItem in grnt_list[0]:
                links = links + str(listItem[0].get('href')) + "\n"
        fileToWrite.write(links)
        fileToWrite.close()

    def getFirstLevelNamesFromPage(self):
        root = html.parse("pages/classification/first-level/first-level.html").getroot()
        grnt_list = root.find_class("grnt_list")

        for listItem in grnt_list[0]:
            print(str(listItem[0].text_content()).encode('latin1').decode('utf-8').lower())


    def getSecondLevelNamesFromPage(self):
        fileToRead = open("pages/classification/second-level/links.txt", "r")
        links: [string] = fileToRead.read().splitlines()
        for i in range(len(links)):
            root = html.parse("pages/classification/second-level/second-level" + str(i) + ".html").getroot()
            grnt_list = root.find_class("grnt_list")

            for listItem in grnt_list[0]:
                print(str(listItem[0].text_content()).encode('latin1').decode('utf-8').lower())

    def getThirdLevelNamesFromPage(self):
        fileToRead = open("pages/classification/third-level/links.txt", "r")
        links: [string] = fileToRead.read().splitlines()
        for i in range(len(links)):
            root = html.parse("pages/classification/third-level/third-level" + str(i) + ".html").getroot()
            grnt_list = root.find_class("grnt_list")

            for listItem in grnt_list[0]:
                print(str(listItem[0].text_content()).encode('latin1').decode('utf-8').lower())

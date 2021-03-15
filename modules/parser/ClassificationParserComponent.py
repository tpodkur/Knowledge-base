from modules.parser.ParserService import ParserService
from lxml import html


class ClassifivationParserComponent:
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

            print(listItem[0].text_content())

            # fileToWrite.write(links)
        fileToWrite.close()

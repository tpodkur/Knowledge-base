from modules.keywords.WordsService import WordsService
import string
import pymorphy2
import re


class WordsComponent:
    service: WordsService

    def __init__(self):
        conjunctionsFile = open("modules/keywords/invalid-words/conjunctions.txt", 'r')
        particlesFile = open("modules/keywords/invalid-words/particles.txt", 'r')
        prepositionsFile = open("modules/keywords/invalid-words/prepositions.txt", 'r')
        pronounsFile = open("modules/keywords/invalid-words/pronouns.txt", 'r')
        otherInvalidWordsFile = open("modules/keywords/invalid-words/other-invalid-words.txt", 'r')

        self.conjunctions: [string] = conjunctionsFile.read().splitlines()
        self.particles: [string] = particlesFile.read().splitlines()
        self.prepositions: [string] = prepositionsFile.read().splitlines()
        self.pronouns: [string] = pronounsFile.read().splitlines()
        self.otherInvalidWords: [string] = otherInvalidWordsFile.read().splitlines()

        self.morph = pymorphy2.MorphAnalyzer()
        self.service = WordsService()

    def getKeywords(self, text: string):
        pattern = r'\w+'
        words = re.findall(pattern, text)

        usefulWords = []
        for word in words:
            wordVariants = self.morph.parse(word)

            if ('NOUN' in wordVariants[0].tag) or ('ADJF' in wordVariants[0].tag):
                usefulWords.append(word)

        descriptors = []
        for word in usefulWords:
            descriptors.append(self.getDescriptor(word))

        return self.deleteInvalidWords(self.deleteRepeatedWords(descriptors))

    def extractKeywordsForCourses(self):
        courses = self.service.getAllCourses()

        for course in courses:
            nameKeywords = self.getKeywords(course[1])
            descriptionKeywords = self.getKeywords(course[5])
            contentKeywords = self.getKeywords(course[6])
            sphereKeywords = self.getKeywords(course[7])

            keywords = self.deleteRepeatedWords(nameKeywords + descriptionKeywords + contentKeywords + sphereKeywords)

            keywordsStr = ','.join(keywords)
            self.service.updateCourseKeywords(keywordsStr, course[0])

    def completeKeywordsFromCourses(self):
        courses = self.service.getAllCourses()

        allKeywords = []
        for course in courses:
            keywords = course[8]
            keywords = keywords.split(',')
            allKeywords = allKeywords + keywords

        uniqueKeywords = self.deleteRepeatedWords(allKeywords)
        for word in uniqueKeywords:
            self.service.insertCourseKeyword(word)

    def extractKeywordsForSecondLevelCategories(self):
        secondLevelCategories = self.service.getAllSecondLevelCategories()
        for category in secondLevelCategories:
            thirdLevelCategories = self.service.getThirdLevelCategoriesByParent(category[2])

            keywords = []
            for subcategory in thirdLevelCategories:
                keywords = keywords + self.getKeywords(subcategory[1])
            keywords = self.deleteRepeatedWords(keywords)
            keywordsStr = ','.join(keywords)
            self.service.updateSecondLevelCategoryKeywords(keywordsStr, category[0])

    def completeKeywordsFromSecondLevelCategories(self):
        secondLevelCategories = self.service.getAllSecondLevelCategories()

        allKeywords = []
        for category in secondLevelCategories:
            keywords = category[4]
            keywords = keywords.split(',')
            allKeywords = allKeywords + keywords

        uniqueKeywords = self.deleteRepeatedWords(allKeywords)
        for word in uniqueKeywords:
            self.service.insertCategoryKeyword(word)

    def completeFrequencyForCoursesKeywords(self):
        keywords = self.service.getAllCoursesKeywords()

        for keyword in keywords:
            frequency = self.calculateFrequencyOfOccurrenceForCoursesWord(keyword[1])
            self.service.updateCoursesKeywordFrequency(frequency, keyword[0])

    def completeFrequencyForCategoriesKeywords(self):
        keywords = self.service.getAllCategoriesKeywords()

        for keyword in keywords:
            frequency = self.calculateFrequencyOfOccurrenceForCategoriesWord(keyword[1])
            self.service.updateCategoriesKeywordFrequency(frequency, keyword[0])

    def calculateFrequencyOfOccurrenceForCoursesWord(self, word: string):
        courses = self.service.getAllCourses()
        counter = 0
        for course in courses:
            keywords = course[8]
            if (keywords.find(word) != -1):
                counter = counter + 1
        return counter

    def calculateFrequencyOfOccurrenceForCategoriesWord(self, word: string):
        categories = self.service.getAllSecondLevelCategories()
        counter = 0
        for category in categories:
            keywords = category[4]
            if (keywords.find(word) != -1):
                counter = counter + 1
        return counter

    def deleteInvalidWords(self, wordsArray: [string]):
        for word in self.otherInvalidWords + self.pronouns:
            if word in wordsArray:
                wordsArray.remove(word)
        return wordsArray

    def getDescriptor(self, word: string):
        wordsVariants = self.morph.parse(word)
        return wordsVariants[0].normalized.word

    def deleteRepeatedWords(self, array):
        return list(dict.fromkeys(array))

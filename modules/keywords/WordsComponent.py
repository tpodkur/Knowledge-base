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
        otherInvalidWordsFile = open("modules/keywords/invalid-words/other-invalid-words.txt", 'r')

        self.conjunctions: [string] = conjunctionsFile.read().splitlines()
        self.particles: [string] = particlesFile.read().splitlines()
        self.prepositions: [string] = prepositionsFile.read().splitlines()
        self.otherInvalidWords: [string] = otherInvalidWordsFile.read().splitlines()

        self.morph = pymorphy2.MorphAnalyzer()
        self.service = WordsService()

    def getKeywords(self, text: string):
        # invalidWords = self.conjunctions + self.particles + self.prepositions
        # invalidWords.sort(key=len)
        # invalidWords.reverse()
        # for word in invalidWords:
        #     text = text.replace(' ' + word + ' ', ' ')

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
            self.service.insertKeywordsToCourse(keywordsStr, course[0])

    def deleteInvalidWords(self, wordsArray: [string]):
        for word in self.otherInvalidWords:
            if word in wordsArray:
                wordsArray.remove(word)
        return wordsArray

    def getDescriptor(self, word: string):
        wordsVariants = self.morph.parse(word)
        return wordsVariants[0].normalized.word

    def deleteRepeatedWords(self, array):
        return list(dict.fromkeys(array))

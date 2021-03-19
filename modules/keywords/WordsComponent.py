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

        self.conjunctions: [string] = conjunctionsFile.read().splitlines()
        self.particles: [string] = particlesFile.read().splitlines()
        self.prepositions: [string] = prepositionsFile.read().splitlines()

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
        print(usefulWords)

    def getDescriptor(self, word: string):
        wordsVariants = self.morph.parse(word)
        return wordsVariants[0].normalized.word
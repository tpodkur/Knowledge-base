from modules.classification.ClassificationService import ClassificationService
import string


class ClassificationComponent:
    service: ClassificationService

    def __init__(self):
        self.service = ClassificationService()

    def buildСlassification(self):
        courses = self.service.getAllCourses()
        categories = self.service.getAllSecondLevelCategories()

        counter = 0

        for course in courses:
            courseKeywords = course[8]
            courseKeywords = courseKeywords.split(',')

            for category in categories:
                categoryKeywords = category[4]
                categoryKeywords = categoryKeywords.split(',')

                intersection = list(set(courseKeywords) & set(categoryKeywords))
                intersectionStr = ','.join(intersection)

                estimation = self.calculateEstimationOfCourseBelongingToCategory(courseKeywords, categoryKeywords)
                estimation = round(estimation, 2)

                if estimation > 0:
                    self.service.insertCourseSecondLevelRelation(course[0], category[0], intersectionStr, len(intersection), estimation)

            counter = counter + 1
            if counter > 3:
                break

    def calculateEstimationOfCourseBelongingToCategory(self, courseKeywords: [string], categoryKeywords: [string]):
        intersection = list(set(courseKeywords) & set(categoryKeywords))
        return len(intersection) / len(categoryKeywords)

    def showClassificationResult(self):
        courseCategoryRelations = self.service.getCourseSecondLevelRelation()
        print(courseCategoryRelations)

        res = ""
        coursesNames = []
        for ralation in courseCategoryRelations:
            coursesNames.append(ralation[0])
        coursesNames = list(set(coursesNames))

        for courseName in coursesNames:
            res = res + courseName + ":" + "\n"
            currentCategories = []
            for relation in courseCategoryRelations:
                if (relation[0] == courseName):
                    currentCategories.append(relation)
                    # res = res + "    " + relation[2] + " " + str(relation[3]) + "\n"
            currentCategories.sort(key=lambda tup: tup[3])

            for category in currentCategories:
                res = res + "    " + category[2] + " " + str(category[3]) + "\n"

        fileToWrite = open("modules/classification/classification-result.txt", "w")
        fileToWrite.write(res)



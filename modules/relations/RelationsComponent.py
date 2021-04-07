from modules.relations.RelationsService import RelationsService


class RelationsComponent:
    service: RelationsService

    def __init__(self):
        self.service = RelationsService()

    def buildRelations(self):
        courses = self.service.getAllCourses()

        for i, currentCourse in enumerate(courses):
            for j in range(i+1, len(courses)):
                estimation = self.calculateEstimationOfCoursesRelation(currentCourse, courses[j])
                if estimation != 0:
                    self.service.insertCoursesRelation(currentCourse[0], courses[j][0], estimation)

    def calculateEstimationOfCoursesRelation(self, leftCourse, rightCourse):
        intersectionKeywords = list(set(self.getCourseKeywords(leftCourse)) & set(self.getCourseKeywords(rightCourse)))
        estimationOfIntersectionKeywords = len(intersectionKeywords)

        leftCourseCategoryRelations = self.service.getCourseSecondLevelRelations(leftCourse[0])
        rightCourseCategoryRelations = self.service.getCourseSecondLevelRelations(rightCourse[0])

        estimationOfIntersectionCategories = 0
        for relation1 in leftCourseCategoryRelations:
            for relation2 in rightCourseCategoryRelations:
                if relation1[4] == relation2[4]:
                    estimationByCategory = (relation1[6] + relation2[6]) / 2
                    estimationOfIntersectionCategories = estimationOfIntersectionCategories + estimationByCategory

        k1 = 1
        k2 = 1
        return k1 * estimationOfIntersectionKeywords + k2 * estimationOfIntersectionCategories

    def getCourseKeywords(self, course):
        courseKeywords = course[8]
        return courseKeywords.split(',')



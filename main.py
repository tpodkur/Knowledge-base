from StepikParser import StepikParser
from CourseraParser import CourseraParser


def main():
    stepik_parser = StepikParser()
    coursera_parser = CourseraParser()
    coursera_parser.run()


if __name__ == '__main__':
    main()

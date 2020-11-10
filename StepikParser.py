from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TypesService import TypesService
import time


class StepikParser:
    url: str = "https://stepik.org/catalog"
    SCROLL_PAUSE_TIME = 5

    def __init__(self):
        self.driver = None
        self.types_service = TypesService()

    def run(self):
        self.driver = webdriver.Chrome()
        links = self.extract_sections_from_page(StepikParser.url)

        courses = []
        for link in links:
            courses_from_page = self.extract_courses_from_section_page(link['href'], link['section'])
            print(courses_from_page)
            courses = courses + courses_from_page

        self.driver.quit()
        print(courses)

    # return array of object {'href': , 'section': }
    def extract_sections_from_page(self, catalog_url: str):
        self.driver.get(catalog_url)
        time.sleep(5)

        # try:
        #     element = WebDriverWait(self.driver, 100).until(
        #         EC.presence_of_element_located((By.CLASS_NAME, 'st-course-filters'))
        #     )
        # finally:
        #     self.driver.quit()

        course_sets: [] = self.driver \
            .find_element_by_class_name('st-course-filters') \
            .find_elements_by_class_name('st-filter')

        course_sets_links = []
        for course_set in course_sets:
            list_items = course_set.find_elements_by_class_name('st-filter__item')
            for list_item in list_items:
                link_element = list_item.find_element_by_class_name('st-filter__link')
                link = self.types_service.form_link(link_element.get_attribute("href"), link_element.text)
                course_sets_links.append(link)
        return course_sets_links

    # return array of object {'href': , 'section': }
    def extract_courses_from_section_page(self, section_page_url: str, section_name: str):
        self.driver.get(section_page_url)
        time.sleep(5)

        course_pack = self.driver.find_element_by_class_name('course-pack')
        li_items = course_pack.find_elements_by_class_name('course-pack-list__item')
        self.scroll_page_down()

        courses = []
        for li_item in li_items:
            link_tag = li_item.find_element_by_class_name('ember-link')
            # link = link_tag.get_attribute('href')
            link = self.types_service.form_link(link_tag.get_attribute('href'), section_name)
            courses.append(link)
        return courses

    # return object { 'title': , 'description': , 'cost': }
    def extract_course_info(self, course_page_url: str):
        self.driver.get(course_page_url)
        time.sleep(5)

        title = self.driver.find_element_by_class_name('course-promo__header')
        description = self.driver.find_element_by_class_name('shortened-text')
        cost = self.driver.find_element_by_class_name('course-promo-enrollment__price')
        cost = 0 if (cost.text == 'Бесплатно') else int(cost)
        rating = self.driver.find_element_by_class_name('course-promo-summary__average').text
        return self.types_service.form_course(title, description, cost, float(rating))

    # void
    def scroll_page_down(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(StepikParser.SCROLL_PAUSE_TIME)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

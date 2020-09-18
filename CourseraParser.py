from selenium import webdriver
import time


class CourseraParser:
    url: str = "https://www.coursera.org/browse"
    SCROLL_PAUSE_TIME = 5

    def __init__(self):
        self.driver = None

    def run(self):
        self.driver = webdriver.Chrome()
        self.extract_sections_from_page(CourseraParser.url)

        self.driver.quit()

    def extract_sections_from_page(self, catalog_url: str):
        self.driver.get(catalog_url)
        time.sleep(5)

        div_items: [] = self.driver \
            .find_element_by_class_name('topic-skills-wrapper') \
            .find_element_by_class_name('slick-list') \
            .find_elements_by_class_name('slick-slide')

        for div_item in div_items:
            if not div_item.get_attribute('tabindex'):
                links = div_item.find_elements_by_tag_name('a')
                for link in links:
                    href = link.get_attribute('href')
                    print(href)

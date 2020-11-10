from selenium import webdriver
from TypesService import TypesService
import time


class CourseraParser:
    url: str = "https://www.coursera.org/browse"
    SCROLL_PAUSE_TIME = 5

    def __init__(self):
        self.driver = None
        self.types_service = TypesService()

    def run(self):
        self.driver = webdriver.Chrome()
        sections = self.extract_sections_from_page(CourseraParser.url)

        # здесь нужно сложить названия категорий в бд

        for section in sections:

            # надо убрать этот костыль:
            if (section['section'] != 'Личное развитие') and (section['section'] != 'Математика и логика'):
                subcategories = self.extract_subcategories(section['href'])

        # здесь нужно сложить названия подкатегорий в бд

        # для категорий, у которых нет подкатегорий (Личное развитие, Математика и логика)
        # нужно сделать одноименные подкатегории

        self.driver.quit()

    # return objects {'href': , 'section': }
    def extract_sections_from_page(self, catalog_url: str):
        self.driver.get(catalog_url)
        time.sleep(5)

        div_items: [] = self.driver \
            .find_element_by_class_name('topic-skills-wrapper') \
            .find_element_by_class_name('slick-list') \
            .find_elements_by_class_name('slick-slide')

        links = []
        for div_item in div_items:
            if not div_item.get_attribute('tabindex'):
                a_tags = div_item.find_elements_by_tag_name('a')
                for a_tag in a_tags:
                    href = a_tag.get_attribute('href')
                    section_name = a_tag.get_attribute('aria-label')
                    print(section_name)

                    link = self.types_service.form_link(href, section_name)
                    links.append(link)

        return links

    # return objects {'href': , 'section': }
    def extract_subcategories(self, section_page_url: str):
        self.driver.get(section_page_url)
        time.sleep(5)

        subcategories = self.driver \
            .find_element_by_class_name('rc-SubdomainCarousel') \
            .find_element_by_class_name('slick-track') \
            .find_elements_by_class_name('slick-slide')

        print(len(subcategories))

        links = []
        for subcategory in subcategories:
            a_tags = subcategory.find_elements_by_tag_name('a')

            for a_tag in a_tags:
                href = a_tag.get_attribute('href')

                # Проблема: имена подкатегорий, которые не отображены на веб-стр, записывает как пустые строки
                # (см. подкатегории "здоровья" и "Естественных и технических наук")
                subcategory_name = a_tag.find_element_by_tag_name('h2').text
                print(subcategory_name)

                link = self.types_service.form_link(href, subcategory_name)
                links.append(link)

        return links

    # return objects {'href': , 'section': }
    # def extract_courses_from_section_page(self, section_page_url: str, section_name: str):
    #     self.driver.get(section_page_url)
    #     time.sleep(5)
    #
    #     next_page_href = None
    #     choose_page_buttons = self.driver.find_elements_by_class_name('_dtnmh78')
    #     for button in choose_page_buttons:
    #         tag_attribute_data = button.get_attribute('data')
    #         if tag_attribute_data == 'right-arrow':
    #             next_page_href = button.get_attribute('href')
    #
    #     courses_links = []
    #     while next_page_href:
    #         self.driver.get(next_page_href)
    #         time.sleep(5)
    #         li_items = self.driver.find_elements_by_class_name('ais-InfiniteHits-item')
    #         for li_item in li_items:
    #             href = li_item.find_elements_by_tag_name('a').get_attribute('href')
    #             link = self.types_service.form_link(href, section_name)
    #             # courses_links.append(link)
    #
    #            next_page_href = self.driver.find_element_by_class_name('_dtnmh78').get_attribute('href')
    #     return courses_links

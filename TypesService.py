

class TypesService:

    # return object {'href': , 'section': }
    def form_link(self, href: str, section_name: str):
        return {
            'href': href,
            'section': section_name
        }

    # return object { 'title': , 'description': , 'cost': }
    def form_course(self, title: str, description: str, cost: int, rating: float):
        return {
            'title': title,
            'description': description,
            'cost': cost,
            'rating': rating
        }

    def form_heading(self, category, subcategory):
        return {
            'category': category,
            'subcategory': subcategory
        }
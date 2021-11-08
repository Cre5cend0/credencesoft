from core_files.dog_supplies import dog_food_categories
from core_files.dog_supplies_wet_food import dog_wet_food
from core_files.product_page import product_details
from core_files.category_pages import pagination_size


test_url = 'https://www.chewy.com/b/veterinary-diets-459'
test_url_product_details = 'https://www.chewy.com/iams-adult-minichunks-small-kibble/dp/36399'


if __name__ == "__main__":
    print("All Dog food Categories: ", dog_food_categories())
    print("All product links: ", dog_wet_food()) # Will take time, as it searches for all products in the category
    print("Number of pages with products in category: ", pagination_size(test_url))
    print("Product details: ", product_details(test_url_product_details))

from utilities.logger import logger
from utilities.config import MetaData
from utilities.setup import setup_bs

URL = MetaData.URL + '/b/dog-288'
log = logger()
soup = setup_bs(URL)


def dog_food_categories():
    """
    return: All categories of dog food -> list
    """
    slider = soup.find('ul', class_="bxslider")  # finding the parent class of all categories
    categories = slider.find_all("li")  # listing out all category elements
    my_list = []

    log.info('Listing dog food categories')
    for item in categories:
        category = item.a.p.text # extracting text from all category elements
        my_list.append(category)
    return my_list
